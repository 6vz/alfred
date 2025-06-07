import os
import json
import logging
from typing import Dict, Any, Optional

import aiohttp
import quart
from quart import Quart, request, Response
import quart_cors
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Quart app with CORS support
app = Quart(__name__)
app = quart_cors.cors(app, allow_origin="*")

# Configuration
SECRET_KEY = os.getenv("SECRET")
if not SECRET_KEY:
    logger.warning("No SECRET environment variable found. Set SECRET in .env file for security.")

@app.route('/', methods=['GET'])
async def index() -> Response:
    """Health check and project information endpoint."""
    return Response(
        response=json.dumps({
            "project": "alfred",
            "version": "1.0.0",
            "description": "A secure HTTP request proxy service",
            "author": "Mateusz Baranowski",
            "github": "https://github.com/6vz/alfred",
            "status": "running"
        }), 
        status=200, 
        content_type='application/json'
    )

@app.route('/req', methods=['POST'])
async def make_request() -> Response:
    """
    Process HTTP requests through the proxy.
    
    Expected JSON payload:
    {
        "secret": "your-secret-key",
        "method": "GET|POST|PUT|DELETE|PATCH",
        "url": "https://example.com/api",
        "headers": {"Header-Name": "Header-Value"},
        "body": {"key": "value"} or "raw string",
        "format_as": "text|json"
    }
    """
    try:
        data = await request.get_json()
        if not data:
            return _error_response("No JSON data provided", 400)
        
        # Validate secret
        if not SECRET_KEY:
            return _error_response("Server configuration error: SECRET not set", 500)
        
        if data.get("secret") != SECRET_KEY:
            logger.warning("Unauthorized request attempt")
            return _error_response("Invalid secret", 401)
        
        # Extract and validate request parameters
        method = data.get("method", "GET").upper()
        url = data.get("url")
        headers = data.get("headers", {})
        body = data.get("body")
        format_as = data.get("format_as", "text")
        
        if not url:
            return _error_response("URL is required", 400)
        
        if method not in ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"]:
            return _error_response(f"Unsupported HTTP method: {method}", 400)
        
        logger.info(f"Making {method} request to {url}")
        
        # Make the HTTP request
        response_data = await _make_http_request(method, url, headers, body, format_as)
        return Response(
            response=json.dumps(response_data),
            status=200,
            content_type='application/json'
        )
        
    except json.JSONDecodeError:
        return _error_response("Invalid JSON format", 400)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return _error_response("Internal server error", 500)

async def _make_http_request(method: str, url: str, headers: Dict[str, Any], 
                           body: Optional[Any], format_as: str) -> Dict[str, Any]:
    """Make HTTP request and return response data."""
    try:
        timeout = aiohttp.ClientTimeout(total=30)  # 30 second timeout
        
        async with aiohttp.ClientSession(timeout=timeout) as session:
            request_kwargs = {
                "method": method,
                "url": url,
                "headers": headers
            }
            
            # Handle request body
            if body and method in ["POST", "PUT", "PATCH"]:
                if isinstance(body, dict):
                    request_kwargs["json"] = body
                else:
                    request_kwargs["data"] = str(body)
            
            async with session.request(**request_kwargs) as response:
                response_text = await response.text()
                
                # Format response based on requested format
                response_body = response_text
                if format_as == "json":
                    try:
                        response_body = json.loads(response_text)
                    except json.JSONDecodeError:
                        logger.warning(f"Failed to parse response as JSON for {url}")
                        response_body = response_text
                
                return {
                    "status": response.status,
                    "headers": dict(response.headers),
                    "body": response_body,
                    "success": True
                }
                
    except aiohttp.ClientTimeout:
        raise Exception("Request timeout - the target server took too long to respond")
    except aiohttp.ClientError as e:
        raise Exception(f"HTTP client error: {str(e)}")
    except Exception as e:
        raise Exception(f"Request failed: {str(e)}")

def _error_response(message: str, status_code: int) -> Response:
    """Create standardized error response."""
    return Response(
        response=json.dumps({
            "error": message,
            "success": False
        }),
        status=status_code,
        content_type='application/json'
    )

@app.errorhandler(404)
async def not_found(error):
    """Handle 404 errors."""
    return _error_response("Endpoint not found", 404)

@app.errorhandler(500)
async def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {error}")
    return _error_response("Internal server error", 500)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    debug = os.getenv("DEBUG", "false").lower() == "true"
    
    logger.info(f"Starting Alfred server on {host}:{port}")
    app.run(host=host, port=port, debug=debug)
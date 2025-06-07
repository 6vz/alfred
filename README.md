# Alfred 🤖

**Alfred** is a secure HTTP request proxy service that allows you to make HTTP requests through a protected API endpoint. Perfect for scenarios where you need to proxy requests through a secure server or bypass CORS restrictions.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Quart](https://img.shields.io/badge/framework-Quart-orange.svg)](https://pgjones.gitlab.io/quart/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

## ✨ Features

- 🔐 **Secure**: Secret key authentication for all requests
- 🌐 **HTTP Methods**: Support for GET, POST, PUT, DELETE, PATCH, HEAD, and OPTIONS
- 📝 **Flexible Body**: Handle JSON objects or raw text data
- 🎯 **Format Control**: Response formatting as text or JSON
- ⚡ **Async**: Built with async/await for high performance
- 🛡️ **CORS Enabled**: Cross-origin requests supported
- 📊 **Logging**: Comprehensive request logging
- ⏱️ **Timeout Protection**: 30-second request timeout
- 🚦 **Error Handling**: Detailed error responses
- 🐳 **Docker Ready**: Easy deployment with Docker and Docker Compose

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

#### Option 1: Direct Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/6vz/alfred.git
   cd alfred
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   SECRET=your-super-secret-key-here
   PORT=8000
   HOST=0.0.0.0
   DEBUG=false
   ```

4. **Run the server**
   ```bash
   python main.py
   ```

#### Option 2: Docker Deployment

1. **Clone the repository**
   ```bash
   git clone https://github.com/6vz/alfred.git
   cd alfred
   ```

2. **Set up environment variables**
   Create a `.env` file:
   ```env
   SECRET=your-super-secret-key-here
   ```

3. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

   Or build and run manually:
   ```bash
   docker build -t alfred .
   docker run -p 8000:8000 --env-file .env alfred
   ```

The server will start on `http://localhost:8000` by default.

## 📋 API Reference

### Health Check

**GET** `/`

Returns server status and project information.

**Response:**
```json
{
  "project": "alfred",
  "version": "1.0.0",
  "description": "A secure HTTP request proxy service",
  "author": "Mateusz Baranowski",
  "github": "https://github.com/6vz/alfred",
  "status": "running"
}
```

### Make Request

**POST** `/req`

Process HTTP requests through the proxy.

**Request Body:**
```json
{
  "secret": "your-secret-key",
  "method": "GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS",
  "url": "https://api.example.com/endpoint",
  "headers": {
    "User-Agent": "Mozilla/5.0...",
    "Authorization": "Bearer token"
  },
  "body": {
    "key": "value"
  },
  "format_as": "json|text"
}
```

**Response:**
```json
{
  "status": 200,
  "headers": {
    "content-type": "application/json",
    "server": "nginx/1.18.0"
  },
  "body": {
    "data": "response content"
  },
  "success": true
}
```

## 💡 Usage Examples

### Example 1: Simple GET Request

```bash
curl -X POST http://localhost:8000/req \
  -H "Content-Type: application/json" \
  -d '{
    "secret": "your-secret-key",
    "method": "GET",
    "url": "https://api.ipify.org?format=json",
    "format_as": "json"
  }'
```

### Example 2: POST Request with JSON Body

```bash
curl -X POST http://localhost:8000/req \
  -H "Content-Type: application/json" \
  -d '{
    "secret": "your-secret-key",
    "method": "POST",
    "url": "https://httpbin.org/post",
    "headers": {
      "User-Agent": "Alfred/1.0.0"
    },
    "body": {
      "message": "Hello, World!",
      "timestamp": "2024-01-01T00:00:00Z"
    },
    "format_as": "json"
  }'
```

### Example 3: Using the Example JSON

The repository includes an `example.json` file that you can use as a template:

```bash
curl -X POST http://localhost:8000/req \
  -H "Content-Type: application/json" \
  -d @example.json
```

## ⚙️ Configuration

Alfred can be configured using environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `SECRET` | *required* | Secret key for authentication |
| `PORT` | `8000` | Port number for the server |
| `HOST` | `0.0.0.0` | Host address to bind to |
| `DEBUG` | `false` | Enable debug mode |

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/6vz/alfred.git
cd alfred

# Create .env file
echo "SECRET=your-secret-key-here" > .env

# Start the service
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the service
docker-compose down
```

### Using Docker Directly

```bash
# Build the image
docker build -t alfred .

# Run the container
docker run -d \
  --name alfred \
  -p 8000:8000 \
  -e SECRET=your-secret-key-here \
  alfred

# View logs
docker logs alfred

# Stop the container
docker stop alfred
```

## 🔒 Security

- **Authentication**: All requests require a valid secret key
- **HTTPS Support**: Use behind a reverse proxy with SSL/TLS
- **Request Timeout**: 30-second timeout prevents hanging requests
- **Input Validation**: Comprehensive validation of all inputs
- **Logging**: Security events are logged for monitoring
- **Docker Security**: Runs as non-root user in Docker

## 🛠️ Development

### Running in Development Mode

```bash
# Set debug mode
export DEBUG=true
python main.py
```

### Project Structure

```
alfred/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── example.json         # Example request payload
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
├── .env                # Environment variables (create this)
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
├── README.md           # This file
└── CONTRIBUTING.md     # Contribution guidelines
```

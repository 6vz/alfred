# Contributing to Alfred 🤖

First off, thank you for considering contributing to Alfred! It's people like you that make Alfred such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by common sense and mutual respect. By participating, you are expected to uphold this standard.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title** for the issue
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots or error logs if applicable**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and explain which behavior you expected to see instead**
* **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

## Development Process

### Setting Up Development Environment

1. Fork and clone the repository
   ```bash
   git clone https://github.com/your-username/alfred.git
   cd alfred
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create your `.env` file
   ```env
   SECRET=dev-secret-key
   DEBUG=true
   PORT=8000
   ```

5. Run the development server
   ```bash
   python main.py
   ```

### Code Style

* Follow PEP 8 Python code style
* Use type hints where appropriate
* Write descriptive docstrings for functions and classes
* Keep functions small and focused
* Use meaningful variable and function names

### Testing

Before submitting a pull request, please ensure:

* Your code passes all existing tests
* You've added tests for new functionality
* Manual testing has been performed
* The server starts without errors

### Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Example:
```
Add rate limiting functionality

- Implement sliding window rate limiter
- Add configuration options for rate limits
- Update documentation with rate limiting info

Fixes #42
```

## Project Structure

```
alfred/
├── main.py              # Main application entry point
├── requirements.txt     # Python dependencies
├── example.json        # Example request payload
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore patterns
├── README.md           # Project documentation
├── CONTRIBUTING.md     # This file
├── LICENSE             # MIT License
└── tests/              # Test files (if added)
```

## Feature Request Process

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with the "enhancement" label
3. **Describe the feature** in detail
4. **Explain the use case** and why it's valuable
5. **Wait for discussion** before starting implementation

## Release Process

Releases are handled by project maintainers:

1. Version bump in `main.py`
2. Update `CHANGELOG.md` (if exists)
3. Create a new GitHub release
4. Tag the release with version number

## Getting Help

* Check the [README.md](README.md) for basic usage
* Look through existing [GitHub Issues](https://github.com/6vz/alfred/issues)
* Create a new issue for questions or problems

## Recognition

Contributors will be recognized in the project documentation and release notes.

Thank you for contributing to Alfred! 🎉 
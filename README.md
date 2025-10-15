# agentic-ghc-demo-02

A FastAPI demo project for GitHub Copilot, showcasing modern Python development practices.

## Features

- ✨ Modern FastAPI application with async support
- 🧪 Comprehensive test suite using pytest
- 📝 Type hints and modern Python 3.9+ syntax
- 🎨 Code quality with Ruff linting and formatting
- 📚 Automatic API documentation with Swagger UI
- 🤖 GitHub Copilot integration guidelines

## Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mc5eamus/agentic-ghc-demo-02.git
cd agentic-ghc-demo-02
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

### Running Tests

Execute the test suite:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=app tests/
```

## Project Structure

```
agentic-ghc-demo-02/
├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI application
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Test fixtures
│   └── test_main.py         # Test cases
├── requirements.txt         # Project dependencies
├── pyproject.toml          # Project configuration
├── copilot.instructions.md # GitHub Copilot guidelines
└── copilot-setup-steps.yml # Setup instructions
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check endpoint
- `GET /api/v1/items/{item_id}` - Retrieve an item by ID
- `POST /api/v1/items` - Create a new item

## GitHub Copilot Integration

This project includes comprehensive GitHub Copilot integration:

- **copilot.instructions.md**: Detailed guidelines for code style, best practices, and modern Python patterns
- **copilot-setup-steps.yml**: Step-by-step setup instructions for developers

These files help GitHub Copilot provide context-aware suggestions that align with the project's standards.

## Development

### Code Quality

Check code with Ruff:
```bash
ruff check .
```

Auto-fix issues:
```bash
ruff check --fix .
```

Format code:
```bash
ruff format .
```

## Contributing

1. Follow the code style guidelines in `copilot.instructions.md`
2. Write tests for new features
3. Ensure all tests pass before submitting
4. Use type hints and docstrings

## License

MIT License

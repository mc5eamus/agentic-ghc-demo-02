# GitHub Copilot Instructions

This document provides guidelines and best practices for working with this FastAPI project using GitHub Copilot.

## Code Style and Standards

### General Python Guidelines

- **Python Version**: Use Python 3.9+ features and syntax
- **Type Hints**: Always use type hints for function parameters and return types
- **Docstrings**: Use Google-style docstrings for all public functions, classes, and modules
- **Line Length**: Maximum 100 characters per line
- **Import Organization**: Group imports in the following order:
  1. Standard library imports
  2. Third-party imports
  3. Local application imports

### Modern Python Patterns

- **Type Annotations**: Use modern union syntax (`str | None` instead of `Optional[str]`)
- **Async/Await**: Prefer async/await for I/O operations in FastAPI endpoints
- **F-strings**: Use f-strings for string formatting
- **Context Managers**: Use context managers for resource management
- **List/Dict Comprehensions**: Use comprehensions for simple transformations
- **Dataclasses/Pydantic**: Use Pydantic models for request/response validation

### FastAPI Best Practices

- **Dependency Injection**: Use FastAPI's dependency injection system for shared logic
- **Path Operations**: Define path operations with clear, RESTful endpoints
- **Response Models**: Always define response models using Pydantic
- **Status Codes**: Use appropriate HTTP status codes for responses
- **Error Handling**: Implement proper error handling with HTTPException
- **Documentation**: Leverage FastAPI's automatic API documentation (Swagger UI)

### Testing Standards

- **Test Framework**: Use pytest for all tests
- **Test Coverage**: Aim for >80% test coverage
- **Test Naming**: Use descriptive names starting with `test_`
- **Fixtures**: Use pytest fixtures for common test setup
- **Async Tests**: Use `pytest-asyncio` for async endpoint testing
- **Test Client**: Use FastAPI's TestClient for endpoint testing

### Code Quality Tools

- **Linter**: Use Ruff for linting and formatting
- **Type Checker**: Consider using mypy for static type checking
- **Pre-commit Hooks**: Set up pre-commit hooks for automated checks

### Security Practices

- **Environment Variables**: Store secrets in environment variables, never in code
- **Input Validation**: Use Pydantic models for request validation
- **CORS**: Configure CORS properly for frontend integration
- **Authentication**: Implement proper authentication and authorization
- **SQL Injection**: Use parameterized queries with ORMs

### Project Structure

```
agentic-ghc-demo-02/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── models.py        # Pydantic models
│   ├── routers/         # API routers
│   ├── services/        # Business logic
│   └── dependencies.py  # Shared dependencies
├── tests/
│   ├── __init__.py
│   ├── conftest.py      # Test fixtures
│   └── test_*.py        # Test modules
├── requirements.txt     # Project dependencies
├── pyproject.toml       # Project configuration
└── README.md            # Project documentation
```

## Copilot Usage Tips

### For Writing Code

- **Be Specific**: Provide clear context in comments before asking Copilot to generate code
- **Incremental Development**: Build features incrementally, using Copilot for each step
- **Review Suggestions**: Always review and understand Copilot's suggestions before accepting

### For Writing Tests

- **Test-First**: Write test descriptions first, then let Copilot help implement
- **Edge Cases**: Explicitly comment about edge cases you want to test
- **Assertions**: Be specific about expected outcomes in test descriptions

### For Refactoring

- **Single Responsibility**: Keep functions focused on a single task
- **DRY Principle**: Eliminate code duplication
- **Clear Intent**: Use descriptive variable and function names

## Common Patterns

### Creating a New Endpoint

```python
@app.get("/api/v1/resource/{resource_id}")
async def get_resource(resource_id: int) -> ResourceResponse:
    """
    Retrieve a resource by ID.
    
    Args:
        resource_id: The unique identifier of the resource
        
    Returns:
        The requested resource
        
    Raises:
        HTTPException: If resource not found (404)
    """
    # Implementation here
```

### Creating a Pydantic Model

```python
from pydantic import BaseModel, Field

class ResourceCreate(BaseModel):
    """Schema for creating a new resource."""
    
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
```

### Writing a Test

```python
def test_create_resource(client: TestClient) -> None:
    """Test creating a new resource returns 201."""
    payload = {"name": "Test", "description": "Test resource"}
    response = client.post("/api/v1/resources", json=payload)
    
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test"
```

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

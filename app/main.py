"""Main FastAPI application module."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="FastAPI Demo",
    description="A demo FastAPI application for GitHub Copilot",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to FastAPI Demo!"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/api/v1/items/{item_id}")
async def read_item(item_id: int, q: str | None = None) -> dict[str, int | str | None]:
    """
    Read an item by ID with optional query parameter.
    
    Args:
        item_id: The ID of the item to retrieve
        q: Optional query parameter
        
    Returns:
        Dictionary containing item information
    """
    return {"item_id": item_id, "q": q}


@app.post("/api/v1/items")
async def create_item(name: str, description: str | None = None) -> JSONResponse:
    """
    Create a new item.
    
    Args:
        name: Name of the item
        description: Optional description of the item
        
    Returns:
        JSON response with created item details
    """
    item = {"name": name, "description": description, "id": 1}
    return JSONResponse(content=item, status_code=201)

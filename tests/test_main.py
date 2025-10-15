"""Tests for the main FastAPI application."""

from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient) -> None:
    """Test the root endpoint returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI Demo!"}


def test_health_check(client: TestClient) -> None:
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_read_item(client: TestClient) -> None:
    """Test reading an item by ID."""
    response = client.get("/api/v1/items/42")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 42
    assert data["q"] is None


def test_read_item_with_query(client: TestClient) -> None:
    """Test reading an item with query parameter."""
    response = client.get("/api/v1/items/42?q=test")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 42
    assert data["q"] == "test"


def test_create_item(client: TestClient) -> None:
    """Test creating a new item."""
    response = client.post("/api/v1/items?name=TestItem&description=TestDesc")
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "TestItem"
    assert data["description"] == "TestDesc"
    assert "id" in data

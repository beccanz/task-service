import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_create_task(client: AsyncClient):
    payload = {
        "title": "Test task",
        "description": "Test description",
    }

    response = await client.post("/tasks", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["status"] == "PENDING"
    assert "id" in data


@pytest.mark.asyncio
async def test_create_task_validation_failure(client: AsyncClient):
    payload = {
        "title": "",  # invalid: min_length=1
    }

    response = await client.post("/tasks", json=payload)

    assert response.status_code == 422

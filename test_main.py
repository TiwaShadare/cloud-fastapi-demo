from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Cloud Task API is running"
    }


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_get_tasks():

    response = client.get("/tasks")

    assert response.status_code == 200

    assert len(response.json()) >= 2


def test_get_first_task():

    response = client.get("/tasks/1")

    assert response.status_code == 200

    assert response.json()["id"] == 1

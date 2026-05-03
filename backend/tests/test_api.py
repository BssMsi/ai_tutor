import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "1.0.0"}

def test_get_onboarding_state():
    response = client.get("/api/v1/onboarding/user123")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "user123"
    assert data["status"] == "not_started"

def test_create_plan():
    response = client.post("/api/v1/plans/", json={
        "user_id": "user123",
        "name": "Bar Exam Prep",
        "status": "active"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bar Exam Prep"
    assert data["status"] == "active"

def test_chat_stream_mock():
    response = client.post("/api/v1/chat/stream", json={
        "user_id": "user123",
        "plan_id": "plan123",
        "messages": [{"role": "user", "content": "hello"}]
    })
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/event-stream; charset=utf-8"

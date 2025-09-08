from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_aula():
    response = client.post("/aulas/", json={
        "nome": "Boxe",
        "horario": "2025-09-10T19:00:00",
        "limite_vagas": 20
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Boxe"
    assert "id" in data

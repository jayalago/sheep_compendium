# Import TestClient to simulate API requests
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

#Testing adding sheep
def test_add_sheep():
    new_sheep = {
        "id": 7,
        "name": "Sully",
        "breed": "Suffolk",
        "sex": "ewe"
    }
    response = client.post("/sheep", json=new_sheep)

    assert response.status_code == 201

    assert response.json() == new_sheep

    get_response = client.get(f"/sheep/{new_sheep['id']}")

    assert get_response.status_code == 200

    assert get_response.json() == new_sheep



from fastapi.testclient import TestClient
from project_1_fastapi_helloworld.main import app

def test_root_path():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
    
def test_piaic_path():
    client = TestClient(app=app)
    response = client.get("/piaic/")
    assert response.status_code == 200
    assert response.json() == {"organization": "Welcome to PIAIC!"}
    
def test_third_check():
    client = TestClient(app=app)
    response = client.get("/piaic/")
    assert response.status_code == 200
    assert response.json() == {"organization": "ABC"}
from api import app
from fastapi.testclient import TestClient

from core.models import ContactModel

client = TestClient(app)

def test_api_access():
    
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_api_add_contact():
    
    add_test_data = {
        "name": "MyTest",
        "gender": "female",
        "age": 33,
        "email": "mt@i.com"
    }

    response = client.post(
        "/add_contact", 
        json = add_test_data 
    )

    assert response.status_code == 200
    assert response.json()["message"] == "successful"

def test_api_read_contact():
    
    response = client.get("/contacts/MyTest")
    assert response.status_code == 200
    assert response.json()["email"] == "mt@i.com"

def test_api_update_contact():
    upd_test_data = {
        "name": "MyTest1",
        "gender": "male",
        "age": 44,
        "email": "mt1@i.com"
    }
    
    response = client.put(
        "/contacts/MyTest",
        json = upd_test_data
    )
        
    assert response.status_code == 200
    assert response.json()["message"] == "successful"

def test_api_delete_contact():
    
    response = client.delete("/contacts/MyTest1")
    assert response.status_code == 200
    assert response.json()["message"] == "successful"
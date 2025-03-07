from chalice.test import Client
from app import app
import json


def test_create_offline():
    with Client(app) as client:
        response = client.http.post(
            "/sales/offline",
            body = json.dumps({"id":"1", "consumer":"usuário um", "value":"12,50", "food":"pizza"}),
            headers ={"Content-Type":"application/json"}
            )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_update_offline():
    with Client(app) as client:
        response = client.http.put(
            "/sales/offline",
            body = json.dumps({"id":"1", "consumer":"usuário um", "value":"12,50", "food":"pizza"}),
            headers = {"Content-Type": "application/json"}
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_delete_offline():
    with Client(app) as client:
        response = client.http.delete(
            "/sales/offline",
            body = json.dumps({"id":"1", "consumer":"usuário um", "value":"12,50", "food":"pizza"}),
            headers = {"Content-Type": "application/json"}
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_get__offlines():
    with Client(app) as client:
        response = client.http.get("/sales/offlines")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200
    
def test_get__offline():
    with Client(app) as client:
        response = client.http.get("/sales/offline/1")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


# API Online

def test_create_online():
    with Client(app) as client:
        response = client.http.post(
            "/sales/online",
            body = json.dumps({"id":"1", "consumer":"usuário um", "value":"12,50", "food":"pizza"}),
            headers ={"Content-Type":"application/json"}
            )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_update_online():
    with Client(app) as client:
        response = client.http.put(
            "/sales/online",
            body = json.dumps({"id":"1", "consumer":"usuário um", "value":"12,50", "food":"pizza"}),
            headers = {"Content-Type": "application/json"}
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_delete_online():
    with Client(app) as client:
        response = client.http.delete(
            "/sales/online",
            body = json.dumps({"id":"1", "consumer":"usuário um", "value":"12,50", "food":"pizza"}),
            headers = {"Content-Type": "application/json"}
        )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200

def test_get__onlines():
    with Client(app) as client:
        response = client.http.get("/sales/online")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200
    
def test_get__online():
    with Client(app) as client:
        response = client.http.get("/sales/online/1")
        print(response.json_body)
        assert response.json_body["statusCode"] == 200
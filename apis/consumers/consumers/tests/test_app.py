from chalice.test import Client
from app import app
import json


def test_create_person():
    with Client(app) as client:
        response = client.http.post(
            '/consumers/person',
            body=json.dumps({"name":"usuario1", "phone":"111111111"}),
            headers={"Content-Type":"application/json"}
        )
        print(f"\n Response: {response.json_body}")
        assert response.json_body["statusCode"] == 200


def test_update_person():
    with Client(app) as client:
        response = client.http.put(
            '/consumers/person',
            body=json.dumps({"name":"usuario1", "phone":"111111111"}),
            headers={"Content-Type":"application/json"}
        )
        print(f"Response: {response.json_body}")
        assert response.json_body["statusCode"] == 200

def test_delete_person():
    with Client(app) as client:
        response = client.http.delete(
            '/consumers/person',
            body=json.dumps({"name":"usuario1", "phone":"111111111"}),
            headers= {"Content-Type":"application/json"}
        )
        print(f"Response: {response.json_body}")
        assert response.json_body["statusCode"] == 200

def test_get_persons():
    with Client(app) as client:
        response = client.http.get('/consumers/persons')
        print(f"Response: {response.json_body}")
        assert response.json_body["statusCode"] == 200

def test_get_person():
    with Client(app) as client:
        response = client.http.get('/consumers/person/1')
        print(f"Response: {response.json_body}")
        assert response.json_body["statusCode"] == 200



def test_create_company():
    with Client(app) as client:
        response = client.http.post(
            '/consumers/company',
            body=json.dumps({"name":"empresa1", "telefone":"111111111"}),
            headers={"Content-Type":"application/json"}
        )
        print(f"\n Response: {response.json_body}")
        assert response.json_body["statusCode"] == 200


def test_update_company():
    with Client(app) as client:
        response = client.http.put(
            '/consumers/company',
            body=json.dumps({"name":"empresa1", "telefone":"111111111"}),
            headers={"Content-Type":"application/json"}
        )
        print(f"Response: {response.json_body}")
        assert response.json_body["statusCode"] == 200

def test_delete_company():
    with Client(app) as client:
        response = client.http.delete(
            '/consumers/company',
            body=json.dumps({"name":"empresa1", "telefone":"111111111"}),
            headers= {"Content-Type":"application/json"}
        )
        print(f"Response: {response.json_body}")
        assert response.json_body["statusCode"] == 200

def test_get_companies():
    with Client(app) as client:
        response = client.http.get('/consumers/companies')
        print(f"Response: {response.json_body}")
        assert response.json_body["statusCode"] == 200

def test_get_company():
    with Client(app) as client:
        response = client.http.get('/consumers/company/1')
        print(f"Response: {response.json_body}")
        assert response.json_body["statusCode"] == 200
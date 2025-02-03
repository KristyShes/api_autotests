import pytest
import requests

@pytest.fixture()
def petId():
    payload = {
        "id": 0,
        "category": {
            "id": 5,
            "name": "cats"
        },
        "name": "cat_my_cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    responce = requests.post(f'https://petstore.swagger.io/v2/pet', json=payload).json()
    yield responce['id']
    requests.delete(f'https://petstore.swagger.io/v2/pet/{responce["id"]}')



def test_create_new_pet():
    payload = {
        "id": 0,
        "category": {
            "id": 5,
            "name": "cats"
        },
        "name": "cat_my_cat",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    responce = requests.post(f'https://petstore.swagger.io/v2/pet', json=payload).json()
    assert responce['name'] == payload['name']

def test_get_new_pet(petId):
    print(petId)
    responce = requests.get(f'https://petstore.swagger.io/v2/pet/{petId}').json()
    assert responce['id'] == petId

def test_get_pets_status():
    query = {"status": "available"}
    responce = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus', params=query).json()

def test_update_pet(petId):
    payload = {
        "id": 0,
        "category": {
            "id": 5,
            "name": "cats"
        },
        "name": "cat_Doggy",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.put(f'https://petstore.swagger.io/v2/pet', json=payload).json()

def test_delete_pet(petId):
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{petId}')
    assert response.status_code == 200
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{petId}')
    assert response.status_code == 404





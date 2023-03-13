import os

from dotenv import load_dotenv
from pytest_voluptuous import S

from schemas.user import created_user, updated_user, registered_user

load_dotenv()

LOGIN = os.getenv("REQRES_LOGIN")
PASSWORD = os.getenv("REQRES_PASSWORD")
API_URL = os.getenv("REQRES_API_URL")


def test_single_user_not_found(reqres):
    response = reqres.get('/users/23')

    assert response.status_code == 404


def test_create_new_user(reqres):
    response = reqres.post(
        '/users',
        {
            "name": "vladislav",
            "job": "mcdonalds"
        }
    )
    name = response.json()['name']
    job = response.json()['job']

    assert name == 'vladislav'
    assert job == 'mcdonalds'
    assert response.status_code == 201
    assert S(created_user) == response.json()


def test_update_user_job(reqres):
    response = reqres.put(
        '/users/9',
        {
            "name": "morpheus",
            "job": "zion resident"
        }
    )
    name = response.json()['name']
    job = response.json()['job']

    assert name == 'morpheus'
    assert job == 'zion resident'
    assert response.status_code == 200
    assert S(updated_user) == response.json()


def test_delete_user(reqres):
    response = reqres.delete('/users/2')

    assert response.status_code == 204
    assert len(response.content) == 0


def test_register_new_user_successful(reqres):
    response = reqres.post(
        '/register',
        {
            "email": LOGIN,
            "password": PASSWORD
        }
    )
    user_id = response.json()['id']
    result = reqres.get(f'/users/{user_id}')
    email = result.json()['data']['email']

    assert response.status_code == 200
    assert result.status_code == 200
    assert S(registered_user) == response.json()
    assert email == LOGIN

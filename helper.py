from faker import Faker
import requests
from data import URLs


def create_random_creds():
    fake = Faker()
    email = fake.free_email()
    name = email.split('@')[0]
    password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    payload = {
        "email": email,
        "password": password,
        "name": name,
    }
    return payload


def auth_user_and_get_creds():
    payload = create_random_creds()
    response = requests.post(f'{URLs.BASE_URL}{URLs.CREATE_USER_URL}', json=payload)
    return payload, response


def get_access_token(response):
    return response.json().get('accessToken')

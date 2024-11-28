import pytest
import allure
from helper import *


@pytest.fixture
@allure.title('Создание пользователя и удаление пользователя при выполнении теста')
def create_and_delete_user():
    payload, response = auth_user_and_get_creds()
    yield payload, response
    access_token = response.json().get('accessToken')
    requests.delete(f'{URLs.BASE_URL}{URLs.DELETE_USER_URL}', headers={'Authorization': access_token})

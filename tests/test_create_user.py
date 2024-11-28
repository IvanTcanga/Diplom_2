import pytest
import allure
from methods.user_methods import UserMethods
from data import InvalidCreds


class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя')
    @allure.description('Создаем уникального user с Faker и удаляем его по токену после теста'
                        'В ответе проверяются код и тело')
    def test_create_new_user_success(self, create_and_delete_user):
        payload, response = create_and_delete_user
        deserials = response.json()
        assert response.status_code == 200 and response.json().get('success') is True
        assert 'accessToken' in deserials and deserials['accessToken'] != ''
        assert 'refreshToken' in deserials and deserials['refreshToken'] != ''
        assert deserials['user']['email'] == payload['email']
        assert deserials['user']['name'] == payload['name']

    @allure.title('Проверка создания  пользователя, который уже зарегистрирован')
    @allure.description('Попытка создать уже зарегистрированного user, проверяем код 403 и тело')
    def test_create_already_exist_user(self, create_and_delete_user):
        payload, _ = create_and_delete_user
        user_methods = UserMethods()
        r = user_methods.post_create_user(payload)
        deserials = r.json()
        assert r.status_code == 403
        assert deserials['success'] is False and deserials['message'] == 'User already exists'

    @allure.title('Проверка ответа на запрос, при попытке пользователя не заполнив одно из обязательных полей')
    @allure.description('Отправляем запросы с незаполненными полями email, pass, name')
    @pytest.mark.parametrize('creds', InvalidCreds.creds_with_empty_field)
    def test_registration_one_required_field_is_empty_failed_submit(self, creds):
        user_methods = UserMethods()
        r = user_methods.post_create_user(creds)
        assert r.status_code == 403
        assert r.json() == {'success': False, 'message': 'Email, password and name are required fields'}

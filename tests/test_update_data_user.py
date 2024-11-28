from helper import create_random_creds
import allure
from methods.user_methods import UserMethods


class TestUpdateDataUser:
    @allure.title('Проверка изменения данных пользователя c авторизацией')
    @allure.description('Проверка, что любое поле можно изменить, проверем код и тело ответа')
    def test_update_data_auth_user_success(self, create_and_delete_user):
        _, response = create_and_delete_user
        new_payload = create_random_creds()
        response = UserMethods().patch_new_payload_auth_user(new_payload, response)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert deserials['user']['email'] == new_payload['email']
        assert deserials['user']['name'] == new_payload['name']

    @allure.title('Проверка изменения данных пользователя без авторизацией')
    @allure.description('Для неавторизованного пользователя система вернёт ошибку')
    def test_update_data_user_unauth_error(self):
        new_payload = create_random_creds()
        response = UserMethods().patch_new_payload_unauth_user(new_payload)
        assert response.status_code == 401 and response.json() == {'success': False,
                                                                   'message': 'You should be authorised'}

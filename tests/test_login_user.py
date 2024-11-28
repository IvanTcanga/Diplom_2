import allure
from methods.user_methods import UserMethods


class TestLoginUser:
	@allure.title('Проверка логин под существующим пользователем')
	@allure.description('Проверяются код и тело')
	def test_login_user_success(self, create_and_delete_user):
		payload, _ = create_and_delete_user
		response = UserMethods().post_login_user(payload)
		deserials = response.json()
		assert response.status_code == 200 and deserials['success'] is True
		assert deserials['accessToken'] != '' and deserials['refreshToken'] != ''
		assert deserials['user']['email'] == payload['email']
		assert deserials['user']['name'] == payload['name']

	@allure.title('Проверка аутентификации с неверным email')
	@allure.description('Проверяются код и тело')
	def test_auth_invalid_email_error(self, create_and_delete_user):
		payload, _ = create_and_delete_user
		response = UserMethods().post_login_user_invalid_email(payload)
		assert response.status_code == 401 and response.json() == {"success": False,
																   "message": "email or password are incorrect"}

	@allure.title('Проверка аутентификации с неверным password')
	@allure.description('Проверяются код и тело')
	def test_auth_invalid_password_error(self, create_and_delete_user):
		payload, _ = create_and_delete_user
		response = UserMethods().post_login_user_invalid_password(payload)
		assert response.status_code == 401 and response.json() == {"success": False,
																   "message": "email or password are incorrect"}

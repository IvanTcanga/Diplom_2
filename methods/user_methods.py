import allure
from data import *
from helper import *


class UserMethods:
	@allure.step('Create user')
	def post_create_user(self, payload):
		creds = payload
		return requests.post(f'{URLs.BASE_URL}{URLs.CREATE_USER_URL}', json=creds)

	@allure.step('login user')
	def post_login_user(self, payload):
		login_payload = {
			"email": payload["email"],
			"password": payload["password"],
		}
		return requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_USER_URL}', json=login_payload)

	@allure.step("Вход  c неправильным паролем")
	def post_login_user_invalid_password(self, payload):
		login_payload = {
			'email': payload["email"],
			'password': UserData.password
		}
		response = requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_USER_URL}', json=login_payload)
		return response

	@allure.step("Вход с неправильным email")
	def post_login_user_invalid_email(self, payload):
		login_payload = {
			'email': UserData.email,
			'password': payload["password"]
		}
		response = requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_USER_URL}', json=login_payload)
		return response

	@allure.step("Получение access_token и обновление данных авторизованного пользователя ")
	def patch_new_payload_auth_user(self, new_payload, response_fixture):
		access_token = get_access_token(response_fixture)
		headers = {
			'Authorization': f'{access_token}',
			'Content-Type': 'application/json'
		}
		response = requests.patch(
			f'{URLs.BASE_URL}{URLs.UPDATE_USER_URL}',
			headers=headers,
			json=new_payload
		)
		return response

	@allure.step("Получение ответа при попытке обновиления данных неавторизованного пользователя ")
	def patch_new_payload_unauth_user(self, new_payload):
		headers = {
			'Content-Type': 'application/json'
		}
		response = requests.patch(
			f'{URLs.BASE_URL}{URLs.UPDATE_USER_URL}',
			headers=headers,
			json=new_payload
		)
		return response

import allure
from helper import *
from data import *


class OrderMethods:
	@allure.step("Получение заказа аутентифицированного пользователя")
	def get_user_order_auth_user(self, response_fixture):
		access_token = get_access_token(response_fixture)
		headers = {
			'Authorization': f'{access_token}'
		}
		return requests.get(f'{URLs.BASE_URL}{URLs.GET_USER_ORDERS_URL}', headers=headers)

	@allure.step("Получение заказа неаутентифицированного пользователя")
	def get_user_order_unauth_user(self):
		headers = {
			'Content-Type': 'application/json'
		}
		return requests.get(f'{URLs.BASE_URL}{URLs.GET_USER_ORDERS_URL}', headers=headers)

	@allure.step('Создаем заказ аутентифицированным пользователем с ингридиентами')
	def post_create_order(self, response_fixture):
		payload = {'ingredients': IngredientData.ingredients}
		access_token = get_access_token(response_fixture)
		headers = {
			'Authorization': f'{access_token}'
		}
		return requests.post(f'{URLs.BASE_URL}{URLs.CREATE_ORDER_URL}', json=payload, headers=headers)

	@allure.step('Создаем заказ неаутентифицированным пользователем с ингридиентами')
	def post_create_unauth_user_order(self):
		payload = {'ingredients': IngredientData.ingredients}
		headers = {
			'Content-Type': 'application/json'
		}
		return requests.post(f'{URLs.BASE_URL}{URLs.CREATE_ORDER_URL}', json=payload, headers=headers)

	@allure.step('Создаем заказ аутентифицированным пользователем не передав ингридиенты')
	def post_create_order_without_ingredients(self, response_fixture):
		payload = {'ingredients': []}
		access_token = get_access_token(response_fixture)
		headers = {
			'Authorization': f'{access_token}'
		}
		return requests.post(f'{URLs.BASE_URL}{URLs.CREATE_ORDER_URL}', json=payload, headers=headers)

	@allure.step('Создаем заказ аутентифицированным пользователем с невалидными ингридиентами')
	def post_create_order_invalid_ingredients(self, response_fixture):
		payload = {'ingredients': IngredientData.INVALID_HASH_INGREDIENT}
		access_token = get_access_token(response_fixture)
		headers = {
			'Authorization': f'{access_token}'
		}
		return requests.post(f'{URLs.BASE_URL}{URLs.CREATE_ORDER_URL}', json=payload, headers=headers)

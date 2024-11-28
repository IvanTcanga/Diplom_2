import allure
from methods.order_methods import OrderMethods


class TestCreateOrder:
    @allure.title('Проверка создания заказа с ингредиентами аутентифицированного пользователя')
    def test_create_order_auth_user_success(self, create_and_delete_user):
        payload, response_fixture = create_and_delete_user
        response = OrderMethods().post_create_order(response_fixture)
        deserials = response.json()
        assert response.status_code == 200 and deserials['success'] is True
        assert 'name' in deserials.keys() and 'number' in deserials['order'].keys()

    @allure.title('Проверка создания заказа с ингредиентами неаутентифицированного пользователя')
    def test_create_order_unauth_user_success(self):
        response = OrderMethods().post_create_unauth_user_order()
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Проверка создания заказа с неуказанными ингредиентами аутентифицированным пользователя')
    @allure.description('Хэш ингредиента в запросе не передается')
    def test_create_order_without_ingredients_auth_user_error(self, create_and_delete_user):
        _, response_fixture = create_and_delete_user
        response = OrderMethods().post_create_order_without_ingredients(response_fixture)
        assert response.status_code == 400 and response.json() == {'success': False,
                                                                   'message': 'Ingredient ids must be provided'}

    @allure.title('Проверка создания заказа с невалидным хэшем ингредиента и аутентифицированным юзером')
    @allure.description('В запрос передается хэш несуществующего ингредиента')
    def test_create_order_invalid_ingredients_auth_user_error(self, create_and_delete_user):
        _, response_fixture = create_and_delete_user
        response = OrderMethods().post_create_order_invalid_ingredients(response_fixture)
        assert response.status_code == 400 and response.json() == {"success": False, "message": "One or more ids provided are incorrect"}
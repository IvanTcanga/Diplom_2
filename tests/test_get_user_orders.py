import allure
from methods.order_methods import OrderMethods


class TestGetUserOrders:
    @allure.title('Проверка получения заказов для аутентифицированного пользователя')
    def test_get_orders_auth_user_success(self, create_and_delete_user):
        payload, response_fixture = create_and_delete_user
        OrderMethods().post_create_order(response_fixture)
        response = OrderMethods().get_user_order_auth_user(response_fixture)
        deserials = response.json()
        assert response.status_code == 200 and deserials['success'] is True
        assert 'orders' in deserials.keys() and 'total' in deserials.keys()

    @allure.title('Проверка получение заказов неаутентифицированного пользователя')
    def test_get_orders_unauthenticated_user_success(self):
        response = OrderMethods().get_user_order_unauth_user()
        assert response.status_code == 401 and response.json() == {'success': False,
                                                                   'message': 'You should be authorised'}

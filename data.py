class URLs:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    CREATE_USER_URL = '/auth/register'
    LOGIN_USER_URL = '/auth/login'
    UPDATE_USER_URL = '/auth/user'
    DELETE_USER_URL = '/auth/user'
    CREATE_ORDER_URL = '/orders'
    GET_USER_ORDERS_URL = '/orders'


class InvalidCreds:
    creds_with_empty_field = [
        {'email': '',
         'password': '12345678',
         'name': 'Ivan'
         },
        {'email': 'ivan@gmail.com',
         'password': '',
         'name': 'Ivan'
         },
        {'email': 'ivan@gmail.com',
         'password': '12345678',
         'name': ''
         }
    ]


class UserData:
    email = "tcanga@yandex.ru"
    password = "WRONG_PASSWORD"
    name = "Ivan"


class IngredientData:
    INVALID_HASH_INGREDIENT = "60d3b41abdacab0026a733c6"
    ingredients = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c', '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79']

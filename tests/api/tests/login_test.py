import pytest
import requests

from tests.common.common import BASE_URL
from tests.api.common.api_endpoints import LOGIN


class TestLogin:
    @pytest.mark.parametrize('email, password', [('eve.holt@reqres.in', 'cityslicka')])
    def test_login_successful(self, email, password):
        creds = {
            'email': email,
            'password': password
        }
        response = requests.post(BASE_URL + LOGIN, json=creds)

        assert response.status_code == 200, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert response.json()['token'] is not None, 'Значение ключа "token" в ответе отсутствует'

    @pytest.mark.parametrize('email, error_description', [('peter@klaven', 'Missing password')])
    def test_login_unsuccessful(self, email, error_description):
        creds = {
            'email': email
        }
        response = requests.post(BASE_URL + LOGIN, json=creds)

        assert response.status_code == 400, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert response.json()['error'] == error_description, 'Описание ошибки не соответствует ожидаемому'

    @pytest.mark.parametrize('email, password, error_description', [
        (None, 123, 'Missing email or username'),
        ('peter@klaven', None, 'Missing password'),
        ('eve.holt@reqres.in', 123, 'Invalid username or password')
    ])
    def test_login_negative(self, email, password, error_description):
        creds = {
            'email': email,
            'password': password
        }
        response = requests.post(BASE_URL + LOGIN, json=creds)

        assert response.status_code == 400, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert response.json()['error'] == error_description, 'Описание ошибки не соответствует ожидаемому'

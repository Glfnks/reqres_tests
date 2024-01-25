import pytest
import requests

from tests.common.common import BASE_URL
from tests.api.common.api_endpoints import REGISTER


class TestRegister:

    @pytest.mark.parametrize('email, password', [('eve.holt@reqres.in', 'pistol')])
    def test_register_successful(self, email, password):
        creds = {
            'email': email,
            'password': password
        }
        response = requests.post(BASE_URL + REGISTER, json=creds)

        assert response.status_code == 200, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert response.json()['token'] is not None, 'Значение ключа "token" в ответе пустое'
        assert isinstance(response.json()['id'], int)

    @pytest.mark.parametrize('email, password, error_description', [
        ('sydney@fife', None, 'Missing password'),
        (None, 'pistol', 'Missing email or username'),
        (None, None, 'Missing email or username'),
        ('invalid_email', 'password123', 'Note: Only defined users succeed registration')
    ])
    def test_register_unsuccessful(self, email, password, error_description):
        creds = {
            'email': email,
            'password': password
        }
        response = requests.post(BASE_URL + REGISTER, json=creds)

        assert response.status_code == 400, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert response.json()['error'] == error_description, 'Описание ошибки не соответствует ожидаемому'

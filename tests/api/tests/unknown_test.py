import pytest
import requests

from tests.api.common.api_endpoints import UNKNOWN
from tests.common.common import BASE_URL


class TestUnknown:

    def test_list_resource(self):
        response = requests.get(BASE_URL + UNKNOWN)

        assert response.status_code == 200, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert isinstance(response.json()['page'], int)
        assert isinstance(response.json()['per_page'], int)
        assert isinstance(response.json()['total'], int)
        assert isinstance(response.json()['total_pages'], int)
        assert isinstance(response.json()['data'], list)

    def test_single_resource(self):
        response = requests.get(BASE_URL + UNKNOWN + '/2')

        assert response.status_code == 200, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert response.json()

    @pytest.mark.parametrize('num', [-5, -1, '@&*', None, 23])
    def test_single_resource_negative(self, num):
        response = requests.get(BASE_URL + UNKNOWN + f'/{num}')

        assert response.status_code == 404, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'

    def test_invalid_method(self):
        response = requests.post(BASE_URL + UNKNOWN + '/2')

        assert response.status_code == 405, f"Получен статус код {response.status_code}"

    def test_single_resource_not_found(self):
        response = requests.get(BASE_URL + UNKNOWN + '/23')

        assert response.status_code == 404, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'

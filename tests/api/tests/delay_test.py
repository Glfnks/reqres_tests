import time
import pytest
import requests

from tests.common.common import BASE_URL
from tests.api.common.api_endpoints import DELAY


class TestDelay:

    @pytest.mark.parametrize('delay', [1, 3, -1, -5, 0])
    def test_delay(self, delay):
        expected_delay = delay
        if delay < 0:
            expected_delay = 0

        start_time = time.time()
        response = requests.get(BASE_URL + DELAY + f'={delay}')
        actual_delay = time.time() - start_time

        assert actual_delay < expected_delay + 1, f'Запрос выполнился долго: {actual_delay} секунд'
        assert response.status_code == 200, f'Получен статус код {response.status_code}'
        assert response.headers, 'Заголовки в ответе отсутствуют'

    @pytest.mark.parametrize('delay', ['one', '!@#$'])
    def test_delay_negative(self, delay):
        response = requests.get(BASE_URL + DELAY + f'={delay}')

        assert response.status_code == 400, f'Получен статус код {response.status_code}'
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert not response.json()

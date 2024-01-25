import pytest
import requests

from tests.api.common.api_endpoints import USERS
from tests.common.common import BASE_URL


class TestUsers:

    def test_list_users(self):
        response = requests.get(BASE_URL + USERS + '?page=2')

        assert response.status_code == 200, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert isinstance(response.json()['page'], int)
        assert isinstance(response.json()['per_page'], int)
        assert isinstance(response.json()['total'], int)
        assert isinstance(response.json()['total_pages'], int)
        assert isinstance(response.json()['data'], list)

    @pytest.mark.parametrize('page_num', [-5, -1, '@&*', None])
    def test_list_users_negative(self, page_num):
        response = requests.get(BASE_URL + USERS + f'?page={str(page_num)}')

        assert response.status_code == 200, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert isinstance(response.json()['page'], int)
        assert isinstance(response.json()['per_page'], int)
        assert isinstance(response.json()['total'], int)
        assert isinstance(response.json()['total_pages'], int)
        assert isinstance(response.json()['data'], list)

    def test_list_users_fail_endpoint(self):
        response = requests.get(BASE_URL + '/fail_endpoint')

        assert response.status_code == 404, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'

    def test_header_narrowing(self):
        headers = {"Content-Type": "text/"}
        response = requests.get(BASE_URL + USERS + '?page=2', headers=headers)

        assert response.status_code == 200, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'

    def test_single_user(self):
        response = requests.get(BASE_URL + USERS + '/2')

        assert response.status_code == 200, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert response.json()

    @pytest.mark.parametrize('user_num', [-5, -1, 0, '@&*', None, 23])
    def test_single_user_not_found(self, user_num):
        response = requests.get(BASE_URL + USERS + f'/{str(user_num)}')

        assert response.status_code == 404, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'

    @pytest.mark.parametrize('name, job', [('morpheus', 'leader')])
    def test_create(self, name, job):
        data = {
            'name': name,
            'job': job
        }
        response = requests.post(BASE_URL + USERS, json=data)

        assert response.status_code == 201, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'

        json_response = response.json()
        assert name == json_response['name'], 'Значение ключа "name" в ответе неверно'
        assert job == json_response['job'], 'Значение ключа "job" в ответе неверно'

    @pytest.mark.parametrize('name, job, expected_status_code', [
        (None, 'leader', 400),
        ('morpheus', None, 400),
        ('morpheus', 'leader', 409)
    ])
    def test_create_negative(self, name, job, expected_status_code):
        user_data = {
            'name': name,
            'job': job
        }
        response = requests.post(BASE_URL + USERS, json=user_data)

        assert response.status_code == expected_status_code, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        """
        Намеренно пропущена проверка наиболее вероятных сообщений при 400 и 409 ответах,
        так как неизвестно, как фактически может быть настроен контроллер
        """

    @pytest.mark.parametrize('name, job', [('morpheus', 'leader')])
    def test_update_put(self, name, job):
        user_data = {
            'name': name,
            'job': job
        }
        response = requests.put(BASE_URL + USERS + '/2', json=user_data)

        assert response.status_code == 200, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'

    @pytest.mark.parametrize('name, job', [
        ('morpheus', 'zion resident'),
        (None, None),
        ('invalid_name', 'job123'),
    ])
    def test_update_patch(self, name, job):
        user_data = {
            'name': name,
            'job': job
        }
        response = requests.patch(BASE_URL + USERS + '/2', json=user_data)

        assert response.status_code == 400, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert isinstance(response.json()['updatedAt'], str)

    @pytest.mark.parametrize('name, job', [('failed_name', 'zion resident')])
    def test_update_patch_failed(self, name, job):
        user_data = {
            'name': name,
            'job': job
        }
        response = requests.patch(BASE_URL + USERS + '/2', json=user_data)

        assert response.status_code == 200, f"Получен статус код {response.status_code}"
        assert response.headers, 'Заголовки в ответе отсутствуют'
        assert isinstance(response.json()['updatedAt'], str)

    def test_delete(self):
        response = requests.patch(BASE_URL + USERS + '/2')

        assert response.status_code == 204, f"Получен статус код {response.status_code}"

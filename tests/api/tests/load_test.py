import httpx
import pytest
import asyncio
import requests
from tests.common.common import env
from tests.common.common import BASE_URL

num_requests = int(env.get('NUM_REQUESTS'))


class TestLoad:
    def test_server_load(self):
        for _ in range(num_requests):
            response = requests.get(BASE_URL)
            assert response.status_code == 200
            assert response.headers

    @pytest.mark.asyncio
    async def test_server_load_async(self):
        async with httpx.AsyncClient() as client:
            tasks = []
            for _ in range(num_requests):
                task = client.get(BASE_URL)
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            for response in responses:
                assert response.status_code == 200
                assert response.headers

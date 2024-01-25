import json
import time
import brotli
from tests.conftest import driver

DEFAULT_UI_TIMEOUT = 1
HALF_OF_DEFAULT_UI_TIMEOUT = 1/2


def get_response_body(url):
    """
    Возвращает тело ответа сервера в json формате
    :param url: url
    :return: Тело ответа в json
    """
    # Ожидание формирования запросов
    time.sleep(HALF_OF_DEFAULT_UI_TIMEOUT)

    start_time = time.time()
    while time.time() - start_time < 3:
        for request in driver.requests:
            if request.url == url and request.response:
                _response = request.response.body
                try:
                    _response.decode('utf-8')
                except UnicodeDecodeError:
                    _response = brotli.decompress(_response)

                if _response == b'':
                    _response = '{}'
                target_response = json.loads(_response)

                del driver.requests
                return target_response

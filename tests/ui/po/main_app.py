from tests.common.common import BASE_URL
from tests.ui.common.common import Waits


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self.base_url = BASE_URL
        self.waits = Waits(driver)

    def get_page(self):
        return self._driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return self.waits.wait_until_button_clickable(time_to_wait=time, button_locator=locator)

    def get_current_url(self):
        return self._driver.current_url

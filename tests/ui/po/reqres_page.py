import time
from selenium.webdriver.common.by import By

from tests.ui.po.main_app import MainPage
from tests.api.common.common import HALF_OF_DEFAULT_UI_TIMEOUT


class MainPageLocators:

    support_reqres_locator = (By.XPATH, '//a[text()="Support ReqRes"]')
    users_locator = (By.CSS_SELECTOR, '[data-id="users"]')
    users_single_locator = (By.CSS_SELECTOR, '[data-id="users-single"]')
    users_single_not_found_locator = (By.CSS_SELECTOR, '[data-id="users-single-not-found"]')
    unknown_locator = (By.CSS_SELECTOR, '[data-id="unknown"]')
    unknown_single_locator = (By.CSS_SELECTOR, '[data-id="unknown-single"]')
    unknown_single_not_found_locator = (By.CSS_SELECTOR, '[data-id="unknown-single-not-found"]')
    post_create_locator = (By.CSS_SELECTOR, '[data-id="post"]')
    update_button_locator = (By.CSS_SELECTOR, '[data-id="put"]')
    patch_button_locator = (By.CSS_SELECTOR, '[data-id="patch"]')
    delete_button_locator = (By.CSS_SELECTOR, '[data-id="delete"]')
    register_successful_locator = (By.CSS_SELECTOR, '[data-id="register-successful"]')
    register_unsuccessful_locator = (By.CSS_SELECTOR, '[data-id="register-unsuccessful"]')
    login_successful_locator = (By.CSS_SELECTOR, '[data-id="login-successful"]')
    login_unsuccessful_locator = (By.CSS_SELECTOR, '[data-id="login-unsuccessful"]')
    delay_locator = (By.CSS_SELECTOR, '[data-id="delay"]')
    output_response_locator = (By.CSS_SELECTOR, '[data-key="output-response"]')


class MainPageMethods(MainPage):

    def click_on_button(self, locator):
        self.find_element(locator).click()

    def get_ui_output_response(self):
        # Предполагаемое время на рендеринг ui
        time.sleep(HALF_OF_DEFAULT_UI_TIMEOUT)
        return self._driver.find_element(*MainPageLocators.output_response_locator).text

import json
import requests

from tests.common.common import BASE_URL
from tests.api.common.api_endpoints import *
from tests.api.common.common import get_response_body
from tests.ui.po.reqres_page import MainPageMethods
from tests.ui.po.reqres_page import MainPageLocators as MPL


class TestGet:

    def test_users_button(self, browser):
        click_on_get_method_button(browser, MPL.users_locator, USERS + '?page=2')

    def test_user_single_button(self, browser):
        click_on_get_method_button(browser, MPL.users_single_locator, USERS + '/2')

    def test_user_single_not_found_button(self, browser):
        click_on_get_method_button(browser, MPL.users_single_not_found_locator, USERS + '/23')

    def test_unknown_button(self, browser):
        click_on_get_method_button(browser, MPL.unknown_locator, UNKNOWN)

    def test_unknown_single_button(self, browser):
        click_on_get_method_button(browser, MPL.unknown_single_locator, UNKNOWN + '/2')

    def test_unknown_single_not_found_button(self, browser):
        click_on_get_method_button(browser, MPL.unknown_single_not_found_locator, UNKNOWN + '/23')

    def test_delay_button(self, browser):
        click_on_get_method_button(browser, MPL.delay_locator, DELAY + '=3')


class TestPost:

    def test_create_button(self, browser):
        click_on_post_put_patch_method_button(browser, MPL.post_create_locator, USERS)

    def test_register_successful_button(self, browser):
        click_on_post_put_patch_method_button(browser, MPL.register_successful_locator, REGISTER)

    def test_register_unsuccessful_button(self, browser):
        click_on_post_put_patch_method_button(browser, MPL.register_unsuccessful_locator, REGISTER)

    def test_login_button(self, browser):
        click_on_post_put_patch_method_button(browser, MPL.login_successful_locator, LOGIN)

    def test_login_unsuccessful_button(self, browser):
        click_on_post_put_patch_method_button(browser, MPL.login_unsuccessful_locator, LOGIN)


class TestPut:
    def test_update_button(self, browser):
        click_on_post_put_patch_method_button(browser, MPL.update_button_locator, USERS + '/2')


class TestPatch:
    def test_update_button(self, browser):
        click_on_post_put_patch_method_button(browser, MPL.patch_button_locator, USERS + '/2')


class TestDelete:
    def test_delete_button(self, browser):
        click_on_post_put_patch_method_button(browser, MPL.delete_button_locator, USERS + '/2')


def test_click_on_support_reqres_button(browser):
    main_page = MainPageMethods(browser)
    main_page.get_page()
    main_page.click_on_button(MPL.support_reqres_locator)

    assert main_page.get_current_url() == BASE_URL + SUPPORT_HEADING


def click_on_get_method_button(browser, locator: MPL, endpoint: str) -> None:
    """
    Common steps for GET method
    :param browser: browser fixture
    :param locator: locator from Class locators
    :param endpoint: endpoint
    :return: None
    """

    main_page = MainPageMethods(browser)
    main_page.get_page()
    main_page.click_on_button(locator)

    response = requests.get(BASE_URL + endpoint)
    ui_output = main_page.get_ui_output_response()
    actual_output_dict = json.loads(ui_output)

    assert actual_output_dict == response.json()


def click_on_post_put_patch_method_button(browser, locator: MPL, endpoint: str) -> None:
    """
    Common steps for click on POST method buttons
    :param browser: browser fixture
    :param locator: locator from Class locators
    :param endpoint: endpoint
    :return: None
    """

    main_page = MainPageMethods(browser)
    main_page.get_page()
    main_page.click_on_button(locator)

    response_body = get_response_body(BASE_URL + endpoint)
    ui_output = main_page.get_ui_output_response()
    if not ui_output:
        ui_output = '{}'
    actual_ui_output_dict = json.loads(ui_output)
    assert actual_ui_output_dict == response_body

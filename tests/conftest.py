import pytest
from seleniumwire import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


@pytest.fixture(scope='session')
def browser():

    yield driver

    driver.quit()

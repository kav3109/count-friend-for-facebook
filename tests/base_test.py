import pytest
from selenium import webdriver
import core.config


@pytest.fixture(scope='class')
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    core.config.browser = webdriver.Chrome(chrome_options=options)
    core.config.browser.maximize_window()
    core.config.browser.set_page_load_timeout(30)
    core.config.browser.implicitly_wait(20)

    def teardown():
        core.config.browser.quit()

    request.addfinalizer(teardown)


@pytest.mark.usefixtures("setup")
class BaseTest(object):
    pass

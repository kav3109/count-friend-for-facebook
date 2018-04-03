from selenium.webdriver import ActionChains

from core import config
from core.elements import FindElementId, CheckTitle, FindElementClassName


def visit(url):
    config.browser.get(url)


def s_id(locator):
    return FindElementId(locator)


def s_cn(locator):
    return FindElementClassName(locator)


def c_title(checked):
    return CheckTitle(checked)


def double_click(locator):
    ActionChains(config.browser).double_click(FindElementClassName(locator)).perform()

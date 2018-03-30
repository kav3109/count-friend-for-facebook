from core import config
from core.elements import FindElement


def visit(url):
    config.browser.get(url)


def s(locator):
    return FindElement(locator)

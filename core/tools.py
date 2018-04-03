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

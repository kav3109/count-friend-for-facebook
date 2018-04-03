import time

from selenium.webdriver import ActionChains

from core import config
from core.elements import FindElementId, CheckTitle, FindElementClassName, FindElementCSSs


def visit(url):
    config.browser.get(url)


def s_id(locator):
    return FindElementId(locator)


def s_cn(locator):
    return FindElementClassName(locator)


def ss_css(locator):
    return FindElementCSSs(locator)


def c_title(checked):
    return CheckTitle(checked)


def double_click(locator):
    ActionChains(config.browser).double_click(FindElementClassName(locator)).perform()


def scroll_down():
    last_height = config.browser.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        config.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page (set param more then 1 for bad connect or hardware )
        time.sleep(4)
        # Calculate new scroll height and compare with last scroll height
        new_height = config.browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def counter(param):
    n = 0
    for i in range(len(param)):
        n = n + 1
    # output to consol
    print("You have " + str(n) + " friends!")

from core import config


class FindElement(object):

    def __init__(self, locator):
        self.locator = locator

    def finder(self):
        return config.browser.find_element_by_id(self.locator)

    def __getattr__(self, item):
        return getattr(self.finder(), item)

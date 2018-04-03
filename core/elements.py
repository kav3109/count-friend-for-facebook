from core import config


class FindElementId(object):
    def __init__(self, locator):
        self.locator = locator

    def finder_id(self):
        return config.browser.find_element_by_id(self.locator)

    def __getattr__(self, item):
        return getattr(self.finder_id(), item)


class FindElementClassName(object):
    def __init__(self, locator):
        self.locator = locator

    def finder_cn(self):
        return config.browser.find_element_by_class_name(self.locator)

    def __getattr__(self, item):
        return getattr(self.finder_cn(), item)


class FindElementCSSs(object):
    def __init__(self, locator):
        self.locator = locator

    def finder_css_s(self):
        return config.browser.find_elements_by_css_selector(self.locator)

    def __getattr__(self, item):
        return getattr(self.finder_css_s(), item)

    def __len__(self):
        return self.finder_css_s().__len__()


class CheckTitle(object):
    def __init__(self, checked):
        self.checked = checked

    def checker(self):
        assert self.checked in config.browser.title

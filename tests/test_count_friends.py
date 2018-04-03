from core.tools import visit, double_click, s_id, c_title
from tests.base_test import *


class Test(BaseTest):
    def test(self):
        visit("http://www.facebook.com")
        login("+380665932998", "#i6EydD7j")
        rid_of_push("_1vp5")


def login(log, pas):
    s_id("email").send_keys(log)
    s_id("pass").send_keys(pas)
    s_id("loginbutton").click()
    c_title("Facebook")


def rid_of_push(locator):
    double_click(locator)

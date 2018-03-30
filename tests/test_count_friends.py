from core.tools import visit, s
from tests.base_test import *


class Test(BaseTest):
    def test(self):
        visit("http://www.facebook.com")
        login("+380665932998", "#i6EydD7j")


def login(log, pas):
    s("email").send_keys(log)
    s("pass").send_keys(pas)

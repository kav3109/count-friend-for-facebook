from core.tools import visit, s
from tests.base_test import *


class Test(BaseTest):
    def test(self):
        visit("http://www.facebook.com")
        login("+380665932998")


def login(log):
    s("email").send_keys(log)
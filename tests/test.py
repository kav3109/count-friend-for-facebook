from core.tools import visit
from tests.base_test import *


class Test(BaseTest):
    def test(self):
        visit("http://www.google.com")
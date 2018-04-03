from core.tools import visit
from tests.base_test import *
from tests.pages.page_count_friends import *


class Test(BaseTest):
    def test(self):
        # open page of Facebook
        visit("http://www.facebook.com")
        # autorization (Enter your Login and Password)
        login("+380665932998", "#i6EydD7j")
        # cure for push message
        rid_of_push("_1vp5")
        # enter on the page of friends
        page_friends()
        # load all friends
        scroll_down()
        # calculating of friends
        count_friends()

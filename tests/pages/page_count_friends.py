from core.tools import s_id, c_title, double_click, s_cn, scroll_down, counter, ss_css


def login(log, pas):
    s_id("email").send_keys(log)
    s_id("pass").send_keys(pas)
    s_id("loginbutton").click()
    c_title("Facebook")


def page_friends():
    s_cn("_1vp5").click()
    s_cn("_gs6").click()


def count_friends():
    counter(len(ss_css("li._698")))

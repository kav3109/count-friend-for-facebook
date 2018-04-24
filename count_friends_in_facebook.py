from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# prepare data for test
getLogin = input("Enter your Login: ")
getPassword = input("Enter your Password: ")

# start test
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)
driver.maximize_window()

# authorization
driver.find_element_by_id("email").send_keys(getLogin)
driver.find_element_by_id("pass").send_keys(getPassword)
driver.find_element_by_id("loginbutton").click()
assert "Facebook" in driver.title

# protection from push-notification in Chrome
actionchains = ActionChains(driver)
actionchains.double_click(driver.find_element_by_class_name("_1vp5")).perform()

# open page Friends and take screenshoot
driver.find_element_by_class_name("_1vp5").click()
driver.find_element_by_class_name("_gs6").click()
driver.get_screenshot_as_file("countFriends.png")

# create scrolling to the bottom of page
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page (set param more then 1 for bad connect or hardware )
    time.sleep(1)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
# calculation count of friend
n = 0
for i in range(len(driver.find_elements_by_css_selector("li._698"))):
    n = n + 1
# output to consol
print ("You have " + str(n) + " friends!")
driver.quit()
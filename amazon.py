from selenium.webdriver import FirefoxProfile

print("Running amazon script")

from selenium.common.exceptions import TimeoutException, NoSuchElementException
import platform
import time
from selenium import webdriver


link_3080s = "https://www.amazon.com/stores/GeForce/RTX3080_GEFORCERTX30SERIES/" \
             "page/6B204EA4-AAAC-4776-82B1-D7C3BD9DDC82"

addToCart = "fulfillment-add-to-cart-button"
addtoCartID = "fulfillment-add-to-cart-button-1290a208-76ed-4368-ac14-38bf2defa2b3"
addtoCartIDMain = "add-to-cart-button"

cartButtonTopRight = "nav-cart"
checkOutButton = "btn btn-lg btn-block btn-primary"

path = ""
print("using ", platform)
if platform == "darwin":
    # OS X
    path = "/Volumes/Mac Os/Users/Kevin/Library/Application Support" \
           "/Firefox/Profiles/iku7lg6q.default/"
elif platform == "win32":
    # Windows...
    path = 'C:\\Users\\kevin\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\\ykfucrta.default-release'

profile = FirefoxProfile(path)
driver = webdriver.Firefox(profile)
driver.get(link_3080s)

elementNotFound = True
while elementNotFound:
    try:
        element = driver.find_element_by_id(addtoCartIDMain)
        element.click()
        print("Found element")
        elementNotFound = False
    except NoSuchElementException:
        elementNotFound = True
        print("element was not found")
    time.sleep(.5)
    driver.refresh()

print("element is been added to cart")
time.sleep(1)
driver.find_element_by_id(addtoCartIDMain).click()

print("going into the cart")
time.sleep(1)
driver.find_element_by_class_name(cartButtonTopRight).click()

print("Going to click checkout button")
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"cartApp\"]/d"
                             "iv[2]/div[1]/div/div/span/div/"
                             "div[1]/div[1]/section[2]/div/div"
                             "/div[3]/div/div[1]/button").click()

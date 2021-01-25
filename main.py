from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys

print("Running BestBuy")

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from sys import platform
import time
from selenium import webdriver

link_airpods = "https://www.bestbuy.com/site/searchpage.jsp?st=airpods&_" \
               "dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Glo" \
               "bal&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"

link_3080s = "https://www.bestbuy.com/site/" \
             "searchpage.jsp?st=3080&_dyncharset=UTF" \
             "-8&_dynSessConf=&id=pcat17071&type=page&sc=" \
             "Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&" \
             "usc=All+Categories&ks=960&keys=keys"

link_bestBuy = 'https://www.bestbuy.com/site/searchpage.' \
               'jsp?st=rtx+3080&_dyncharset=UTF-8&_dynSess' \
               'Conf=&id=pcat17071&type=page&sc=Global&cp=1&nrp' \
               '=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'

searchBarClass = "search-input"
searchIconClass = "header-search-icon"
searchIconXPath = '//*[@class="header-search-icon"]'
addToCart = "fulfillment-add-to-cart-button"
addtoCartID = "fulfillment-add-to-cart-button-1290a208-76ed-4368-ac14-38bf2defa2b3"
addtoCartIDMain = "fulfillment-add-to-cart-button-ed1970d1-d147-45a8-a3d2-4b969e03c839"

cartButtonTopRight = "cart-label"
checkOutButton = "btn btn-lg btn-block btn-primary"
path = ""
print("using ", platform)
timeToSleep = 0
if platform == "darwin":
    # OS X
    path = "/Volumes/Mac Os/Users/Kevin/Library/Application Support" \
           "/Firefox/Profiles/iku7lg6q.default/"
    timeToSleep = 3
elif platform == "win32":
    # Windows...
    path = 'C:\\Users\\kevin\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\\ykfucrta.default-release'
    timeToSleep = 1

profile = FirefoxProfile(path)
driver = webdriver.Firefox(profile)
driver.implicitly_wait(3)
driver.get(link_bestBuy)
driver.find_element_by_class_name(searchBarClass).send_keys("RTX 3080")
time.sleep(.5)
driver.find_element_by_xpath(searchIconXPath).click()


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
        driver.back()
    time.sleep(timeToSleep)

    try:
        #driver.find_element_by_class_name(searchBarClass).send_keys("RTX 3080")
        driver.find_element_by_xpath(searchIconXPath).click()
    except NoSuchElementException:
        print("did not find element")
        driver.refresh()

print("element is been added to cart")
time.sleep(1)
driver.find_element_by_class_name(addToCart).click()

print("going into the cart")
time.sleep(1)
driver.find_element_by_class_name(cartButtonTopRight).click()

print("Going to click checkout button")

time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"cartApp\"]/d"
                             "iv[2]/div[1]/div/div/span/div/"
                             "div[1]/div[1]/section[2]/div/div"
                             "/div[3]/div/div[1]/button").click()


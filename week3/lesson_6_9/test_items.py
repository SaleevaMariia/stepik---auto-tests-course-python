from selenium.webdriver.common.by import By
import time


def test_is_basket_available(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button_size = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))
    assert button_size > 0, "button add to basket is not present"



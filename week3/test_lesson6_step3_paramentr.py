import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link_part1="https://stepik.org/lesson/"
link_part2="/step/1"

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize('page', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_params(browser, page):
    browser.get(f"{link_part1}{page}{link_part2}")
    input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "textarea"))
    )
    answer = math.log(int(time.time()))
    input.send_keys(str(answer))
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()
    alert = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    assert alert.text == "Correct!", "number is not correct, try again"




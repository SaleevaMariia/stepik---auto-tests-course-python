import unittest
from selenium import webdriver
import time

class TestFirst(unittest.TestCase):
    def test_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first[placeholder='Input your first name']")
        input1.send_keys("Иван")
        input2 = browser.find_element_by_css_selector(".second[placeholder='Input your last name']")
        input2.send_keys("Иванов")
        input3 = browser.find_element_by_css_selector(".third[placeholder='Input your email']")
        input3.send_keys("jerkhrdjhg@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",  welcome_text)

    def test_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first[placeholder='Input your first name']")
        input1.send_keys("Иван")
        input2 = browser.find_element_by_css_selector(".second[placeholder='Input your last name']")
        input2.send_keys("Иванов")
        input3 = browser.find_element_by_css_selector(".third[placeholder='Input your email']")
        input3.send_keys("jerkhrdjhg@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_fname = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
    element_fname.send_keys("Имя")

    element_lname = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    element_lname.send_keys("Фамилия")

    element_email = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
    element_email.send_keys("Мой email")

    element_phone = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']")
    element_phone.send_keys("Мой phone")

    element_address = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
    element_address.send_keys("Мой address")

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
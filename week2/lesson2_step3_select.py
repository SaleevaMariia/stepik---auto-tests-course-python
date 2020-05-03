from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1_element = browser.find_element_by_id("num1").text
    num2_element = browser.find_element_by_id("num2").text
    summa = int(num1_element)+int(num2_element)
    summa = str(summa)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summa)       
  
    button = browser.find_element_by_class_name("btn")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
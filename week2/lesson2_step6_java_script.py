from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
  
try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
       
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    check_box = browser.find_element_by_css_selector("[for='robotCheckbox']")
    check_box.click()
    radio_button = browser.find_element_by_css_selector("[for='robotsRule']")
    radio_button.click()
    
    button = browser.find_element_by_tag_name("button")
  #  browser.execute_script("return arguments[0].scrollIntoView(true);", button)    
    button.click()  
            

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
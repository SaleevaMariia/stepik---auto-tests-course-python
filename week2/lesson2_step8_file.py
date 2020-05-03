from selenium import webdriver
import time
import os 


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys("Mariia")
    
    surname=browser.find_element_by_css_selector("[name='lastname']")
    surname.send_keys("Ivanova")
    
    email=browser.find_element_by_css_selector("[name='email']")
    email.send_keys("Ivanova@gmail.com")
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 
      
    file=browser.find_element_by_css_selector("[type='file']")
    file.send_keys(file_path)      
        
    button = browser.find_element_by_class_name("btn") 
    button.click()  
            

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
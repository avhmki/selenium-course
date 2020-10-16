from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    file_input = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  
    file_path = os.path.join(current_dir, 'file.txt.txt')
    file_input.send_keys(file_path)
        
    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('Popa')
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Pipa')
    email = browser.find_element_by_name('email')
    email.send_keys('mail@mail.ru')

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
    
finally:
    # успеваем скопировать код за 30 секундR
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

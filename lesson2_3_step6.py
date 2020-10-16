from selenium import webdriver
import time 
import math


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
    
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    y = calc(x)
        
    input_result = browser.find_element_by_id('answer')
    input_result.send_keys(y)
    
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

    
finally:
    # успеваем скопировать код за 30 секундR
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

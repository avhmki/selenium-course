from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
        
    input_result = browser.find_element_by_id('answer')
    input_result.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # успеваем скопировать код за 30 секундR
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

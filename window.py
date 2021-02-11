from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
driver.implicitly_wait(5)

driver.get('http://suninjuly.github.io/redirect_accept.html')
driver.find_element_by_tag_name('button').click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

x = driver.find_element_by_id('input_value').text
driver.find_element_by_id('answer').send_keys(calc(x))

driver.find_element_by_tag_name('button').click()

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

driver.quit()

# browser.switch_to.window(window_name)
# new_window = browser.window_handles[1]
# first_window = browser.window_handles[0]
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/alert_accept.html')
driver.find_element_by_tag_name('button').click()

confirm = driver.switch_to.alert
confirm.accept()

x = driver.find_element_by_id('input_value').text
driver.find_element_by_id('answer').send_keys(calc(x))

driver.find_element_by_tag_name('button').click()

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

driver.quit()

# alert = driver.switch_to.alert
# alert_text = alert.text
# alert.accept()
#
#
# confirm = driver.switch_to.alert
# confirm.accept()
# confirm.dismiss()
#
#
# prompt = driver.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()
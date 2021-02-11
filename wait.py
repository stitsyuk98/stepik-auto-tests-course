from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/explicit_wait2.html')
WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
driver.find_element_by_id('book').click()


x = driver.find_element_by_id('input_value').text
driver.find_element_by_id('answer').send_keys(calc(x))

driver.find_element_by_id('solve').click()



alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

driver.quit()

# browser.switch_to.window(window_name)
# new_window = browser.window_handles[1]
# first_window = browser.window_handles[0]
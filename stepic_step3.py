from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest, math, time

url = 'https://stepik.org/lesson/236905/step/1'

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url)
    answer = math.log(int(time.time()))
    # WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, 'textarea')))
    textarea = driver.find_element_by_css_selector('.textarea')
    # time.sleep(3)
    textarea.send_keys(str(answer))
    driver.find_element_by_css_selector('.submit-submission').click()
    el = driver.find_element_by_css_selector('pre.smart-hints__hint')
    assert el.text == "Correct!", 'blin(((!'

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
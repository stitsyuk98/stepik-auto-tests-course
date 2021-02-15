from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# browser.execute_script("return arguments[0].scrollIntoView(true);", a)

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    mas = browser.find_elements_by_xpath('//input[@type="text"]')
    for a in mas:
        a.send_keys('text')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '../file.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_id('file').send_keys(file_path)

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    # Select(browser.find_element_by_id('dropdown')).select_by_visible_text(str(x))
    # browser.find_element_by_id('robotCheckbox').click()
    # browser.find_element_by_id('robotsRule').click()
    # browser.find_element_by_css_selector('.first_block .first').send_keys('Имя')
    # browser.find_element_by_css_selector('.first_block .second').send_keys('Фамилия')
    # browser.find_element_by_css_selector('.first_block .third').send_keys('mail@mail.ru')


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    print(welcome_text_elt)
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest, math, time

@pytest.fixture
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    # return driver
    yield driver
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    driver.quit()

@pytest.mark.parametrize('url',[('https://stepik.org/lesson/236895/step/1'),
                                       ('https://stepik.org/lesson/236896/step/1'),
                                       ('https://stepik.org/lesson/236897/step/1'),
                                       ('https://stepik.org/lesson/236898/step/1'),
                                       ('https://stepik.org/lesson/236899/step/1'),
                                       ('https://stepik.org/lesson/236903/step/1'),
                                       ('https://stepik.org/lesson/236904/step/1'),
                                       ('https://stepik.org/lesson/236905/step/1')])


# url = 'https://stepik.org/lesson/236905/step/1'
class TestZad():
    def test_zad(self, url):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get(url)
        answer = math.log(int(time.time()+0.022))
        # WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, 'textarea')))
        textarea = driver.find_element_by_css_selector('.textarea')
        # time.sleep(3)
        textarea.send_keys(str(answer))
        driver.find_element_by_css_selector('.submit-submission').click()
        el = driver.find_element_by_css_selector('pre.smart-hints__hint')
        assert el.text == "Correct!", 'blin(((!'
        driver.quit()


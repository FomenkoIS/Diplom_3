import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

TIMEOUT = 10

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    @property
    def url(self):
        return self.driver.current_url
    
    @allure.step('Открытие страницы')
    def open(self):
        self.driver.get(self.URL)


    @allure.step('Поиск элемента с локатором {locator}')
    def find_element(self, locator, timeout=TIMEOUT):
        return self._wait_for_element(locator, timeout)

    @allure.step('Ожидание видимости элемента с локатором {locator}')
    def _wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидание исчезновения элемента с локатором {locator}')
    def _wait_for_element_disappear(self, locator, timeout=TIMEOUT):

        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    
    @allure.step('Ожидание кликабельности элемента с локатором {locator}')
    def _wait_for_element_to_be_clickable(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    @allure.step('Клик по элементу с локатором {locator}')
    def click_element(self, locator, timeout=TIMEOUT):
        self._wait_for_element(locator)
        self._wait_for_element_to_be_clickable(locator).click()


    @allure.step('Ввод текста в элемент с локатором {locator}')
    def send_keys_to_element(self, locator, keys):
        element = self._wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получение текста из элемента с локатором {locator}')
    def get_text_from_element(self, locator, timeout=TIMEOUT):
        return self._wait_for_element(locator, timeout).text

    @allure.step('Прокрутка до элемента с локатором {locator}')
    def scroll_to_element(self, locator, timeout=TIMEOUT):
        element = self._wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        return element

    @allure.step('Ожидание исчезновения элемента с локатором {locator}')
    def _wait_for_element_disappear(self, locator, timeout=TIMEOUT):

        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step('Проверка отображения элемента с локатором {locator}')
    def is_element_displayed(self, locator, timeout=TIMEOUT):

        try:
            element = self._wait_for_element(locator, timeout)
            return element.is_displayed()
        except:
            return False




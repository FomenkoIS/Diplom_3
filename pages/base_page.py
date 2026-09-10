import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        element = self._wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        return element


    @allure.step('Проверка отображения элемента с локатором {locator}')
    def is_element_displayed(self, locator, timeout=TIMEOUT):

        try:
            element = self._wait_for_element(locator, timeout)
            return element.is_displayed()
        except:
            return False


    @allure.step('Перетаскивание через JavaScript')
    def drag_and_drop_js(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        
        script = """
            function createEvent(type, clientX, clientY) {
                var event = new MouseEvent(type, {
                    view: window,
                    bubbles: true,
                    cancelable: true,
                    clientX: clientX,
                    clientY: clientY
                });
                return event;
            }
            
            var source = arguments[0];
            var target = arguments[1];
            
            var sourceRect = source.getBoundingClientRect();
            var targetRect = target.getBoundingClientRect();
            
            var sourceX = sourceRect.left + sourceRect.width / 2;
            var sourceY = sourceRect.top + sourceRect.height / 2;
            var targetX = targetRect.left + targetRect.width / 2;
            var targetY = targetRect.top + targetRect.height / 2;
            
            source.dispatchEvent(createEvent('mousedown', sourceX, sourceY));
            source.dispatchEvent(createEvent('dragstart', sourceX, sourceY));
            
            document.dispatchEvent(createEvent('dragover', targetX, targetY));
            document.dispatchEvent(createEvent('dragenter', targetX, targetY));
            
            target.dispatchEvent(createEvent('dragover', targetX, targetY));
            target.dispatchEvent(createEvent('dragenter', targetX, targetY));
            target.dispatchEvent(createEvent('drop', targetX, targetY));
            
            source.dispatchEvent(createEvent('dragend', targetX, targetY));
            source.dispatchEvent(createEvent('mouseup', targetX, targetY));
        """
        self.driver.execute_script(script, source, target)
        
    @allure.step('Ожидание появления текста {text} в элементе с локатором {locator}')
    def _wait_for_text_in_element(self, locator, text, timeout=TIMEOUT):

        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
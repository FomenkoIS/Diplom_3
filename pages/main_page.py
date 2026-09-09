import allure
from pages.base_page import BasePage
from url import MAIN_URL
from locators.main_page_locators import MainLocators
from selenium.webdriver.common.action_chains import ActionChains
from data import UserForLogin
import time

class MainPage(BasePage):
    URL = MAIN_URL

    @allure.step('Клик по кнопке Конструктор в шапке')
    def click_constructor_button(self):

        self.click_element(MainLocators.CONSTRUCTOR_BUTTON)


    @allure.step('Клик по кнопке Лента заказов в шапке')
    def click_list_orders_button(self):

        self.click_element(MainLocators.LIST_ORDERS_BUTTON)


    @allure.step('Клик по кнопке Личный кабинет в шапке')
    def click_personal_account_button(self):

        self.click_element(MainLocators.PERSONAL_ACCOUNT_BUTTON)


    @allure.step('Клик по кнопке Соусы и переход на вкладку Соусы в конструкторе')
    def click_sauces_button(self):

        self.click_element(MainLocators.SAUCES_BUTTON)
        self._wait_for_element(MainLocators.SAUCES_HEADER)
        time.sleep(0.5)

    @allure.step('Клик по кнопке Начинки и переход на вкладку Начинки в конструкторе')
    def click_fillings_button(self):
    
        self.click_element(MainLocators.FILLINGS_BUTTON)
        self._wait_for_element(MainLocators.FILLINGS_HEADER)
        time.sleep(0.5)


    @allure.step('Клик по 1-ой булке в разделе Булки (открыть попап)')
    def click_first_buns_open(self):

        if self.is_element_displayed(MainLocators.INGREDIENT_POPUP_HEADER, timeout=2):
            self.click_close_ingredient_popup_button()
        self.click_element(MainLocators.FIRST_BUNS_INGREDIENT)
        self._wait_for_element(MainLocators.INGREDIENT_POPUP_HEADER)

    @allure.step('Клик по 1-ой булке в разделе Булки (открыть и закрыть попап)')
    def click_first_buns(self):

        self.click_first_buns_open()
        self.click_close_ingredient_popup_button()

    @allure.step('Клик по 1-му соусу в разделе Соусы (только открыть)')
    def click_first_sauces_open(self):


        self.scroll_to_element(MainLocators.FIRST_FILLINGS_INGREDIENT)
        self.click_element(MainLocators.FIRST_SAUCES_INGREDIENT)
        self._wait_for_element(MainLocators.INGREDIENT_POPUP_HEADER)

    @allure.step('Клик по 1-му соусу в разделе Соусы (открыть и закрыть)')
    def click_first_sauces(self):

        self.click_first_sauces_open()
        self.click_close_ingredient_popup_button()
        

    @allure.step('Клик по 1-ой начинке в разделе Начинки (только открыть)')
    def click_first_fillings_open(self):

        self.scroll_to_element(MainLocators.FIRST_FILLINGS_INGREDIENT)
        self.click_element(MainLocators.FIRST_FILLINGS_INGREDIENT)
        self._wait_for_element(MainLocators.INGREDIENT_POPUP_HEADER)

    @allure.step('Клик по 1-ой начинке в разделе Начинки (открыть и закрыть)')
    def click_first_fillings(self):

        self.click_first_fillings_open()
        self.click_close_ingredient_popup_button()

    @allure.step('Клик по крестику попапа с информацией об ингредиенте')
    def click_close_ingredient_popup_button(self):

        self._wait_for_element(MainLocators.INGREDIENT_POPUP_CLOSE_BUTTON)
        self.click_element(MainLocators.INGREDIENT_POPUP_CLOSE_BUTTON)
        self._wait_for_element_disappear(MainLocators.INGREDIENT_POPUP_HEADER)


    @allure.step('Добавляем булку в бургер')
    def add_bun_to_burger(self):

        self.scroll_to_element(MainLocators.FIRST_BUNS_INGREDIENT)
        super().drag_and_drop_js(
            MainLocators.FIRST_BUNS_INGREDIENT,
            MainLocators.CONSTRUCTOR_OF_BURGER
        )
        time.sleep(2)


    @allure.step('Добавляем соус в бургер')
    def add_sauce_to_burger(self):

        self.scroll_to_element(MainLocators.FIRST_SAUCES_INGREDIENT)
        super().drag_and_drop_js(
            MainLocators.FIRST_SAUCES_INGREDIENT,
            MainLocators.CONSTRUCTOR_OF_BURGER
        )
        time.sleep(2)


    @allure.step('Добавляем начинку в бургер')
    def add_filling_to_burger(self):

        self.scroll_to_element(MainLocators.FIRST_FILLINGS_INGREDIENT)
        super().drag_and_drop_js(
            MainLocators.FIRST_FILLINGS_INGREDIENT,
            MainLocators.CONSTRUCTOR_OF_BURGER
        )
        time.sleep(2)

    @allure.step('Получение значения счетчика ингредиента')
    def get_counter_value(self, counter_locator):
        
        counter_element = self.find_element(counter_locator)
        return int(counter_element.text)


    @allure.step('Создание заказа и получение его номера')
    def create_order_and_get_number(self):

        self.click_constructor_button()
        self._wait_for_element(MainLocators.MAIN_HEADER)
        self.add_bun_to_burger()

        self.click_element(MainLocators.SAUCES_BUTTON)
        self._wait_for_element(MainLocators.SAUCES_HEADER)
        self.add_sauce_to_burger()

        self.click_element(MainLocators.FILLINGS_BUTTON)
        self._wait_for_element(MainLocators.FILLINGS_HEADER)
        self.add_filling_to_burger()

        self.click_element(MainLocators.ORDER_BUTTON)
        self._wait_for_element(MainLocators.ORDER_POPUP_ORDER_NUMBER)
        current_order_number = int(self.get_text_from_element(MainLocators.ORDER_POPUP_ORDER_NUMBER))
        self.click_element(MainLocators.ORDER_POPUP_CLOSE_BUTTON)
        return current_order_number


    @allure.step('Авторизация под известным пользователем')
    def login(self, email=UserForLogin.LOGIN_EMAIL, password=UserForLogin.LOGIN_PASSWORD):

        self.click_element(MainLocators.PERSONAL_ACCOUNT_BUTTON)
        self._wait_for_element(MainLocators.LOGIN_HEADER)
        self.send_keys_to_element(MainLocators.EMAIL_FIELD, email)
        self.send_keys_to_element(MainLocators.PASSWORD_FIELD, password)
        self.click_element(MainLocators.ENTER_BUTTON)
        self._wait_for_element(MainLocators.MAIN_HEADER)        
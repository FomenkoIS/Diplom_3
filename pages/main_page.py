import allure
from pages.base_page import BasePage
from url import MAIN_URL
from locators.main_page_locators import MainLocators

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


    @allure.step('Клик по кнопке Начинки и переход на вкладку Начинки в конструкторе')
    def click_fillings_button(self):
    
        self.click_element(MainLocators.FILLINGS_BUTTON)
        self._wait_for_element(MainLocators.FILLINGS_HEADER)


    @allure.step('Клик по 1-ой булке в разделе Булки')
    def click_first_buns(self):
    
        self.click_element(MainLocators.FIRST_BUNS_INGREDIENT)
        self._wait_for_element(MainLocators.INGREDIENT_POPUP_HEADER)    

    @allure.step('Клик по 1-му соусу в разделе Соусы')
    def click_first_sauces(self):

        self.click_element(MainLocators.SAUCES_BUTTON)
        self._wait_for_element(MainLocators.SAUCES_HEADER)
        self.click_element(MainLocators.FIRST_SAUCES_INGREDIENT)
        self._wait_for_element(MainLocators.INGREDIENT_POPUP_HEADER)             
        

    @allure.step('Клик по 1-ой начинке в разделе Начинки')
    def click_first_fillings(self):

        self.click_element(MainLocators.FILLINGS_BUTTON)
        self._wait_for_element(MainLocators.FILLINGS_HEADER)
        self.click_element(MainLocators.FIRST_FILLINGS_INGREDIENT)
        self._wait_for_element(MainLocators.INGREDIENT_POPUP_HEADER)

    @allure.step('Клик по крестику попапа с информацией об ингридиенте')
    def click_close_ingreient_popup_button(self):

        self._wait_for_element(MainLocators.INGREDIENT_POPUP_CLOSE_BUTTON)
        self.click_element(MainLocators.INGREDIENT_POPUP_CLOSE_BUTTON)
       
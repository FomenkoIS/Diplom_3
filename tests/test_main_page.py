import allure
from pages.base_page import BasePage
from url import MAIN_URL
from locators.main_page_locators import MainLocators
from locators.order_page_locators import OrderLocators


class TestMainPage:


    @allure.title('Переход по клику на Конструктор')
    @allure.description('Переход в Конструктор по клику по кнопке Конструктор')
    def test_constructor_button__click(self, order_page):

        order_page.open()
        order_page.click_constructor_button()

        assert order_page.get_text_from_element(MainLocators.MAIN_HEADER) == 'Соберите бургер'


    @allure.title('Переход по клику в раздел Лента заказов')
    @allure.description('Переход в раздел Лента заказов при клике по кнопке Лента заказов')
    def test_list_orders_button__click(self, main_page):

        main_page.open()
        main_page.click_bottom_order_button()

        assert main_page.get_text_from_element(OrderLocators.ORDER_HEADER) == 'Лента заказов'


    @allure.title('Клик по ингридиенту из категории Булки, появление окна с деталями')
    @allure.description('Появление всплывающего окна с деталями при клике по ингридиенту из категории Булки')
    def test_buns_popup(self, main_page):

        main_page.open()
        main_page.click_first_buns()

        assert main_page.get_text_from_element(MainLocators.INGREDIENT_POPUP_HEADER) == 'Детали ингредиента'


    @allure.title('Клик по ингридиенту из категории Соусы, появление окна с деталями')
    @allure.description('Появление всплывающего окна с деталями при клике по ингридиенту из категории Соусы')
    def test_sauces_popup(self, main_page):

        main_page.open()
        main_page.click_sauces_button()
        main_page.click_first_sauces()

        assert main_page.get_text_from_element(MainLocators.INGREDIENT_POPUP_HEADER) == 'Детали ингредиента'



    @allure.title('Клик по ингридиенту из категории Начинки, появление окна с деталями')
    @allure.description('Появление всплывающего окна с деталями при клике по ингридиенту из категории Начинки')
    def test_fillings_popup(self, main_page):

        main_page.open()
        main_page.click_fillings_button()
        main_page.click_first_fillings()

        assert main_page.get_text_from_element(MainLocators.INGREDIENT_POPUP_HEADER) == 'Детали ингредиента'


    @allure.title('Всплывающее окно с информацией о булке закрывается кликом по крестику')
    @allure.description('Если кликнуть на крестик всплывающее окно с информацией о булке закрывается')
    def test_close_buns_popup(self, main_page):

        main_page.open()
        main_page.click_first_buns()
        main_page.click_close_ingredient_popup_button()

        assert not main_page._wait_for_element(MainLocators.INGREDIENT_POPUP_HEADER), "Попап не закрылся"


    @allure.title('Всплывающее окно с информацией о соусе закрывается кликом по крестику')
    @allure.description('Если кликнуть на крестик всплывающее окно с информацией о соусе закрывается')
    def test_close_sauces_popup(self, main_page):

        main_page.open()
        main_page.click_sauces_button()
        main_page.click_first_sauces()
        main_page.click_close_ingredient_popup_button()

        assert not main_page._wait_for_element(MainLocators.INGREDIENT_POPUP_HEADER), "Попап не закрылся"



    @allure.title('Всплывающее окно с информацией о начинке закрывается кликом по крестику')
    @allure.description('Если кликнуть на крестик всплывающее окно с информацией о начинке закрывается')
    def test_close_fillings_popup(self, main_page):

        main_page.open()
        main_page.click_fillings_button()
        main_page.click_first_fillings()
        main_page.click_close_ingredient_popup_button()

        assert not main_page._wait_for_element(MainLocators.INGREDIENT_POPUP_HEADER), "Попап не закрылся"




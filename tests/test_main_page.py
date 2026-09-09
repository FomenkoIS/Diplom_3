import allure
from locators.main_page_locators import MainLocators
from locators.order_page_locators import OrderLocators


class TestMainPage:


    @allure.title('Переход по клику на Конструктор')
    @allure.description('Переход в Конструктор по клику по кнопке Конструктор')
    def test_constructor_button__click(self, main_page):

        main_page.open()
        main_page.click_list_orders_button()
        main_page.click_constructor_button()

        assert main_page.get_text_from_element(MainLocators.MAIN_HEADER) == 'Соберите бургер'


    @allure.title('Переход по клику в раздел Лента заказов')
    @allure.description('Переход в раздел Лента заказов при клике по кнопке Лента заказов')
    def test_list_orders_button__click(self, main_page):

        main_page.open()
        main_page.click_list_orders_button()

        assert main_page.get_text_from_element(OrderLocators.ORDER_HEADER) == 'Лента заказов'


    @allure.title('Клик по ингредиенту из категории Булки, появление окна с деталями')
    @allure.description('Появление всплывающего окна с деталями при клике по ингредиенту из категории Булки')
    def test_buns_popup(self, main_page):

        main_page.open()
        main_page.click_first_buns_open()

        assert main_page.get_text_from_element(MainLocators.INGREDIENT_POPUP_HEADER) == 'Детали ингредиента'


    @allure.title('Клик по ингредиенту из категории Соусы, появление окна с деталями')
    @allure.description('Появление всплывающего окна с деталями при клике по ингредиенту из категории Соусы')
    def test_sauces_popup(self, main_page):

        main_page.open()
        main_page.click_first_sauces_open()

        assert main_page.get_text_from_element(MainLocators.INGREDIENT_POPUP_HEADER) == 'Детали ингредиента'



    @allure.title('Клик по ингредиенту из категории Начинки, появление окна с деталями')
    @allure.description('Появление всплывающего окна с деталями при клике по ингредиенту из категории Начинки')
    def test_fillings_popup(self, main_page):

        main_page.open()
        main_page.click_first_fillings_open()

        assert main_page.get_text_from_element(MainLocators.INGREDIENT_POPUP_HEADER) == 'Детали ингредиента'


    @allure.title('Всплывающее окно с информацией о булке закрывается кликом по крестику')
    @allure.description('Если кликнуть на крестик всплывающее окно с информацией о булке закрывается')
    def test_close_buns_popup(self, main_page):

        main_page.open()
        main_page.click_first_buns_open()
        main_page.click_close_ingredient_popup_button()

        assert not main_page.is_element_displayed(MainLocators.INGREDIENT_POPUP_HEADER), "Попап не закрылся"


    @allure.title('Всплывающее окно с информацией о соусе закрывается кликом по крестику')
    @allure.description('Если кликнуть на крестик всплывающее окно с информацией о соусе закрывается')
    def test_close_sauces_popup(self, main_page):

        main_page.open()
        main_page.click_first_sauces_open()
        main_page.click_close_ingredient_popup_button()

        assert not main_page.is_element_displayed(MainLocators.INGREDIENT_POPUP_HEADER), "Попап не закрылся"



    @allure.title('Всплывающее окно с информацией о начинке закрывается кликом по крестику')
    @allure.description('Если кликнуть на крестик всплывающее окно с информацией о начинке закрывается')
    def test_close_fillings_popup(self, main_page):

        main_page.open()
        main_page.click_first_fillings_open()
        main_page.click_close_ingredient_popup_button()

        assert not main_page.is_element_displayed(MainLocators.INGREDIENT_POPUP_HEADER), "Попап не закрылся"


    @allure.title('Добавление булки в бургер увеличивает счетчик')
    @allure.description('При перетаскивании булки в конструктор счетчик увеличивается')
    def test_add_bun_increase_counter(self, main_page):

        main_page.open()
        initial_counter = main_page.get_counter_value(MainLocators.FIRST_BUNS_COUNTER)
        main_page.add_bun_to_burger()
        new_counter = main_page.get_counter_value(MainLocators.FIRST_BUNS_COUNTER)
        
        assert new_counter == initial_counter + 2, "Счетчик не увеличился"


    @allure.title('Добавление соуса в бургер увеличивает счетчик')
    @allure.description('При перетаскивании соуса в конструктор счетчик увеличивается')
    def test_add_sauce_increase_counter(self, main_page):

        main_page.open()
        main_page.click_sauces_button()
        initial_counter = main_page.get_counter_value(MainLocators.FIRST_SAUCES_COUNTER)
        main_page.add_sauce_to_burger()
        new_counter = main_page.get_counter_value(MainLocators.FIRST_SAUCES_COUNTER)
        
        assert new_counter == initial_counter + 1, "Счетчик не увеличился"


    @allure.title('Добавление начинки в бургер увеличивает счетчик')
    @allure.description('При перетаскивании начинки в конструктор счетчик увеличивается')
    def test_add_filling_increase_counter(self, main_page):

        main_page.open()
        main_page.click_fillings_button()
        initial_counter = main_page.get_counter_value(MainLocators.FIRST_FILLINGS_COUNTER)
        main_page.add_filling_to_burger()
        new_counter = main_page.get_counter_value(MainLocators.FIRST_FILLINGS_COUNTER)
        
        assert new_counter == initial_counter + 1, "Счетчик не увеличился"



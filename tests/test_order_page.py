import allure
from locators.main_page_locators import MainLocators
from locators.order_page_locators import OrderLocators


class TestOrderPage:


    @allure.title('После оформлении заказа, счетчик Выполнено за всё время увеличивается')
    @allure.description('При оформлении заказа счетчик Выполнено за всё время увеличивается на 1')
    def test_orders_count_increases_after_order(self, main_page, order_page):

        order_page.open()
        
        initial_count = order_page.get_number_of_orders_for_all_time()
        
        main_page.click_constructor_button()
        main_page.create_order_and_get_number()

        main_page.click_list_orders_button()
        updated_count = order_page.get_number_of_orders_for_all_time()
        
        assert updated_count == initial_count + 1, 'Счетчик Выполнено за всё время не увеличился'


    @allure.title('После оформлении заказа, счетчик Выполнено за сегодня увеличивается')
    @allure.description('При оформлении заказа счетчик Выполнено за сегодня увеличивается на 1')
    def test_today_orders_count_increases_after_order(self, main_page, order_page):

        order_page.open()
        
        initial_count = order_page.get_number_of_orders_for_today()
        
        main_page.click_constructor_button()
        main_page.create_order_and_get_number()
        
        main_page.click_list_orders_button()
        updated_count = order_page.get_number_of_orders_for_today()
        
        assert updated_count == initial_count + 1, 'Счетчик Выполнено за сегодня не увеличился'


    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description('При оформлении заказа его номер с 0 вначале появляется в разделе В работе')
    def test_order_number_appear_in_at_work(self, main_page, order_page):

        main_page.open()

        new_order_number = str(main_page.create_order_and_get_number())
        
        main_page.click_list_orders_button()
        order_page.wait_for_orders_ready_to_disappear()
        order_number_in_at_work = order_page.get_number_of_order_at_work()
        
        assert new_order_number in order_number_in_at_work, 'Номера сделанного заказа нет в разделе В работе'
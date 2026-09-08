import allure
from pages.base_page import BasePage
from url import LIST_ORDER_URL
from locators.order_page_locators import OrderLocators
from locators.main_page_locators import MainLocators

class OrderPage(BasePage):

    URL = LIST_ORDER_URL
    
    @allure.step('Получить число заказов за все время')
    def get_number_of_orders_for_all_time(self):

        return int(self.get_text_from_element(OrderLocators.ALL_TIME_DONE))


    @allure.step('Получить число заказов за сегодня')
    def get_number_of_orders_for_today(self):

        return int(self.get_text_from_element(OrderLocators.TODAY_DONE))


    @allure.step('Получить номер заказа из раздела В работе')
    def get_number_of_order_at_work(self):
    
        return self.get_text_from_element(OrderLocators.AT_WORK)

    @allure.step('Ожидание исчезновения текста Все текущие заказы готовы!')
    def wait_for_orders_ready_to_disappear(self, timeout=10):

        self._wait_for_element_disappear(OrderLocators.ALL_ORDERS_COMPLETED, timeout)




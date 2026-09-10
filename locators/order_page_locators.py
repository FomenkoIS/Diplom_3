from selenium.webdriver.common.by import By

class OrderLocators:


    ORDER_HEADER = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")

    ALL_TIME_DONE = (By.XPATH, "//div[contains(@class, 'undefined')]/p[contains(@class, 'OrderFeed_number')]")
    TODAY_DONE = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    AT_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    ALL_ORDERS_COMPLETED = (By.XPATH, "//li[text()='Все текущие заказы готовы!']")

    




    
     
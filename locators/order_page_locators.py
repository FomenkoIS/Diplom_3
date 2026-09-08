from selenium.webdriver.common.by import By

class OrderLocators:

    ORDER_HEADER = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
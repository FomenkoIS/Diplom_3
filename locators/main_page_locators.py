from selenium.webdriver.common.by import By

class MainLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//ul//a[@href='/']")
    LIST_ORDERS_BUTTON = (By.XPATH, "//a[@href='/feed']")
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div/a[@href='/']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")

    MAIN_HEADER = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    BUNS_BUTTON = (By.XPATH, "//div[span[contains(text(), 'Булки')]]")
    SAUCES_BUTTON = (By.XPATH, "//div[span[contains(text(), 'Соусы')]]")
    FILLINGS_BUTTON = (By.XPATH, "//div[span[contains(text(), 'Начинки')]]")


    INGREDIENT_POPUP_HEADER = (By.XPATH, "//h2[text() = 'Детали ингредиента']")
    INGREDIENT_POPUP_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button")

    FIRST_BUNS_INGREDIENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    FIRST_BUNS_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[contains(@class, 'counter_counter')]")
    


    FIRST_SAUCES_INGREDIENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']")
    FIRST_SAUCES_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']//p[contains(@class, 'counter_counter')]")


    FIRST_FILLINGS_INGREDIENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6f']")
    FIRST_FILLINGS_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6f']//p[contains(@class, 'counter_counter')]")


    BUNS_HEADER = (By.XPATH, "//h2[contains(text(), 'Булки')]")
    SAUCES_HEADER = (By.XPATH, "//h2[contains(text(), 'Соусы')]")
    FILLINGS_HEADER = (By.XPATH, "//h2[contains(text(), 'Начинки')]")

    LOG_IN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_POPUP_ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//h2")
    ORDER_POPUP_TEXT = (By.XPATH, "//div/p[contains(text(), 'идентификатор заказа')]")
    ORDER_POPUP_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button")


    CONSTRUCTOR_OF_BURGER = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")


    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_FIEL = (By.XPATH, "//input[@type='password']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
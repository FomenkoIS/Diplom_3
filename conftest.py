import pytest

from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    
    driver.maximize_window()
    
    yield driver
    driver.quit()



@pytest.fixture
def main_page(driver):

    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    
    return OrderPage(driver)
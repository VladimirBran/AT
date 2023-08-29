# import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://test.theconf.ru/"

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        # наличие кнопки войти
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "li.header__signin > a")

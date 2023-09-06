import time
from logging import root

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

link = "https://test.theconf.ru/login"
link_1 = "https://test.theconf.ru/"

def test_autorisation(browser):
    # browser = webdriver.Chrome() открывает ещё одно окно браузера
    browser.get(link)
    user_name = browser.find_element(By.CSS_SELECTOR, "div.mail > input[type=mail]")
    user_name.send_keys("89625407194@mail.ru")
    password = browser.find_element(By.CSS_SELECTOR, "div.password > input[type=password]")
    password.send_keys("1234567!Dv")
    password.send_keys(Keys.RETURN)   #""""вместо нажатия на кнопку "войти", заменяет enter"""""
    # button_1 = browser.find_element(By.CSS_SELECTOR, "div > form > button")
    # button_1.click()
    time.sleep(5)


def test_filter(browser):
    browser.get(link_1)
    button = browser.find_element(By.XPATH, "/html/body/div/div/div/ul/li[2]/a")  # выбор "все конфереции"
    button.click()
    time.sleep(5)
    button_2 = browser.find_element(By.XPATH, "/html/body/div/div/section/div[2]/div[1]/div/div")  # выбор фильтра "ВУЗ"
    button_2.click()
    time.sleep(5)
    browser.quit()

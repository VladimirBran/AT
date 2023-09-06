import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

link = "https://theconf.ru/login"
login = "mops144@mail.ru"
password_user = "1234567!Dv"


def test_autorisation(browser):
    # browser = webdriver.Chrome() открывает ещё одно окно браузера
    browser.get(link)
    browser.manage().window().maximize()
    user_name = browser.find_element(By.CSS_SELECTOR, "div.mail > input[type=mail]")
    user_name.send_keys(login)
    password = browser.find_element(By.CSS_SELECTOR, "div.password > input[type=password]")
    password.send_keys(password_user)
    # password.send_keys(Keys.RETURN) вместо нажатия на кнопку "войти", заменяет enter
    button = browser.find_element(By.CSS_SELECTOR, "div > form > button")
    button.click()
    time.sleep(5)
    browser.quit()

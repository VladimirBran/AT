import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

link = "https://test.theconf.ru/"


def test_scroll(browser):
    # browser = webdriver.Chrome() открывает ещё одно окно браузера
    browser.get(link)
    # user_name = browser.find_element(By.CSS_SELECTOR, "div.mail > input[type=mail]")
    # user_name.send_keys("89625407194@mail.ru")
    # password = browser.find_element(By.CSS_SELECTOR, "div.password > input[type=password]")
    # password.send_keys("1234567!Dv")
    # # password.send_keys(Keys.RETURN) вместо нажатия на кнопку "войти", заменяет enter
    # button = browser.find_element(By.CSS_SELECTOR, "div > form > button")
    # button.click()
    time.sleep(1)

    browser.execute_script("window.scrollTo(0,500)")

    time.sleep(1)
    browser.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://test.theconf.ru/login"

try:
    browser = webdriver.Chrome()
    time.sleep(10)  # добавить эту строку после запуска браузера
    browser.get(link)



    input1 = browser.find_element(By.CSS_SELECTOR, "div.mail > input[type=mail]")
    input1.send_keys("boberkurwa@mail.ru")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.password > input[type=password]")
    input2.send_keys("1234567!Dv")
    button = browser.find_element(By.CSS_SELECTOR, "div > form > button")
    button.click()
    feedback = browser.find_element_by_css_selector('div.greeting__text > h1').text
    # Проверяем ответ
    assert feedback == 'Correct!'
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
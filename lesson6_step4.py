from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    time.sleep(10)  # добавить эту строку после запуска браузера
    browser.get(link)



    input1 = browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input ")
    input1.send_keys("Boba")
    input2 = browser.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input")
    input2.send_keys("Fett")
    input3 = browser.find_element(By.CSS_SELECTOR, "div:nth-child(3) > input")
    input3.send_keys("Seversk")
    input4 = browser.find_element(By.CSS_SELECTOR, "div:nth-child(4) > input")
    input4.send_keys("Mandalor")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
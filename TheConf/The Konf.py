from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
# подготовка для теста
# открываем страницу первого товара
link = "https://test.theconf.ru/"

try:
    browser = webdriver.Chrome()
    time.sleep(10)  # добавить эту строку после запуска браузера
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input")
    input1.send_keys("экон ")
    time.sleep(10)
    # Нажимаем кнопку "Отправить"
    input4 = browser.find_element(By.XPATH, "/header/div/form/div[2]/ul/div/button")
    input4.click()
    time.sleep(10)

finally:


    # закрываем браузер после всех манипуляций
    browser.quit()

#root > header > div > form > div.input > input
# //*[@id="root"]/header/div/form/div[2]/ul/a[1]/div/div[1]/span/span[2]
# //*[@id="root"]/header/div/form/div[2]/ul/div/button
#root > header > div > form > div.dropdown-filter > ul > div > button
#root > header > div > form > div.dropdown-filter > ul > a:nth-child(1) > div > div:nth-child(2) > span > span:nth-child(3)
#root > div > div > section:nth-child(3) > div.conference__container > div:nth-child(1) > div.conference__tags > a > div
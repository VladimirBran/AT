from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
       #Функция возращает результат формулы
       #:param x:
       #:return:
      return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

# Находим элемент, содержащий значение x
    x = browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute('valuex')
# Получаем текст внутри этого элемента
    #x = x_element.text
# Считаем функцию со значением х
    y = calc(x)

# Передаем в поле ввода результат вычисления функции
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

# Кликаем чекбокс "Подтверждаю, что являюсь роботом"
    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()

# Кликаем radio "Роботы рулят"
    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input3.click()

# Нажимаем кнопку "Отправить"
    input4 = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    input4.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
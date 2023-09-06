import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://theconf.ru/login"
login = "mops144@mail.ru"
password_user = "1234567!Dv"
# login_1 = "mopsreal@mail.ru" #может быть несколько пользователей
# password_user_1 = "1234567!Dv" #можно единый пароль сделать, тогда переменная одна будет

browser = webdriver.Chrome()
browser.get(link)
user_name = browser.find_element(By.CSS_SELECTOR, "div.mail > input[type=mail]")
user_name.send_keys(login)
password = browser.find_element(By.CSS_SELECTOR, "div.password > input[type=password]")
password.send_keys(password_user)
# password.send_keys(Keys.RETURN) вместо нажатия на кнопку "войти", заменяет enter
button = browser.find_element(By.CSS_SELECTOR, "div > form > button")
button.click()
time.sleep(1)
text_reg = browser.find_element(By.CSS_SELECTOR, "div > h1") #проверяем элемент на нужной странице после авторизации
# записываем в переменную feedback_text текст из элемента feedback_text_reg
feedback_text_reg = text_reg.text
print(feedback_text_reg)
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert feedback_text_reg == "Здесь находится страница авторизованного пользователя"
print("DONE")
# url = "https://theconf.ru/profile" #проверяем url на нужной странице после авторизации, элемент может меняться, url нет
# get_url = browser.current_url
# print(get_url)
# assert url == get_url
# print("Done")


time.sleep(5)
browser.quit()
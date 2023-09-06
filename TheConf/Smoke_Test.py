import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

link = "https://test.theconf.ru/login"



def test_autorisation(browser):
# browser = webdriver.Chrome() открывает ещё одно окно браузера
    browser.get(link)

    user_name = browser.find_element(By.CSS_SELECTOR, "div.mail > input[type=mail]")
    user_name.send_keys("89625407194@mail.ru")
    password = browser.find_element(By.CSS_SELECTOR, "div.password > input[type=password]")
    password.send_keys("1234567!Dv")
    # password.send_keys(Keys.RETURN) вместо нажатия на кнопку "войти", заменяет enter
    button = browser.find_element(By.CSS_SELECTOR, "div > form > button")
    button.click()
    time.sleep(1)

    button = browser.find_element(By.XPATH, "/html/body/div/div/div/ul/li[2]/a")  # выбор "все конфереции"
    button.click()
    time.sleep(1)

    # запоминаем ключевое слово
    word_conf_1 = browser.find_element(By.XPATH, "/html/body/div/div/section/div[3]/div[1]/div/h2")
    # # conf_2.click()
    value_word_conf_1 = word_conf_1.text
    print(value_word_conf_1)

    select_conf_1 = browser.find_element(By.XPATH, "//html/body/div/div/section/div[3]/div[1]/div/a[1]")
    select_conf_1.click() #выбираем конференцию
    time.sleep(1)
    favorites_tab_add = browser.find_element(By.CSS_SELECTOR, "div.full-conference__container-top > div > svg")
    favorites_tab_add.click() #добавляем в избранное
    time.sleep(1)
    favorites_tab = browser.find_element(By.CSS_SELECTOR, "li:nth-child(2) > a > div > div > svg")
    favorites_tab.click() #открываем избранное
    time.sleep(1)
    select_conf_2 = browser.find_element(By.XPATH, "/html/body/div/div/section/div[2]/div/div/a[1]")
    select_conf_2.click()  # выбираем конференцию
    time.sleep(1)

    # проверяем наличие конференции с ключевым словом в избранном
    word_conf_2 = browser.find_element(By.CSS_SELECTOR, "div.full-conference > div > div.full-conference__title > h1")
    value_word_conf_2 = word_conf_2.text
    print(value_word_conf_2)

    assert value_word_conf_1 == value_word_conf_2
    print("Success") # сверяем наличие ключевого слова

    favorites_tab_delete = browser.find_element(By.CSS_SELECTOR, "div.full-conference > div > div.full-conference__container-top > div > svg > path")
    favorites_tab_delete.click() # удаляем из избранного

    exit_button = browser.find_element(By.CSS_SELECTOR, "li.header__signin > button")
    exit_button.click() # выходим из системы

    time.sleep(5)
    browser.quit()


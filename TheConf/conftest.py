# Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл conftest.py,
# который должен лежать в директории верхнего уровня в вашем проекте с тестами.
# Можно создавать дополнительные файлы conftest.py в других директориях,
# но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

login_user = "mops144@mail.ru"
password_user = "1234567!Dv"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

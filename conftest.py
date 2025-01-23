import allure
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    with allure.step("Настройка драйвера"):
        driver = webdriver.Firefox()
        driver.maximize_window()

    yield driver

    with allure.step("Закрытие драйвера"):
        driver.quit()

import allure
import pytest
from pages.main_page import MainPage
from helpers.data import TestData
from helpers.urls import Urls


@allure.suite("Основной набор тестов")
@allure.sub_suite("Тесты главной страницы")
class TestMainPage:

    @allure.description("На главной странице проверяем, что в разделе 'Вопросы о важном' указан верный текст")
    @pytest.mark.parametrize("accordion_locator, text_locator, expected_text, title", TestData.test_data)
    def test_text_answer(self, driver, accordion_locator, text_locator, expected_text, title):
        allure.dynamic.title(title)

        with allure.step(f"Открываем страницу {Urls.BASE_URL}"):
            main_page = MainPage(driver, Urls.BASE_URL)
            main_page.open()

        with allure.step("Проверяем, что текст соответствует ожидаемому"):
            text = main_page.check_text_accordion(accordion_locator, text_locator)

        assert text == expected_text, f"Ожидалось: '{expected_text}', получено: '{text}'"

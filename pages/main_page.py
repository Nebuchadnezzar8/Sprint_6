import allure
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Нажимаем на выпадающий список и проверяем текст")
    def check_text_accordion(self, accordion_locator, text_locator):
        self.go_to_element(accordion_locator)
        self.click_element(accordion_locator)
        return self.check_text(text_locator)

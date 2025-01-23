import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполняем первую форму заказа")
    def fill_in_the_first_form(self, data):
        self.go_to_element(data["order_button"])
        self.click_element(data["order_button"])
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, data["name"])
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, data["surname"])
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, data["address"])
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.click_element(data["metro"])
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, data["phone"])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполняем вторую форму заказа")
    def fill_in_the_second_form(self, data):
        self.click_element(OrderPageLocators.DATE_INPUT)
        self.click_element(data["date"])
        self.click_element(OrderPageLocators.RENT_DROPDOWN)
        self.click_element(data["rent"])
        self.click_element(data["checkbox"])
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, data["comment"])
        self.click_element(OrderPageLocators.ORDER_BUTTON_FORM)
        self.click_element(OrderPageLocators.ORDER_BUTTON_CONFIRM)

    @allure.step("Проверяем, что модальное окно 'Заказ оформлен' отображается на экране")
    def is_order_modal_visible(self):
        return self.element_is_visible(OrderPageLocators.MODAL_WINDOW)

    @allure.step("Проверяем ссылку на главную страницу через лого")
    def open_scooter_links(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_STATUS)
        self.click_element(OrderPageLocators.LOGO_SCOOTER_LINK)

    @allure.step("Проверяем ссылку на DZEN")
    def open_dzen_link(self):
        self.click_element(OrderPageLocators.LOGO_YANDEX_LINK)

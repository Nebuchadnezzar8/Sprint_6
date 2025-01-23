import allure
import pytest
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from helpers.data import DataUser
from helpers.urls import Urls


@allure.suite("Основной набор тестов")
@allure.sub_suite("Тесты страницы заказа")
class TestOrderPage:

    @allure.title("Заполнение формы заказа и переход по ссылкам")
    @allure.description("Проверка заполнение формы заказа самоката и переход по ссылкам на главную страницу и DZEN")
    @pytest.mark.parametrize("order_data", DataUser.data_user)
    def test_fill_the_form(self, driver, order_data):

        with allure.step(f"Открываем страницу {Urls.BASE_URL}"):
            order_page = OrderPage(driver, Urls.BASE_URL)
            order_page.open()

        order_page.fill_in_the_first_form(order_data)
        order_page.fill_in_the_second_form(order_data)

        with allure.step(f"Проверяем что заказ был создан"):
            modal_visible = order_page.element_is_visible(OrderPageLocators.MODAL_WINDOW)
            assert modal_visible, f"Модальное окно 'Заказ оформлен' не появилось. Текущее состояние: {modal_visible}"

        order_page.open_scooter_links()
        order_page.url_to_be(Urls.BASE_URL)
        current_url = driver.current_url
        assert current_url == Urls.BASE_URL, f"Ожидалось: {Urls.BASE_URL}, Получено:  {current_url}"

        order_page.open_dzen_link()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        order_page.url_to_be(Urls.DZEN_URL)
        current_url = driver.current_url
        assert current_url == Urls.DZEN_URL, f"Ожидалось: {Urls.DZEN_URL}, Получено:  {current_url}"

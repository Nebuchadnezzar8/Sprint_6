import allure
import pytest
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
            modal_visible = order_page.is_order_modal_visible()
            assert modal_visible, f"Модальное окно 'Заказ оформлен' не появилось. Текущее состояние: {modal_visible}"

        order_page.open_scooter_links()
        order_page.url_to_be(Urls.BASE_URL)
        assert order_page.get_current_url() == Urls.BASE_URL, f"Ожидалось: {Urls.BASE_URL}, Получено:  {order_page.get_current_url()}"

        order_page.open_dzen_link()
        order_page.switch_to_window(1)
        order_page.url_to_be(Urls.DZEN_URL)
        assert order_page.get_current_url() == Urls.DZEN_URL, f"Ожидалось: {Urls.DZEN_URL}, Получено:  {order_page.get_current_url()}"

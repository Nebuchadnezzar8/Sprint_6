from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from helpers.generator import generate_user_data


# тестовые данные для формы
class DataUser:
    user_1 = generate_user_data()
    user_2 = generate_user_data()

    data_user = [
        {
            "order_button": OrderPageLocators.ORDER_BUTTON,
            "name": user_1["name"],
            "surname": user_1["surname"],
            "address": "Ленина 10, д. 17",
            "metro": OrderPageLocators.METRO_STATION_1,
            "phone": user_1["phone"],
            "date": OrderPageLocators.TODAY_DATE,
            "rent": OrderPageLocators.RENT_DROPDOWN_OPTION_1,
            "checkbox": OrderPageLocators.CHECKBOX_BLACK,
            "comment": user_1["comment"]
        },
        {
            "order_button": OrderPageLocators.ORDER_BUTTON_2,
            "name": user_2["name"],
            "surname": user_2["surname"],
            "address": "Пушкина 77, д. 13",
            "metro": OrderPageLocators.METRO_STATION_2,
            "phone": user_2["phone"],
            "date": OrderPageLocators.TODAY_DATE,
            "rent": OrderPageLocators.RENT_DROPDOWN_OPTION_2,
            "checkbox": OrderPageLocators.CHECKBOX_GREY,
            "comment": ""
        }
    ]


# Текст для выпадающего списка
class TextAccordion:
    COST_AND_PAYMENT_TEXT = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    MULTIPLE_SCOOTERS_TEXT = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                              'можете просто сделать несколько заказов — один за другим.')
    RENTAL_TIME_TEXT = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                        'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                        'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    ORDER_TODAY_TEXT = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    EXTEND_OR_RETURN_TEXT = ('Пока что нет! Но если что-то срочное — всегда можно '
                             'позвонить в поддержку по красивому номеру 1010.')
    CHARGER_PROVIDED_TEXT = ('Самокат приезжает к вам с полной зарядкой. '
                             'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                             'Зарядка не понадобится.')
    CANCEL_ORDER_TEXT = ('Да, пока самокат не привезли. Штрафа не будет, '
                         'объяснительной записки тоже не попросим. Все же свои.')
    DELIVERY_OUTSIDE_MKAD_TEXT = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


# Тестовые данные для выпадающего списка
class TestData:
    test_data = [
        (MainPageLocators.ACCORDION_COST_AND_PAYMENT, MainPageLocators.ELEMENT_COST_AND_PAYMENT,
         TextAccordion.COST_AND_PAYMENT_TEXT, "Проверка текста для стоимости и оплаты"),
        (MainPageLocators.ACCORDION_MULTIPLE_SCOOTERS, MainPageLocators.ELEMENT_MULTIPLE_SCOOTERS,
         TextAccordion.MULTIPLE_SCOOTERS_TEXT, "Проверка текста для нескольких самокатов"),
        (MainPageLocators.ACCORDION_RENTAL_TIME, MainPageLocators.ELEMENT_RENTAL_TIME, TextAccordion.RENTAL_TIME_TEXT,
         "Проверка текста для времени аренды"),
        (MainPageLocators.ACCORDION_ORDER_TODAY, MainPageLocators.ELEMENT_ORDER_TODAY, TextAccordion.ORDER_TODAY_TEXT,
         "Проверка текста для заказа на сегодня"),
        (MainPageLocators.ACCORDION_EXTEND_OR_RETURN, MainPageLocators.ELEMENT_EXTEND_OR_RETURN,
         TextAccordion.EXTEND_OR_RETURN_TEXT, "Проверка текста для продление/возврат"),
        (MainPageLocators.ACCORDION_CHARGER_PROVIDED, MainPageLocators.ELEMENT_CHARGER_PROVIDED,
         TextAccordion.CHARGER_PROVIDED_TEXT, "Проверка текста для зарядки"),
        (MainPageLocators.ACCORDION_CANCEL_ORDER, MainPageLocators.ELEMENT_CANCEL_ORDER,
         TextAccordion.CANCEL_ORDER_TEXT, "Проверка текста для отмены заказа"),
        (MainPageLocators.ACCORDION_DELIVERY_OUTSIDE_MKAD, MainPageLocators.ELEMENT_DELIVERY_OUTSIDE_MKAD,
         TextAccordion.DELIVERY_OUTSIDE_MKAD_TEXT, "Проверка текста для доставки за МКАД")
    ]

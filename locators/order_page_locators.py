from selenium.webdriver.common.by import By


class OrderPageLocators:
    # локаторы для 1 формы
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BUTTON_2 = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp' and text()='Заказать']")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@class='select-search__input']")
    METRO_STATION_1 = (By.XPATH, "(//div[text()='Бульвар Рокоссовского'])[1]")
    METRO_STATION_2 = (By.XPATH, "(//div[text()='Черкизовская'])[1]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # локаторы для 2 формы
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    TODAY_DATE = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and @tabindex='0']")
    RENT_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-control']")
    RENT_DROPDOWN_OPTION_1 = (By.XPATH, "//div[@class='Dropdown-menu']//div[text()='двое суток']")
    RENT_DROPDOWN_OPTION_2 = (By.XPATH, "//div[@class='Dropdown-menu']//div[text()='сутки']")
    CHECKBOX_BLACK = (By.XPATH, "//label[@for='black']")
    CHECKBOX_GREY = (By.XPATH, "//label[@for='grey']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_FORM = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[contains(text(),'Заказать')]")
    ORDER_BUTTON_CONFIRM = (By.XPATH, "//button[text()='Да']")

    # локаторы для проверки заказа и ссылок
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
    ORDER_BUTTON_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")
    LOGO_SCOOTER_LINK = (By.XPATH, "//img[contains(@src, '/assets/scooter.svg')]")
    LOGO_YANDEX_LINK = (By.XPATH, "//img[contains(@src, '/assets/ya.svg')]")






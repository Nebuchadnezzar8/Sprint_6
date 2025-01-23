from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCORDION_COST_AND_PAYMENT = (By.ID, 'accordion__heading-0') # локатор для 1 списка
    ELEMENT_COST_AND_PAYMENT = (By.XPATH, "//div[@id='accordion__panel-0']//p") # локатор для 1 списка
    ACCORDION_MULTIPLE_SCOOTERS = (By.ID, 'accordion__heading-1') # локатор для 2 списка
    ELEMENT_MULTIPLE_SCOOTERS = (By.XPATH, "//div[@id='accordion__panel-1']//p") # локатор для 2 списка
    ACCORDION_RENTAL_TIME = (By.ID, 'accordion__heading-2') # локатор для 3 списка
    ELEMENT_RENTAL_TIME = (By.XPATH, "//div[@id='accordion__panel-2']//p") # локатор для 3 списка
    ACCORDION_ORDER_TODAY = (By.ID, 'accordion__heading-3') # локатор для 4 списка
    ELEMENT_ORDER_TODAY = (By.XPATH, "//div[@id='accordion__panel-3']//p") # локатор для 4 списка
    ACCORDION_EXTEND_OR_RETURN = (By.ID, 'accordion__heading-4') # локатор для 5 списка
    ELEMENT_EXTEND_OR_RETURN = (By.XPATH, "//div[@id='accordion__panel-4']//p") # локатор для 5 списка
    ACCORDION_CHARGER_PROVIDED = (By.ID, 'accordion__heading-5') # локатор для 6 списка
    ELEMENT_CHARGER_PROVIDED = (By.XPATH, "//div[@id='accordion__panel-5']//p") # локатор для 6 списка
    ACCORDION_CANCEL_ORDER = (By.ID, 'accordion__heading-6') # локатор для 7 списка
    ELEMENT_CANCEL_ORDER = (By.XPATH, "//div[@id='accordion__panel-6']//p") # локатор для 7 списка
    ACCORDION_DELIVERY_OUTSIDE_MKAD = (By.ID, 'accordion__heading-7') # локатор для 8 списка
    ELEMENT_DELIVERY_OUTSIDE_MKAD = (By.XPATH, "//div[@id='accordion__panel-7']//p") # локатор для 8 списка
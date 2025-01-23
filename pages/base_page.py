import allure
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("Открыть страницу браузера")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Найти видимый элемент")
    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Проверить наличие элемента")
    def element_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Найти кликабельный элемент")
    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Проверяем что URL изменился")
    def url_to_be(self, expected_url, timeout=20):
        return wait(self.driver, timeout).until(EC.url_to_be(expected_url))

    @allure.step("Проскролить до элемента")
    def go_to_element(self, locator, timeout=10):
        element = self.element_is_present(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator, timeout=10):
        element = self.element_is_clickable(locator, timeout)
        element.click()

    @allure.step("Добавить текст в элемент")
    def send_keys_to_element(self, locator, text, timeout=10):
        element = self.element_is_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Взять текст элемента")
    def check_text(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).text

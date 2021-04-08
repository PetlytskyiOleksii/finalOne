from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from constants.urls import URLS


class MainPage:

    TARIFF_BUTTON = (By.XPATH, "//a[contains(@class, 'btn') and text() = 'Выбор тарифа']")

    def __init__(self, browser):
        self.browser = browser

    def load(self, needed_link):
        self.browser.get(needed_link)

    def open_modal_window(self):
        tariff_button = self.browser.find_element(*self.TARIFF_BUTTON)
        assert tariff_button.is_displayed(), "Rate button does not exist"
        tariff_button.click()

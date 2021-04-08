from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from constants.urls import URLS


class MainPage:

    TARIFF_BUTTON = (By.XPATH, "//a[contains(@class, 'btn') and text() = 'Точный рассчет стоимости сайта']")

    def __init__(self, browser):
        self.browser = browser

    def load(self, needed_link):
        self.browser.get(needed_link)

    def open_modal_window(self):
        tariff_button = self.browser.find_element(*self.TARIFF_BUTTON)
        tariff_button.click()

    def to_check_if_traffic_button_text_correct(self):
        tariff_button = self.browser.find_element(*self.TARIFF_BUTTON)
        return tariff_button.is_displayed()

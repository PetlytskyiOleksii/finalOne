from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage:

    TARIFF_BUTTON = (By.XPATH, "//a[contains(@class, 'btn') and text() = 'Точный рассчет стоимости сайта']")
    STIM_RB_RF_BUTTON = (By.XPATH, "//div[contains(@style, 'stim')]")
    ORDER_SELLING_WEBSITE_BUTTON = (By.XPATH, "//a[contains(text(), 'продающий сайт')]")

    def __init__(self, browser):
        self.browser = browser

    def open_main_page(self, needed_link):
        self.browser.get(needed_link)

    def open_modal_window(self):
        tariff_button = self.browser.find_element(*self.TARIFF_BUTTON)
        tariff_button.click()

    def check_if_traffic_button_text_correct(self):
        tariff_button = self.browser.find_element(*self.TARIFF_BUTTON)
        return tariff_button.is_displayed()

    def scroll_page(self):
        self.browser.find_element_by_tag_name('body').send_keys(Keys.END)

    def click_stim_rb_rf_button(self):
        stim_rb_rf_button = self.browser.find_element(*self.STIM_RB_RF_BUTTON)
        stim_rb_rf_button.click()

    def check_order_selling_site_button_present(self):
        order_selling_site_button = self.browser.find_element(*self.ORDER_SELLING_WEBSITE_BUTTON)
        return order_selling_site_button.is_displayed()

    def click_order_selling_site_button_present(self):
        order_selling_site_button = self.browser.find_element(*self.ORDER_SELLING_WEBSITE_BUTTON)
        order_selling_site_button.click()

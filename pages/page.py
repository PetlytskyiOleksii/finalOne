from selenium.webdriver.support import expected_conditions as EC
from constants import messages
from constants import urls
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    TARIFF_BUTTON = (By.XPATH, "//a[contains(@class, 'btn') and text() = 'Точный рассчет стоимости сайта']")
    STIM_RB_RF_BUTTON = (By.XPATH, "//div[contains(@style, 'stim')]")
    ORDER_SELLING_WEBSITE_BUTTON = (By.XPATH, "//a[contains(text(), 'продающий сайт')]")

    def __init__(self, browser):
        self.browser = browser

    def find_element(self, locator, wait_time):
        if WebDriverWait(self.browser, wait_time).until(EC.visibility_of_element_located(locator)):
            return WebDriverWait(self.browser, wait_time).until(EC.invisibility_of_element_located(locator))
        raise Exception(messages.NO_SUCH_ELEMENT)

    def find_elements(self, locator, wait_time):
        if WebDriverWait(self.browser, wait_time).until(EC.visibility_of_all_elements_located(locator)):
            return WebDriverWait(self.browser, wait_time).until(EC.visibility_of_all_elements_located(locator))
        raise Exception(messages.NO_SUCH_ELEMENTS)

    def go_to_url(self, base_url):
        self.browser.get(base_url)

    def open_modal_window(self):
        tariff_button = self.browser.find_element(*Page.TARIFF_BUTTON)
        tariff_button.click()

    def check_if_traffic_button_text_correct(self):
        tariff_button = self.browser.find_element(*Page.TARIFF_BUTTON)
        return tariff_button.is_displayed()

    def scroll_page(self):
        self.browser.find_element_by_tag_name('body').send_keys(Keys.END)

    def click_stim_rb_rf_button(self):
        stim_rb_rf_button = self.browser.find_element(*Page.STIM_RB_RF_BUTTON)
        stim_rb_rf_button.click()

    def check_order_selling_site_button_present(self):
        order_selling_site_button = self.browser.find_element(*Page.ORDER_SELLING_WEBSITE_BUTTON)
        return order_selling_site_button.is_displayed()

    def click_order_selling_site_button_present(self):
        order_selling_site_button = self.browser.find_element(*Page.ORDER_SELLING_WEBSITE_BUTTON)
        order_selling_site_button.click()

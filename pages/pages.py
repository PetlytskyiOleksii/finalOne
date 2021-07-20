from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Pages:
    NAME_FIELD = (By.NAME, 'Name')
    PHONE_FIELD = (By.NAME, 'Phone')
    ORDER_BUTTON = (By.XPATH, "//form[contains(@class, 'form_sub')]//a[text()='Заказать']")
    CLOSE_ORDER_MODAL_WINDOW_BUTTON = (By.XPATH, "//div[@id='formZ']//button[@class='close exicon']")
    ORDER_SITE_MODAL_WINDOW = (By.XPATH, "//div[@id='formZ' and @style='display: block;']")
    SUCCESS_ORDER_BLOCK = (By.XPATH, "//div[@id='formZ']//div[contains(@class, 'successbox')]")

    # протестировать как элемент!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    @staticmethod
    def REQUIRED_FIELD_WARNING():
        return By.XPATH, "//div[text()='Это поле обязательно для заполнения']"

    def __init__(self, browser):
        self.browser = browser

    def check_order_site_modal_window_present(self):
        order_site_modal_window = self.browser.find_element(*Pages.ORDER_SITE_MODAL_WINDOW)
        return order_site_modal_window.is_displayed()

    def click_order_button(self):
        order_button = self.browser.find_element(*Pages.ORDER_BUTTON, 10)
        order_button.click()

    def check_required_fields_warnings_show(self):
        return len(self.browser.find_elements(*Pages.REQUIRED_FIELD_WARNING()))

    def input_name(self, name):
        name_field = self.browser.find_element(*Pages.NAME_FIELD)
        name_field.send_keys(f"{name}")

    def input_phone_number(self, phone_number):
        phone_field = self.browser.find_element(*Pages.PHONE_FIELD)
        phone_field.send_keys(f"{phone_number}")

    def check_success_order_block_shows(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(Pages.SUCCESS_ORDER_BLOCK))

    def close_order_modal_window(self):
        self.browser.find_element(*Pages.CLOSE_ORDER_MODAL_WINDOW_BUTTON).click()
        return WebDriverWait(self.browser, 2).until(EC.invisibility_of_element_located(Pages.ORDER_SITE_MODAL_WINDOW))

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TariffModalWindow:

    @staticmethod
    def CURRENT_STEP_LABEL(step):
        return By.XPATH, f"//div[@id='meedget_popup_content']//div[@step={step}]//div[@class='meedget_step']"
    MODAL_WINDOW = (By.ID, "meedget_popup_content")
    NEXT_STEP_BUTTON = (By.XPATH, "//div[@step='1']//*[text()='Cледующий шаг']")
    PREVIOUS_STEP_BUTTON = (By.XPATH, "//div[@step='2']//*[text()='К предыдущему шагу']")
    CLOSE_MODAL_WINDOW_BUTTON = (By.CLASS_NAME, "meedget_close_link")
    @staticmethod
    def CHECKBOX(amount):
        return By.XPATH, f"//label//p[contains(text(), '{amount}')]"

    def __init__(self, browser):
        self.browser = browser

    def check_modal_window_shows(self):
        modal_window = self.browser.find_element(*self.MODAL_WINDOW)
        return modal_window.is_displayed()

    def check_current_step(self, step):
        current_step_label = self.browser.find_element(*TariffModalWindow.CURRENT_STEP_LABEL(step))
        return current_step_label.text

    def check_next_step_button_present(self):
        next_step_button = self.browser.find_element(*self.NEXT_STEP_BUTTON)
        return next_step_button.is_displayed()

    def select_the_first_option(self, amount):
        first_option_checkbox = self.browser.find_element(*TariffModalWindow.CHECKBOX(amount))
        first_option_checkbox.click()

    def click_next_step_button(self):
        next_step_button = self.browser.find_element(*self.NEXT_STEP_BUTTON)
        next_step_button.click()

    def click_previous_button(self):
        previous_step_button = self.browser.find_element(*self.PREVIOUS_STEP_BUTTON)
        previous_step_button.click()

    def close_modal_window(self):
        close_modal_window_button = self.browser.find_element(*self.CLOSE_MODAL_WINDOW_BUTTON)
        close_modal_window_button.click()
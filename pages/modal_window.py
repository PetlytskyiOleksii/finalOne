from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ModalWindow:

    @staticmethod
    def CURRENT_STEP_LABEL(step):
        return By.XPATH, f"//div[@id='meedget_popup_content']//div[@step={step}]//div[@class='meedget_step']"
    MODAL_WINDOW = (By.ID, "meedget_popup_content")

    def __init__(self, browser):
        self.browser = browser

    def to_check_modal_window_shows(self):
        modal_window = self.browser.find_element(*self.MODAL_WINDOW)
        return modal_window.is_displayed()

    def to_check_current_step(self, step):
        current_step_label = self.browser.find_element(*ModalWindow.CURRENT_STEP_LABEL(step))
        return current_step_label.text

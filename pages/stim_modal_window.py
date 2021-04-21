from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StimModalWindow:

    STIM_MODAL_WINDOW = (By.XPATH, "//img[contains(@src, 'stim')]")
    CLOSE_STIM_MODAL_WINDOW_BUTTON = (By.CLASS_NAME, "popup_close")

    def __init__(self, browser):
        self.browser = browser

    def check_if_stim_modal_shows(self):
        stim_modal_window = self.browser.find_element(*StimModalWindow.STIM_MODAL_WINDOW)
        print(stim_modal_window.is_displayed())
        return stim_modal_window.is_displayed()

    def close_stim_modal_window(self):
        close_stim_modal_window_button = self.browser.find_element(*StimModalWindow.CLOSE_STIM_MODAL_WINDOW_BUTTON)
        close_stim_modal_window_button.click()
        return WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located(StimModalWindow.STIM_MODAL_WINDOW))
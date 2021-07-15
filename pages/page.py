from selenium.webdriver.support import expected_conditions as EC
from constants import messages
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    LOGIN_BUTTON = (By.XPATH, '//a[@href="/auth/login"]')
    REGISTRATION_BUTTON = (By.XPATH, '//a[@href="/auth/register"]')

    # LOGIN WINDOW
    NAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, '//button[@airloadwhen="login"]')
    FORGOT_PASS_BUTTON = (By.XPATH, '//a[@href="/auth/forgot-password"]')

    # REGISTRATION WINDOW
    PHONE_NUMBER_FIELD = (By.ID, "username")
    PHONE_CITY_FIELD = (By.XPATH, "//input[@formcontrolname='city']")
    FULL_NAME_FIELD = (By.XPATH, '//input[@formcontrolname="name" and @placeholder="שם מלא"]')
    AGREE_TO_MAILING_CHECKBOX = (By.XPATH, '//air-checkbox[@formcontrolname="add_to_mailing_list"]')
    AGREE_TO_TERMS_CHECKBOX = (By.XPATH, '//air-checkbox[@formcontrolname="agree_to_terms"]')



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

    def check_if_login_button_is_present(self):
        login_button = self.browser.find_element(*Page.LOGIN_BUTTON)
        return login_button.is_displayed()

    def click_login_button(self):
        login_button = self.browser.find_element(*Page.LOGIN_BUTTON)
        login_button.click()

    def click_registration_button(self):
        registration_button = self.browser.find_element(*Page.REGISTRATION_BUTTON)
        registration_button.click()

    def check_input_name_field_shows(self):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(Page.NAME_FIELD))

    def click_name(self):
        name_field = self.browser.find_element(*Page.NAME_FIELD)
        name_field.click()

    def input_name(self, name):
        name_field = self.browser.find_element(*Page.NAME_FIELD)
        name_field.send_keys(f"{name}")

    def click_password(self):
        name_field = self.browser.find_element(*Page.PASSWORD_FIELD)
        name_field.click()

    def input_password(self, password):
        name_field = self.browser.find_element(*Page.PASSWORD_FIELD)
        name_field.send_keys(f"{password}")

    def click_submit_login_button(self):
        submit_login_button = self.browser.find_element(*Page.SUBMIT_LOGIN_BUTTON)
        submit_login_button.click()

    def scroll_page(self):
        self.browser.find_element_by_tag_name('body').send_keys(Keys.END)

    def check_order_selling_site_button_present(self):
        order_selling_site_button = self.browser.find_element(*Page.ORDER_SELLING_WEBSITE_BUTTON)
        return order_selling_site_button.is_displayed()

    def click_order_selling_site_button_present(self):
        order_selling_site_button = self.browser.find_element(*Page.ORDER_SELLING_WEBSITE_BUTTON)
        order_selling_site_button.click()

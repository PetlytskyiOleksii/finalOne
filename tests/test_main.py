import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from constants.urls import URLS
from pages.main_page import MainPage


@pytest.fixture
def browser():
    driver = Chrome("/Users/opetlytskyi/finalProject/drivers/chromedriver")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_if_the_button_present(browser):
    main_page = MainPage(browser)
    main_page.load(URLS["BASE_URL"])
    main_page.open_modal_window()

    # browser.get(URLS["BASE_URL"])
    # tariff_button = browser.find_element(By.XPATH, "//a[contains(@class, 'btn') and text() = 'Выбор тарифа']")
    # "to check if Rate button exists"
    # assert tariff_button.is_displayed(), "Rate button does not exist"
    # print("Rate button exists")
    # tariff_button.click()
    # receive_an_offer_window = browser.find_element(By.ID, "meedget_block")
    # "to check if the Modal window exists"
    # assert receive_an_offer_window.is_displayed(), "Modal window does not exist"
    # print("Modal window exists")
    # current_step_label_1 = browser.find_element(By.XPATH, "//div[@id=\"meedget_popup_content\"]//div[@step=\"1\"]//div[@class=\"meedget_step\"]")
    # "to check if the current step is exist"
    # assert current_step_label_1.text == "Шаг: 1 из 4"
    # next_step_button = browser.find_element(By.XPATH, "(//button[contains(@class, \"next\") and text()=\"Cледующий шаг\"])[1]")
    # "to check if the next step button is exist"
    # assert next_step_button.is_displayed(), "Next step button does not exist"
    # "to select the first option:'site level complexity'"
    # first_level_complexity = browser.find_element(By.XPATH, "//*[@for=\"ans0-01\"]")
    # first_level_complexity.click()
    # "click next step button"
    # next_step_button.click()
    # "to check if the label is changed"
    # current_step_label_2 = browser.find_element(By.XPATH,
    #                                           "//div[@id=\"meedget_popup_content\"]//div[@step=\"2\"]//div[@class=\"meedget_step\"]")
    # assert current_step_label_2.text == "Шаг: 2 из 4"
    # "to check in 'back button' is present"
    # back_button = browser.find_element(By.XPATH, "//div[@step=\"2\"]//a[contains(@class, \"meedget_back\")]")
    # assert back_button.is_displayed(), "Back button is not displayed"
    # back_button.click()
    # # "to check if the first option is still selected"
    # # if not first_level_complexity.is_selected():
    # #     first_level_complexity.click()
    # assert current_step_label_1.text == "Шаг: 1 из 4"
    # "to close modal window and to check if it is closed"
    # close_modal_window_button = browser.find_element(By.CLASS_NAME, "meedget_close_link")
    # close_modal_window_button.click()
    # assert receive_an_offer_window.is_displayed() == False

    # while True:
    #     pass


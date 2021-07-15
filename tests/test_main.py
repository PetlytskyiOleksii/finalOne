from constants import urls
from constants.urls import URLS
from pages.pages import Pages
from pages.stim_modal_window import StimModalWindow
from pages.page import Page
import pytest


@pytest.mark.skip
def test_login(browser):
    page = Page(browser)
    page.go_to_url(URLS["BASE_URL"])
    assert page.check_if_login_button_is_present(), " כניסת משתמשים "
    page.click_login_button()
    assert page.check_input_name_field_shows(), "login window is not present"
    page.input_name("petlytslyi")
    page.input_password("Manchester17")
    page.click_submit_login_button()
    while True:
        pass


def test_registration(browser):
    page = Page(browser)
    page.go_to_url(URLS["BASE_URL"])
    page.click_registration_button()
    while True:
        pass


@pytest.mark.skip
def test_order_selling_site_modal_window(browser):
    page = Page(browser)
    pages = Pages(browser)
    page.go_to_url(urls.URLS["BASE_URL"])
    page.scroll_page()
    assert page.check_order_selling_site_button_present(), "Order selling site is not displayed"
    page.click_order_selling_site_button_present()
    assert pages.check_order_site_modal_window_present(), "Order selling site modal window is not displayed"
    pages.click_order_button()
    assert pages.check_required_fields_warnings_show() == 2, "less then 2 warnings were showed"
    pages.input_name("test name")
    pages.click_order_button()
    assert pages.check_required_fields_warnings_show() == 1, "less then 1 warning was showed"
    pages.input_phone_number("+1111111111")
    pages.click_order_button()
    assert pages.check_success_order_block_shows(), "success order block is not present"
    pages.close_order_modal_window()
    # while True:
    #     pass



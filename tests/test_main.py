from constants import urls
from constants.urls import URLS
from pages.pages import Pages
from pages.stim_modal_window import StimModalWindow
from pages.tariff_modal_window import TariffModalWindow
from pages.page import Page
import pytest


@pytest.mark.skip
def test_tariff_modal_window(browser):
    page = Page(browser)
    modal_window = TariffModalWindow(browser)
    page.go_to_url()
    assert page.check_if_traffic_button_text_correct(), "tariff button does not exist"
    page.open_modal_window()
    assert modal_window.check_modal_window_shows(), "Modal window does not exist"
    assert modal_window.check_current_step("1") == "Шаг: 1 из 4"
    assert modal_window.check_next_step_button_present(), "Next step button is not present"
    modal_window.select_the_first_option("490 BYN")
    modal_window.click_next_step_button()
    assert modal_window.check_current_step("2") == "Шаг: 2 из 4"
    modal_window.click_previous_button(), "previous button does not exist"
    assert modal_window.check_current_step("1") == "Шаг: 1 из 4"
    modal_window.close_modal_window()
    assert not modal_window.check_modal_window_shows()


@pytest.mark.skip
def test_stim_modal_window(browser):
    page = Page(browser)
    stim_modal_window = StimModalWindow(browser)
    page.go_to_url()
    page.scroll_page()
    page.click_stim_rb_rf_button()
    assert stim_modal_window.check_if_stim_modal_shows(), "Stim modal window is missed"
    assert stim_modal_window.close_stim_modal_window()


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



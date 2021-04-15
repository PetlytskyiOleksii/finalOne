from constants.urls import URLS
from pages.modal_window import ModalWindow
from pages.main_page import MainPage


# def test_tariff_modal_window(browser):
#     main_page = MainPage(browser)
#     modal_window = ModalWindow(browser)
#     main_page.open_main_page(URLS["BASE_URL"])
#     assert main_page.to_check_if_traffic_button_text_correct(), "Traffic button does not exist"
#     main_page.open_modal_window()
#     assert modal_window.to_check_modal_window_shows(), "Modal window does not exist"
#     assert modal_window.to_check_current_step("1") == "Шаг: 1 из 4"
#     assert modal_window.to_check_next_step_button_present(), "Next step button is not present"
#     modal_window.select_the_first_option("490 BYN")
#     modal_window.click_next_step_button()
#     assert modal_window.to_check_current_step("2") == "Шаг: 2 из 4"
#     modal_window.click_previous_button(), "previous button does not exist"
#     assert modal_window.to_check_current_step("1") == "Шаг: 1 из 4"
#     modal_window.close_modal_window()
#     assert not modal_window.to_check_modal_window_shows()


def test_stim_rb_rf_modal_window(browser):
    main_page = MainPage(browser)
    main_page.open_main_page(URLS["BASE_URL"])
    main_page.click_stim_rb_rf_button()
    # while True:
    #     pass




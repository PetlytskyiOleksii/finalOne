import json

import pytest
from selenium.webdriver import Chrome


@pytest.fixture
def config():
    with open("tests/config.json") as f:
        config_data = json.load(f)
        return config_data


@pytest.fixture
def browser(config):
    if config["browser"] == "Chrome":
        driver = Chrome("C:\\Users\\opetlytskyi\\PycharmProjects\\finalProject\\drivers\\chromedriverWin.exe")
        # driver = Chrome("/Users/opetlytskyi/finalProject/drivers/chromedriver")
    else:
        raise Exception("browser is not supported")
    driver.implicitly_wait(config["wait_time"])
    driver.maximize_window()
    yield driver
    driver.quit()


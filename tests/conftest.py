import json
import pytest
import platform
from selenium import webdriver
from constants.supported_browsers import SUPPORTED_BROWSERS, CHROME_BROWSER, FIREFOX_BROWSER
from constants.supported_platforms import SUPPORTED_PLATFORMS, LINUX_PLATFORM, WINDOWS_PLATFORM


@pytest.fixture
def define_platform():
    if platform.system() not in SUPPORTED_PLATFORMS:
        raise Exception("this platform is not supporting")
    return platform.system()


@pytest.fixture
def config():
    with open("tests/config.json") as f:
        config_data = json.load(f)
        return config_data


@pytest.fixture
def config_browser(config):
    if "browser" not in config:
        raise Exception("browser is required")
    if config["browser"] in SUPPORTED_BROWSERS:
        return config["browser"]
    raise Exception("browser is not supported")


@pytest.fixture
def config_wait_time(config):
    if "wait_time" not in config:
        raise Exception("wait time is required")
    if type(config["wait_time"]) != int:
        raise Exception("Wait time should be int")
    if 0 < config["wait_time"] <= 10:
        return config["wait_time"]
    raise Exception("wait time should be more then 0 and <= 10")


@pytest.fixture
def browser(config_browser, config_wait_time, define_platform):
    if config_browser == CHROME_BROWSER:
        if define_platform == WINDOWS_PLATFORM:
            driver = webdriver.Chrome("C:\\Users\\opetlytskyi\\PycharmProjects\\finalProject\\drivers\\chromedriverWin.exe")
        elif define_platform == LINUX_PLATFORM:
            driver = webdriver.Chrome("/Users/opetlytskyi/finalProject/drivers/chromedriverMac")
    elif config_browser == FIREFOX_BROWSER:
        if define_platform == WINDOWS_PLATFORM:
            driver = webdriver.Firefox(executable_path="C:\\Users\\opetlytskyi\\PycharmProjects\\finalProject\\drivers\\firefoxdriverWin.exe")
        elif define_platform == LINUX_PLATFORM:
            driver = webdriver.Firefox(executable_path="/Users/opetlytskyi/finalProject/drivers/firefoxdriverMac")
    else:
        raise Exception("browser is not supported")
    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()
    yield driver
    driver.quit()


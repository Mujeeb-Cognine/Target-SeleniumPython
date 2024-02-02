import webbrowser

from selenium.webdriver.chrome.webdriver import WebDriver
from PytestPackage1 import test_SynchroLogin
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get("https://portal.synchrogistics.com/home")
# browser.maximize_window()

# @pytest.fixture()
# def setup_teardown():
#     test_SynchroLogin.test_CustomerLogin()


def test_logo_displayed():
    test_SynchroLogin.test_CustomerLogin()
    browser = webdriver.Chrome()
# Locate the logo element (adjust the locator as needed)
    logo_element = browser.find_element(By.XPATH, "//a[normalize-space()='Logout']")
    # Assert that the logo is displayed
    assert logo_element.is_displayed(), "Logo is not displayed on the website"

#
# def test_LogoutSynchro(test_CustomerLogin):
#     test_SynchroLogin()
#     browser.implicitly_wait(10)
#     browser.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
#
#     time.sleep(3)
#     time.sleep(5)

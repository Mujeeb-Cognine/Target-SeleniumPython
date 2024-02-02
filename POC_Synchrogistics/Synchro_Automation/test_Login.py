import time
import pytest
from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome()
browser.get("https://portal.synchrogistics.com")
browser.maximize_window()

@pytest.fixture()
def test_customer_login():
    browser.implicitly_wait(10)
    try:
        okay = browser.find_element(By.XPATH, "//button[normalize-space()='Okay']")
        okay.click()
    except NoSuchElementException:
        browser.implicitly_wait(5)
        browser.find_element(By.ID, "mat-input-0").send_keys("customer.demo.b1@synchrogistics.com")
        browser.find_element(By.ID, "mat-input-1").send_keys("Synchro@2023")
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Login Successful")
        browser.implicitly_wait(5)
        print(browser.title)
        time.sleep(2)

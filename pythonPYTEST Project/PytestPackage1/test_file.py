import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# To open Synchro website
browser = webdriver.Chrome()
browser.get("https://portal.synchrogistics.com/home")

# Synchro login
# @pytest.fixture()
def test_CustomerLogin():
    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, "//button[normalize-space()='Okay']").click()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.find_element(By.ID, "mat-input-0").send_keys("customer.demo.b1@synchrogistics.com")
    browser.find_element(By.ID, "mat-input-1").send_keys("Synchro@2023")
    # browser.find_element(By.CSS_SELECTOR, "input[role = 'img']").click()
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    # time.sleep(3)
    print("Login Successful")
    browser.implicitly_wait(5)
    print(browser.title)
def test_InHomePage():
    message = browser.title
    URL = browser.current_url
    if message == "Synchrogistics-Customer Portal":
        print("You are in Synchrogistics Home page")
    elif URL == "https://portal.synchrogistics.com/home":
        print("You are in Synchrogistics Home page")
    else:
        print("Login Successful, but you are not in Home page")

def test_LogoutSynchro():
    # browser.implicitly_wait(10)
    # browser.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    # time.sleep(3)
    # ----------------
    # wait = WebDriverWait(browser, 10)
    # element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']")))
    # browser.execute_script("arguments[0].scrollIntoView(true);", element)
    # element.click()
    # # ----------------
    element = browser.find_element(By.XPATH, "//a[normalize-space()='Logout']")
    # browser.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    time.sleep(5)

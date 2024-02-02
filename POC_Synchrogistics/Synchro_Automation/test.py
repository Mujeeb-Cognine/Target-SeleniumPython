import time
import pytest
from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


browser = webdriver.Chrome()
browser.get("https://portal.synchrogistics.com")
browser.maximize_window()

# def test_customer_login():
#     browser.implicitly_wait(10)
#     # browser.implicitly_wait(5)
#     browser.find_element(By.ID, "mat-input-0").send_keys("customer.demo.b1@synchrogistics.com")
#     browser.find_element(By.ID, "mat-input-1").send_keys("Synchro@2023")
#     browser.implicitly_wait(5)
#     browser.find_element(By.XPATH, "//button[@type='submit']").click()
#     print("Login Successful")
#     browser.implicitly_wait(5)
#     print(browser.title)
#     wait = WebDriverWait(browser, 10)
#     logout_element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
#     #     # browser.execute_script("arguments[0].scrollIntoView(true);", element)
#     logout_element.click()
#     # browser.implicitly_wait(5)
#     #     # logout_message = browser.find_element(By.XPATH, "//pre[contains(text(),
#     #     'You have successfully logged out of the Customer P')]")
#     #     # assert logout_message.is_displayed(), "LogOut successful"
#     #     # pass

def test_customer_logout():
    browser.implicitly_wait(10)
    # browser.implicitly_wait(5)
    browser.find_element(By.ID, "mat-input-0").send_keys("customer.demo.b1@synchrogistics.com")
    browser.find_element(By.ID, "mat-input-1").send_keys("Synchro@2023")
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Login Successful")
    browser.implicitly_wait(5)
    print(browser.title)
    # Wait for the 'Logout' element to be clickable
    wait = WebDriverWait(browser, 10)
    logout_element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))

    # Attempt to scroll the 'Logout' button into view
    browser.execute_script("arguments[0].scrollIntoView(true);", logout_element)

    # Try clicking the 'Logout' button
    try:
        logout_element.click()
        print("Logout Successful")

    except ElementClickInterceptedException:
        print("Element Click Intercepted. Trying alternative approach.")
        # Alternative method: JavaScript click if the regular click fails
        browser.execute_script("arguments[0].click();", logout_element)
        time.sleep(2)

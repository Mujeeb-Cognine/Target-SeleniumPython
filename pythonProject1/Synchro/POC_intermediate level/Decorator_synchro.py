import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def login_decorator(func):
    def login():
        driver = webdriver.Chrome()
        driver.get("https://portal.synchrogistics.com")
        print("Login Successful")
        driver.minimize_window()
        driver.implicitly_wait(10)
        driver.maximize_window()
        try:
            Okay = driver.find_element(By.XPATH, "//button[normalize-space()='Okay']")
            Okay.click()
        except NoSuchElementException:
            driver.implicitly_wait(5)
            driver.find_element(By.ID, "mat-input-0").send_keys("customer.demo.b1@synchrogistics.com")
            driver.find_element(By.ID, "mat-input-1").send_keys("Synchro@2023")
            driver.implicitly_wait(5)
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print("Login Successful")
            driver.implicitly_wait(5)
            print(driver.title)

        func(driver)  # Passes the WebDriver instance to the original test function

        driver.quit()  # Closes the WebDriver after the test function completes

    return login


@login_decorator
def test_customer_login(driver):
    # Perform test actions after login using the driver instance passed by the decorator
    driver.implicitly_wait(10)
    Shipment = driver.find_element(By.LINK_TEXT, "Shipment")
    action = ActionChains(driver)
    action.move_to_element(Shipment).click().perform()
    print("Clicked the Shipments button using Decoraor ")
    # Shipment.click()
    time.sleep(2)


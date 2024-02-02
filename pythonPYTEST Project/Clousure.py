import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get("https://portal.synchrogistics.com")
    driver.maximize_window()
    print("1")

    # Login function
    def login():
        driver.implicitly_wait(10)
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
    return login()


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SynchroPortalTest:
    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://portal.synchrogistics.com/home")
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()


class TestCustomerLogin(SynchroPortalTest):
    def test_customer_login(self):
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.XPATH, "//button[normalize-space()='Okay']").click()
        self.browser.implicitly_wait(5)
        self.browser.find_element(By.ID, "mat-input-0").send_keys("customer.demo.b1@synchrogistics.com")
        self.browser.find_element(By.ID, "mat-input-1").send_keys("Synchro@2023")
        self.browser.implicitly_wait(5)
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Login Successful")
        self.browser.implicitly_wait(5)
        print(self.browser.title)

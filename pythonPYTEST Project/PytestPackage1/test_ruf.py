import time
import pytest
from selenium.common import NoSuchElementException
from PytestPackage1 import test_SynchroLogin
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
        try:
            Okay = self.browser.find_element(By.XPATH, "//button[normalize-space()='Okay']")
            Okay.click()
        except NoSuchElementException:
            self.browser.implicitly_wait(5)
            self.browser.find_element(By.ID, "mat-input-0").send_keys("customer.demo.b1@synchrogistics.com")
            self.browser.find_element(By.ID, "mat-input-1").send_keys("Synchro@2023")
            self.browser.implicitly_wait(5)
            self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
            print("Login Successful")
            self.browser.implicitly_wait(5)
            print(self.browser.title)


class TestCustomerLogout(SynchroPortalTest):
    def test_customer_logout(self):
        test_SynchroLogin.test_CustomerLogin()
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        time.sleep(3)
        time.sleep(5)
        pass
#
# # Run the test classes using pytest
# if __name__ == "__main__":
#     pytest.main()

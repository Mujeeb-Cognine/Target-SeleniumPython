import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SynchroPortalTest:
    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://portal.synchrogistics.com/home")
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()


class TestCustomerLogout(SynchroPortalTest):
    def test_customer_logout(self):
        # Perform the logout actions here
        # self.browser.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        self.browser.implicitly_wait(5)

        wait = WebDriverWait(self.browser, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']")))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        self.browser.implicitly_wait(5)
        logout_message = self.browser.find_element(By.XPATH, "//pre[contains(text(),'You have successfully logged out of the Customer P')]")
        assert logout_message.is_displayed(), "LogOut successful"
        pass

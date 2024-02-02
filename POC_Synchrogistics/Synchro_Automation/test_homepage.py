import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote import webelement
import test_Login
from selenium import webdriver
from selenium.webdriver.common.by import By
from Synchro_Automation.test_Login import test_customer_login

browser = webdriver.Chrome()
browser.get("https://portal.synchrogistics.com/home")
browser.maximize_window()


def test_logo():
    pass


class test_loginandhome:
    def test_elements(self):
        test_Login()
    def test_logo(self):
        logo_element = browser.find_element(By.XPATH("//img[@title='Tutorialspoint']"))
        if logo_element.is_displayed():
            print("Logo is present in the Synchrogistics home page")
        else:
            print("Logo is not present in the Synchrogistics home page")
            exit(test_logo())
    def test_home(self):
        home_element = browser.find_element(By.LINK_TEXT, "Home")
        if home_element.is_displayed():
            print("Home element is present in the Synchrogistics home page")
        else:
            print("Home is not present in the Synchrogistics home page")
            exit(self.test_home())
    def test_shipment(self):
        shipment = browser.find_element(By.LINK_TEXT, "Shipment")
        if shipment.is_displayed():
            print("Home element is present in the Synchrogistics home page")
        else:
            print("Home is not present in the Synchrogistics home page")
            exit(self.test_shipment())



#
#     webelement i = browser.find_element(By.XPATH("//img[@title='Tutorialspoint']"));
#     if i == 1:
#         print("Logo is present in the Synchrogistics home page")
#
#     browser.find_element(By.XPATH, "//a[@class='synchro-nav-brand']")
#
#
# def check_exists_by_xpath(xpath):
#     try:
#         webdriver.find_element_by_xpath(xpath)
#     except NoSuchElementException:
#         return False
#     return True

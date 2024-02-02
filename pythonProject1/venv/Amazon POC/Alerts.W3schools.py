import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# using class
class Alerts ():
    def Alerts(self):
        browser = webdriver.Chrome()
        browser.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
        browser.maximize_window()
        time.sleep(2)
        browser.switch_to.frame("iframeResult")

        # Accept Alert
        # browser.find_element(By.XPATH, "/html[1]/body[1]/button[1]").click()
        # browser.switch_to.alert.accept()
        # time.sleep(2)
        # # Dismiss Alert
        # browser.find_element(By.XPATH, "/html[1]/body[1]/button[1]").click()
        # browser.switch_to.alert.dismiss()
        # time.sleep(2)
        # # Alert
        browser.find_element(By.XPATH, "/html[1]/body[1]/button[1]").click()
        time.sleep(1)
        browser.switch_to.alert.send_keys("Manasa Chamarthi")
        time.sleep(1)
        browser.switch_to.alert.accept()
        time.sleep(2)


Execute = Alerts()
Execute.Alerts()

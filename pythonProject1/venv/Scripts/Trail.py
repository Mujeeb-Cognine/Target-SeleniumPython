import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# To open Synchro website
browser = webdriver.Chrome()
browser.get("https://portal.synchrogistics.com")
browser.maximize_window()

# Synchro login
browser.implicitly_wait(10)
# browser.find_element(By.XPATH, "//button[normalize-space()='Okay']").click()
# browser.implicitly_wait(5)
browser.find_element(By.ID, "mat-input-0").send_keys("customer.demo.b1@synchrogistics.com")
browser.find_element(By.ID, "mat-input-1").send_keys("Synchro@2023")
# browser.find_element(By.CSS_SELECTOR, "input[role = 'img']").click()
browser.implicitly_wait(5)
browser.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
print("Login Successful")
browser.implicitly_wait(5)

# browser.implicitly_wait(10)
browser.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
time.sleep(3)
# browser.find_element(By.CSS_SELECTOR, "a[class='f-size-1']").click()
# Wait = WebDriverWait(browser, 10)
# LogoutElement = Wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Logout']")))
# # LogoutElement = Wait.until(EC.presence_of_element_located(browser.find_element(By.XPATH, "//a[normalize-space()='Logout']")))
#
# # browser.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
# LogoutElement.click()
# time.sleep(5)


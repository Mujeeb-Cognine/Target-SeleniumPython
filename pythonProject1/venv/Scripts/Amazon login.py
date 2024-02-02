import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# To open Amazon website
browser = webdriver.Chrome()
browser.get("https://www.amazon.in/")
browser.maximize_window()
time.sleep(5)

# Amazon Signin
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]/span").click()
# time.sleep(3)
browser.find_element(By.ID, "ap_email").send_keys(6281056611)
# time.sleep(2)
browser.find_element(By.XPATH, "//input[@type= 'submit']").click()
# time.sleep(2)
browser.find_element(By.CSS_SELECTOR, "input[name = 'password']").send_keys("Manasa@1425")
# time.sleep(2)
browser.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
# time.sleep(5)

# Placing an order
# Selecting Amazon Devices options from the categories dropdown
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select").click()
time.sleep(2)
dropdown = Select(browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select"))
dropdown.select_by_index(2)
time.sleep(2)







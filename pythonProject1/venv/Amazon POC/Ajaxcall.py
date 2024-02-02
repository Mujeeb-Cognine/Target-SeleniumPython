import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


# To open Amazon website
browser = webdriver.Chrome()
browser.get("https://www.amazon.in/")
time.sleep(2)
browser.maximize_window()



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

# searching for iphone 14 pro
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys("book bus tickets online on ama")
time.sleep(2)
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys(Keys.ARROW_DOWN)
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys(Keys.ENTER)
time.sleep(1)




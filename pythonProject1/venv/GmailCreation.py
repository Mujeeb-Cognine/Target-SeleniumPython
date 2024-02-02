from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("https://accounts.google.com/signup/v2/createaccount?theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp")
browser.maximize_window()

browser.find_element(By.ID, "firstName").send_keys("test")
browser.find_element(By.ID, "lastName").send_keys("name")
delay = 50
browser.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
time.sleep(2)




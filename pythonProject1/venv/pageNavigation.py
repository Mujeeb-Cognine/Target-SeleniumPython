from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://rahulshettyacademy.com/client/auth/login")
browser.find_element(By.LINK_TEXT, "Forgot password?").click()
# browser.find_element(By.CLASS_NAME, "forgot-password-link").click()
browser.maximize_window()

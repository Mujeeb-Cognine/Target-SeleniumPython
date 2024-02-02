import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# PulpLoad.com
browser.get("https://www.plupload.com/examples/")
browser.maximize_window()
time.sleep(2)
element = browser.find_element(By.XPATH, "//div[@id='uploader_buttons']/div/input")
time.sleep(2)
element.send_keys("C:\\Users\Manasa Chamarthi\Pictures\Test.sendKeys.png")
time.sleep(5)






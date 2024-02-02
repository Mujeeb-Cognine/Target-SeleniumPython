import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# To open Amazon website
browser = webdriver.Chrome()
browser.get("https://www.amazon.in/")
browser.maximize_window()
time.sleep(5)


# Selecting Amazon Devices options from the categories dropdown
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select").click()
time.sleep(2)
dropdown = Select(browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select"))
dropdown.select_by_index(2)
time.sleep(2)
# searching for iphone 14 pro
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys("iphone 14 pro 256 gb")
time.sleep(2)
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").click()
time.sleep(1)
# searching for Apple iPhone 14 (256 GB) - (Product) RED
browser.find_element(By.LINK_TEXT, "Apple iPhone 14 (256 GB) - (Product) RED").click()
time.sleep(10)

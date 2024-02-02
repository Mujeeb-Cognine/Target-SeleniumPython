# As part of this, Chrome browser will be opened

# import time
# from selenium import webdriver
# webdriver.Chrome()

# To open a URL (opening amazon)
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.amazon.in")
browser.get("https://www.flipkart.com/")
browser.back()
delay = 5  # seconds

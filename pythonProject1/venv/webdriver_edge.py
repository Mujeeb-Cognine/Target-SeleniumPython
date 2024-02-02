from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException


def display_website(url, A):
    browser = webdriver.Edge()
    browser.get(url)
    delay = A

display_website("https://www.w3schools.com/python/default.asp", 3)
display_website("https://www.amazon.in", 50)

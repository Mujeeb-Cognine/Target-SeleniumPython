from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def display_website(url, a):
    browser = webdriver.Firefox()
    browser.get(url)
    delay = a
    browser.close()

display_website("https://www.w3schools.com/python/default.asp", 3)
display_website("https://www.amazon.in", 50)

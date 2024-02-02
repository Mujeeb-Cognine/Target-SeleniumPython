from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Open the browser
browser = webdriver.Chrome()
browser.maximize_window()

# Load the Amazon website
browser.get("https://www.amazon.in/")

# Find the search bar and enter a query
search_bar = browser.find_element(By.ID, "twotabsearchtextbox")
search_bar.send_keys("laptop")
search_bar.submit()

# Wait for the page to load
time.sleep(2)

# Capture a screenshot and save it as a binary file
browser.save_screenshot("amazon_screenshot.png")

# Read the screenshot file in binary mode
with open("amazon_screenshot.png", "rb") as file:
    screenshot_data = file.read()
    print("Screenshot read as binary:", screenshot_data)

# Write the current URL into a text file
current_url = browser.current_url
with open('amazon_url.txt', 'w') as file:
    file.write(current_url)

# Read the contents of the file
with open('amazon_url.txt', 'r') as file:
    contents = file.read()
    print("Contents of amazon_url.txt:", contents)

# Close the browser
browser.quit()

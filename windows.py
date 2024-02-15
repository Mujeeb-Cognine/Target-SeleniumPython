from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# Navigate to the URL
driver.get("http://yourwebsite.com")
# Get the parent window handle
parent_handle = driver.current_window_handle
# Get all window handles
handles = driver.window_handles
# Iterate through window handles
for handle in handles:
    if handle != parent_handle:
        # Switch to the child window
        driver.switch_to.window(handle)
        print(driver.title)
        driver.close()

# Switch back to the parent window
driver.switch_to.window(parent_handle)




















































Collaborated with QA team to test software quality through manual and automated testing.
Collaborated with product owners to stay current on intended functionality.
Created successful test scripts to manage automated feature testing,
Developed, implemented and maintained automated testware for scripts, functions and programs to boost testing efficiency.
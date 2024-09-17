from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver (assuming Chrome)
driver = webdriver.Chrome()
driver.get("https://www.swiggy.com/")

# Create an instance of ActionChains
actions = ActionChains(driver)

# Find the search bar element by its ID
search_bar = driver.find_element_by_id('location')

# Example actions using ActionChains
actions.move_to_element(search_bar)  # Move to the search bar
actions.click(search_bar)  # Click the search bar
actions.double_click(search_bar)  # Doubleclick the search bar
actions.context_click(search_bar)  # Right click (context click) the search bar

# Click and hold the search bar (not typically used for input fields)
actions.click_and_hold(search_bar)

# Example of sending keys to the search bar
search_bar.send_keys("Hello, World!")  # Directly send keys using element

# Drag and drop the search bar to a target element (assuming target exists)
target = driver.find_element_by_id("target_id")
actions.drag_and_drop(search_bar, target)

# Release the search bar (after click_and_hold)
actions.release(search_bar)

# Perform all actions accumulated in ActionChains
actions.perform()

# Alternatively, you can chain actions together and perform them at once
actions.move_to_element(search_bar).click().send_keys("Hello").perform()

# Close the browser (after your operations are complete)
driver.quit()

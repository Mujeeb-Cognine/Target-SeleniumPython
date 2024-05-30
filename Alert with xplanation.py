from selenium import webdriver

# Start a WebDriver session
driver = webdriver.Chrome()

# Navigate to a webpage with an alert
driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")

# Find and click on the button that triggers an alert
button = driver.find_element_by_xpath("//button[contains(text(),'Click for JS Alert')]")
button.click()

# Switch to the alert
alert = driver.switch_to.alert

# Get the text of the alert
alert_text = alert.text
print("Alert Text:", alert_text)

# Accept the alert (clicking OK)
alert.accept()

# Close the WebDriver session
driver.quit()

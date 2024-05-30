
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assuming you have already initialized the WebDriver (e.g., ChromeDriver)
# If not, you can create a new instance like this:
# driver = webdriver.Chrome(executable_path="path/to/chromedriver.exe")

# Initialize WebDriverWait
wait = WebDriverWait(driver, 10)

# Navigate to the Guru99 demo site
driver.get("https://demo.guru99.com/test/delete_customer.php")

# Enter a customer ID (you can replace "53920" with any valid ID)
driver.find_element(By.NAME, "cusid").send_keys("53920")

# Click the "Submit" button
driver.find_element(By.NAME, "submit").click()

# Wait for the alert to appear
alert = wait.until(EC.alert_is_present())

# Accept the alert (click "OK")
alert.accept()

# Alternatively, you can dismiss the alert (click "Cancel")
# alert.dismiss()

# If you want to send text to a prompt dialog, you can do the following:
# alert.send_keys("Enter the text")
# alert.accept()

# Close the browser (optional)
# driver.quit()

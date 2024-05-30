from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
import time

# Set up the Chrome WebDriver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.browserstack.com/users/sign_up")
time.sleep(3)

# Interact with the web page
driver.find_element(By.ID, "user_full_name").send_keys("hsghgv")
driver.find_element(By.ID, "user_email_login").send_keys("sdfghvc@gmail.com")
driver.find_element(By.ID, "user_password").send_keys("fgh@567")
driver.find_element(By.ID, "user_submit").click()
time.sleep(5)

# Wait for the alert to be present
time.sleep(5)

# Switch to the alert
try:
    alert = driver.switch_to.alert
    alert_message = alert.text
    print(alert_message)
    time.sleep(5)
    alert.accept()
except NoAlertPresentException:
    print("No alert present")

# Close the browser
driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Alert

# driver = webdriver.Chrome() or any other browser

wait = WebDriverWait(Alert.driver, 10)

# Dismiss an alert
alert = wait.until(EC.alert_is_present())
alert.dismiss()

# Accept a confirmation dialog
wait.until(EC.visibility_of_element_located((By.ID, "confirm-dialog")))
alert = Alert.driver.switch_to.alert
alert.accept()

# Send text to a prompt dialog and accept it
wait.until(EC.visibility_of_element_located((By.ID, "prompt-dialog")))
alert = Alert.driver.switch_to.alert
alert.send_keys("Enter the text")
alert.accept()



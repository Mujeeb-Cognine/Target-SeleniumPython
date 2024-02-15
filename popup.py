#Popup

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pynput.mouse import Button, Controller
from selenium.webdriver.chrome.service import Service
# Initialize the WebDriver for Firefox
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.browserstack.com/users/sign_up")
time.sleep(3)
# Sleep is generally not a good practice, better to use explicit waits
time.sleep(1)
# Click on the popup element
driver.find_element(By.ID, "PopUp").click()
# Initialize the mouse controller
mouse = Controller()
# Move the mouse to the specified position and click
mouse.position = (400, 5)
mouse.press(Button.left)
time.sleep(2)
mouse.release(Button.left)
time.sleep(2)
# Close the browser
driver.quit()

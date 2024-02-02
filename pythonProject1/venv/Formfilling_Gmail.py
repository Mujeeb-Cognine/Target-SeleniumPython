# Gmail account creation
# URL "https://accounts.google.com/signup/v2/createaccount?theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp"
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
import time

# browser = Service("/users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(Service=browser)

browser = webdriver.Chrome()
browser.get("https://rahulshettyacademy.com/angularpractice/")
browser.maximize_window()


# ID, Name, CSSselector, Xpath, classname, linkTest
browser.find_element(By.NAME, "email").send_keys("testmail@gmail.com")
time.sleep(3)
browser.find_element(By.ID, "exampleInputPassword1").send_keys("123654aB")
browser.find_element(By.ID, "exampleCheck1").click()

# to create a Xpath, here is the syntax -- //tagname[@attribute = 'value']
# to create a CSS, here is the syntax -- tagname[attribute = 'value'];; #id, .classname 


browser.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("My Name")
browser.find_element(By.XPATH, "//input[@type= 'submit']").click()
time.sleep(3)
message = browser.find_element(By.CLASS_NAME, "alert-success").text
time.sleep(3)
browser.maximize_window()

print(message)

assert 'Success' in message
# Assertion will check for 'Success' in the message




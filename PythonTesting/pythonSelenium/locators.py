import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/Mujeeb Rahaman/Downloads/PythonDocs/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name , linkText
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Mujeeb")
driver.find_element(By.NAME,"email").send_keys("mujeeb7036@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Mujeeb@8143")
driver.find_element(By.CSS_SELECTOR,"input[value='option1']").click()
driver.find_element(By.ID,"exampleCheck1").click()

# Xpath - //tagname[@attribute='value'] -> //input[@type='submit']
# CSS - tagname[attribute='value'] -> //input[@type='submit'], #id, .classname
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

driver.find_element(By.XPATH,"//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("HelloWorld!")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
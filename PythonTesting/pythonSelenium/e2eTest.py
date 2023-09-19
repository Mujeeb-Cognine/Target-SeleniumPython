from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/Mujeeb Rahaman/Downloads/PythonDocs/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
# a[href*='shop'] -css selectir or //a[contains(@href,'shop')] -xpath

products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()
        break

driver.find_element(By.CLASS_NAME,"navbar-toggler-icon").click()
driver.find_element(By.CSS_SELECTOR,"a[class$='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("India")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()


driver.find_element(By.CLASS_NAME,"checkbox-primary").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
successMessage = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in successMessage
driver.close()


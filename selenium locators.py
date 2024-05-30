from selenium import webdriver
from selenium.webdriver.common.by import By

exe_path = "C:\\Selenium\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=exe_path)

driver.get("https://demoqa.com/")

driver.get("https://demoqa.com/registration")
driver.find_element(By.ID, "firstName")

driver.get("https://demoqa.com/registration")
driver.find_element(By.NAME, "gender")

driver.get("https://demoqa.com/registration")
driver.find_element(By.CLASS_NAME, "practice-form-wrapper")

driver.get("https://demoqa.com/registration")
driver.find_element(By.LINK_TEXT, "Home")

driver.find_element(By.PARTIAL_LINK_TEXT, "Ho")

driver.get("https://demoqa.com/registration")
list_of_elements = driver.find_elements(By.TAG_NAME, "a")

driver.get("https://demoqa.com/registration")
driver.find_element(By.CSS_SELECTOR, "input[id='userName']")

driver.get("https://demoqa.com/registration")
driver.find_element(By.XPATH, "//input[@id='userName']")


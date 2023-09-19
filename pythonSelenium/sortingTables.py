from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/Mujeeb Rahaman/Downloads/PythonDocs/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserSortedveggies = []
# click on column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
# collect all veggie names -> BrowserSortedveggieList
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browserSortedveggies.append(ele.text)

originalBrowserSortedList = browserSortedveggies.copy()
# Sort this BrowserSortedveggieList => newSortedList
browserSortedveggies.sort()
# BrowserSortedveggieList == newSortedList
assert browserSortedveggies == originalBrowserSortedList


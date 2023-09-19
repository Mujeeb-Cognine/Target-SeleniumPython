from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome driver - Chrome browser
# service_obj = Service() #seleniumManager
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://rahulshettyacademy.com")

# -- Chrome
service_obj = Service("/Users/Mujeeb Rahaman/Downloads/PythonDocs/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# -- Firefox

# service_obj = Service("/Users/Mujeeb Rahaman/Downloads/PythonDocs/geckodriver-v0.33.0-win64/geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

# -- Edge

# service_obj = Service("/Users/Mujeeb Rahaman/Downloads/PythonDocs/msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
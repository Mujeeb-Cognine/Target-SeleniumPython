import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
print("testing add to cart")
item="Sauce Labs Bolt T-Shirt"
add_to_cart_btns = driver.find_element(By.CLASS_NAME, "btn_inventory")
# add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
# for btns in add_to_cart_btns[2:3]:
#     btns.click()
time.sleep(30)
driver.minimize_window()
driver.close()

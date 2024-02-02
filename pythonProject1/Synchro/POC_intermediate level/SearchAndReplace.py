from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def search_and_replace(search_query, replace_text):
    driver.get("https://www.amazon.in")
    driver.maximize_window()

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    time.sleep(2)
    updated_query = search_query.replace("DELL", replace_text)
    search_box.send_keys(updated_query)
    search_box.submit()
    time.sleep(2)


search_and_replace("DELL laptop", "head phones for")

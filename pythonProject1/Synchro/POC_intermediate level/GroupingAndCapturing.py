import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def get_titles(source_code):
    pattern = r'<span class="a-size-medium a-color-base a-text-normal">(.*?)</span>'
    titles = re.findall(pattern, source_code)
    return titles


def extract_titles():
    driver.get("https://www.amazon.in")
    driver.maximize_window()

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("laptop")
    search_box.submit()
    time.sleep(2)

    titles_text = driver.page_source
    titles = get_titles(titles_text)
    print(titles)


extract_titles()

# Clousers, Reduce, Decorators and Pattern Matching

from selenium import webdriver
from selenium.webdriver.common.by import By
from functools import reduce
import re


# Create a function to initialize the WebDriver
def initialize_driver():
    return webdriver.Chrome()


# Decorator to manage driver initialization and quitting
def manage_driver(func):
    def wrapper(*args, **kwargs):
        driver = initialize_driver()
        func(driver, *args, **kwargs)
        driver.quit()

    return wrapper


# Function to search for a product on Amazon
@manage_driver
def search_amazon(driver, search_term):
    driver.get("https://www.amazon.in")
    driver.maximize_window()

    search_input = driver.find_element(By.ID, "twotabsearchtextbox")
    search_input.send_keys(search_term)
    search_input.submit()

    product_titles = driver.find_elements(By.CSS_SELECTOR, "span.a-text-normal")
    titles_text = list(map(lambda x: x.text, product_titles))

# Using reduce to concatenate titles
    concatenated_titles = reduce(lambda x, y: f"{x}\n{y}", titles_text)
    print(concatenated_titles)

# Using pattern matching (regex) to extract relevant information
#     pattern = r'\$\d+\.\d+'
    pattern = r'(\d+\.\d+)\s*(cm|cms)'

    matches = re.findall(pattern, concatenated_titles)
    print("Pattern Matches:")
    for match in matches:
        print(match)


# Search for a specific product on Amazon using the function
search_amazon("laptop")

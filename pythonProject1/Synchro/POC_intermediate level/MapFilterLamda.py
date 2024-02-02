from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Define your search term
search_term = "laptop"

# Initialize the Chrome WebDriver
browser = webdriver.Chrome()

# Open Amazon website
browser.get("https://www.amazon.in")
browser.maximize_window()

# Find the search bar and input the search term
search_input = browser.find_element(By.ID, "twotabsearchtextbox")
search_input.send_keys(search_term)
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
# (Add explicit waits or more robust handling based on your use case)
browser.implicitly_wait(5)

# Get all the product titles using map and lambda
product_titles = browser.find_elements(By.CSS_SELECTOR, "span.a-text-normal")
titles_text = list(map(lambda x: x.text, product_titles))

# Filter out empty titles (if any)
filtered_titles = list(filter(lambda x: x.strip() != "", titles_text))

# Print the filtered product titles
for title in filtered_titles:
    print(title)

# Close the browser window
browser.quit()


import time
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.dentganga.com/")
time.sleep(3)
#open the all button
opennav= driver.find_element(By.CLASS_NAME,"openbtn").click()
time.sleep(3)
# Find the sidenav element
# try:
#     # Find the sidebar navigation element with the class name "sidenav"
#     sidenav = driver.find_element(By.CLASS_NAME, "sidenav")
#     driver.execute_script("window.scrollBy(0, 500);")
#     # Find the specific option within the sidenav
#     # Wait for the specific option to be visible
#     specific_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     (By.XPATH, "//div[contains(@class, 'sidenavRow click_to_child') and contains(text(), 'Dental Hygiene')]")))
#     # specific_option = sidenav.find_element(By.XPATH, "//div[contains(@class, 'sidenavRow click_to_child') and contains(text(), 'Dental Hygiene')]")
#     # Click on the specific option
#     specific_option.click()
#     time.sleep(3)
# # Close the sidebar navigation
#     close_button = driver.find_element(By.ID, "closeBtn")
#     close_button.click()
# except Exception as e:
#     print("An error occurred:", str(e))
close_button = driver.find_element(By.ID, "closeBtn").click()
#closing the notification popup
option_notificatins=driver.find_element(By.CLASS_NAME,"truepush_optin_notifications")
close= driver.find_element(By.CLASS_NAME,"tp_btn_default").click()
# Look for the class
search_box = driver.find_element(By.CLASS_NAME, "ais-SearchBox-input")
# Write what we be searched#
search_box.send_keys('Equipment')
time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")
# Submit the text
search_box.send_keys(Keys.RETURN)
# product = driver.find_element(By.XPATH, "//div[@class='Dental Spare Parts 3 Way 3w']")
# product.click()
length=1
while(True):
    search_box.send_keys(Keys.BACK_SPACE)
    if(length == len('Equipment')):
        break
    length += 1
time.sleep(4)
element = driver.find_element(By.XPATH, "//i[contains(@class, 'far') and contains(@class, 'fa-times-circle') and contains(@class, 'fa-2x')]")
element.click()
time.sleep(3)
try:
    # Wait for the element to be clickable
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'https')]"))
    )

    # Scroll into view if needed (using JavaScript)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Click the element
    element.click()

    # Add any additional actions after clicking the element if needed

except Exception as e:
    print(f"Exception occurred: {str(e)}")
    # Handle exception as needed, such as logging or retrying

finally:
    # Optionally, you can quit the driver at the end of your script
    driver.quit()
cart_quantity_element = driver.find_element(By.XPATH,"//span[contains(@class, 'cart-number') and contains(@class, 'cart_qty_count')]")
# Now you can interact with the cart quantity element as needed
# For example, you can retrieve its text:
cart_quantity = cart_quantity_element.text
print("Cart Quantity:", cart_quantity)
driver.get("https://www.dentganga.com")  # Replace with the URL of the webpage
vatech_accessories_link = driver.find_element(By.LINK_TEXT, "Vatech Product Accessories")
# Get the URL from the href attribute
url = vatech_accessories_link.get_attribute("href")
# Navigate to the URL
driver.get(url)
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)
#opening the cart
cart = driver.find_element(By.XPATH, '//button[contains(@onclick, "window.location.href=\'https://www.dentganga.com/cart\';")]').click()
time.sleep(3)


# elements = driver.find_element(By.CLASS_NAME, "ais-InfiniteHits-loadMore")
# time.sleep(2)
# element.click()
# time.sleep(3)
# search_box.clear()
# time.sleep(3)
# search_box.send_keys(Keys.RETURN)
# time.sleep(3)

# scroll=driver.find_element(By.ID,value:"")


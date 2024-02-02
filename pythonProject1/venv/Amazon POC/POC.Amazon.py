import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


# To open Amazon website
browser = webdriver.Chrome()
browser.get("https://www.amazon.in/")

time.sleep(2)
browser.maximize_window()


# Amazon Signin
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]/span").click()
time.sleep(3)
browser.find_element(By.ID, "ap_email").send_keys(6281056611)
time.sleep(2)
browser.find_element(By.XPATH, "//input[@type= 'submit']").click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, "input[name = 'password']").send_keys("Manasa@1425")
time.sleep(2)
browser.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
time.sleep(5)

# Selecting Amazon Devices options from the categories dropdown
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select").click()
time.sleep(2)
dropdown = Select(browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select"))
dropdown.select_by_index(2)
time.sleep(2)


# getting the current page
ParentPage = browser.current_window_handle
# # searching for iphone 14 pro
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys("iphone 14 pro 256 gb red")
time.sleep(2)
browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").click()
time.sleep(1)


# searching for Apple iPhone 14 (256 GB) - (Product) RED
# using Action class
browser.find_element(By.LINK_TEXT, "Apple iPhone 14 (256 GB) - (Product) RED").send_keys(Keys.ENTER)
browser.maximize_window()

# using window handle methods
# Adding to cart
time.sleep(2)
AllPages = browser.window_handles
for CurrentPage in AllPages:
    if CurrentPage != ParentPage:
        browser.switch_to.window(CurrentPage)
        time.sleep(2)
        # Radio button
        # browser.find_element(By.CSS_SELECTOR, 'i[class="a-icon a-accordion-radio a-icon-radio-inactive"]').click()
        time.sleep(2)

# Scroll
element = browser.find_element(By.ID, "add-to-cart-button")
browser.execute_script("arguments[0].scrollIntoView();", element)
browser.find_element(By.ID, "add-to-cart-button").click()
time.sleep(2)

# Wait
wait = WebDriverWait(browser, 20)
# set a max wait time
cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='attach-sidesheet-view-cart-button']"))).click()
# set the dynamic wait, which should end the wait early (ie not 20 seconds)
time.sleep(2)


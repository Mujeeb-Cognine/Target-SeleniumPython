import time
from selenium.common.exceptions import NoSuchElementException
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
#open the application
driver.get("https://www.dentganga.com/")
time.sleep(3)
#open the all button
opennav= driver.find_element(By.CLASS_NAME,"openbtn").click()
time.sleep(3)
#closing the all button
close_button = driver.find_element(By.ID, "closeBtn").click()
#closing the notification popup
option_notificatins=driver.find_element(By.CLASS_NAME,"truepush_optin_notifications")
close= driver.find_element(By.CLASS_NAME,"tp_btn_default").click()
# Look for the searchbox class
search_box = driver.find_element(By.CLASS_NAME, "ais-SearchBox-input")
# Write what we be searched
search_box.send_keys('Equipment')
time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")
# Submit the text
search_box.send_keys(Keys.RETURN)
#by using the while loop we removing the search text
length=1
while(True):
    search_box.send_keys(Keys.BACK_SPACE)
    if(length == len('Equipment')):
        break
    length += 1
time.sleep(4)
#Getting back to homepage by clicking on cancel button
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, "closesearchresult"))).click()
time.sleep(3)
#Selecting one item from the application
element=driver.find_element(By.XPATH, '//a[@class="shadow_image" and contains(@aria-label, "GC Tooth Mouse Vanilla Flavor")]/img')
driver.execute_script("arguments[0].click();", element)
time.sleep(3)
#add to cart
button = driver.find_element(By.ID, "cart_button_product")
# Click the button
button.click()
time.sleep(3)
#navigate to hamepage
homepage=driver.find_element(By.CLASS_NAME, "navbar-brand").click()
time.sleep(3)
#selecting the taskbar item
taskbaritem = driver.find_element_by_xpath("//a[@href='https://www.dentganga.com/vatech-product-accessories']").click()
time.sleep(3)



# element.click()
# # time.sleep(3)
# # link_element = driver.find_element(By.XPATH, '//a[@class="shadow_image" and contains(@aria-label, "GC Tooth Mouse Vanilla Flavor")]/img')
# # link_element.click()
# # time.sleep(3)
# # add_to_cart=driver.find_element(By.ID,"cart_button_product").click()
# # time.sleep(3)
# # homepage=driver.find_element(By.CLASS_NAME, "navbar-brand").click()
# # time.sleep(3)
# wait = WebDriverWait(driver, 20)
# cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.trans-btn")))
# # cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, 'YOUR_XPATH_HERE')))
# # cart_button.click()
# # iframe = driver.find_element_by_css_selector("iframe_selector")
# # driver.switch_to.frame(iframe)
# # # Scroll to the button
# # cart_button.send_keys(Keys.END)
# # # Now click the button
# # cart_button.click()
# # #scroll into the view:
# # cart_buttons = driver.find_element_by_css_selector("button.trans-btn")
# # driver.execute_script("arguments[0].scrollIntoView();", cart_button)
# # cart_buttons.click()
# # #clicking on cart
# # cart_button = driver.find_element_by_css_selector("button.trans-btn")
# # driver.execute_script("arguments[0].click();", cart_button)
#

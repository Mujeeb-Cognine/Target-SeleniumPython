import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Already used iFrames in alerts, this is another example for iFrames
# Trying to click on the Tutorials button, which is located in 2 nested iframes.

browser = webdriver.Chrome()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
browser.maximize_window()
time.sleep(2)
browser.switch_to.frame("iframeResult")
iframe_src = browser.find_element(By.CSS_SELECTOR, "iframe[src='/default.asp']")
browser.switch_to.frame(iframe_src)

browser.find_element(By.ID, 'navbtn_tutorials').click()
time.sleep(2)


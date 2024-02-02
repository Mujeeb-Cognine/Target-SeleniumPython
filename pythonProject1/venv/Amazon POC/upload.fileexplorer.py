import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
import pynput

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("https://www.plupload.com/examples/")
browser.maximize_window()
browser.find_element(By.ID, "uploader_browse").click()
time.sleep(2)

Keyboard = Controller()
Keyboard.type("C:\\Users\Manasa Chamarthi\Pictures\Test.sendKeys.png")
time.sleep(2)
Keyboard.press(Key.enter)
Keyboard.release(Key.enter)
time.sleep(2)


import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class DemoDragDrop():
    def Drag_Drop(self):
        browser = webdriver.Chrome()
        browser.get("https://jqueryui.com/droppable/")
        browser.maximize_window()
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        ElementDrag = browser.find_element(By.ID, "draggable")
        ElementDrop = browser.find_element(By.ID, "draggable")
        ActionChains(browser).drag_and_drop(ElementDrag, ElementDrop).perform()

        time.sleep(5)

dd = DemoDragDrop()
dd.Drag_Drop()



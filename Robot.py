from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
class Robot:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def move_mouse_to_element(self, element):
        self.actions.move_to_element(element).perform()

    def click_element(self, element):
        self.actions.click(element).perform()

    def double_click_element(self, element):
        self.actions.double_click(element).perform()

    def right_click_element(self, element):
        self.actions.context_click(element).perform()

    def drag_and_drop(self, source_element, target_element):
        self.actions.drag_and_drop(source_element, target_element).perform()

    def send_keys_to_element(self, element, keys):
        element.send_keys(keys)

    def press_key(self, key):
        self.actions.key_down(key).perform()

    def release_key(self, key):
        self.actions.key_up(key).perform()

    def perform_actions(self):
        self.actions.perform()

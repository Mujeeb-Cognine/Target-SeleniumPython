import time
import pytest
from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.get("https://portal.synchrogistics.com")
browser.maximize_window()


@pytest.fixture()
def test_customer_login():
    browser.implicitly_wait(10)
    try:
        Okay = browser.find_element(By.XPATH, "//button[normalize-space()='Okay']")
        Okay.click()
    except NoSuchElementException:
        browser.implicitly_wait(5)
        browser.find_element(By.ID, "mat-input-0").send_keys("customer.demo.b1@synchrogistics.com")
        browser.find_element(By.ID, "mat-input-1").send_keys("Synchro@2023")
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Login Successful")
        browser.implicitly_wait(5)
        print(browser.title)


def test_customer_Shipment(test_customer_login):
    browser.implicitly_wait(10)
    tools = browser.find_element(By.LINK_TEXT, "Tools")
    actions = ActionChains(browser)
    actions.move_to_element(tools).perform()

    browser.find_element(By.LINK_TEXT, "Quoting").click()
    # Clicking on the LTL option from Mode
    browser.find_element(By.XPATH, "//button[normalize-space()='LTL']").click()
    # browser.implicitly_wait(10)
    # nmfc_dropdown = browser.find_element(By.XPATH, "//div[@class='mat-select-value ng-tns-c70-2' and @id='mat-select-value-3']")
    # nmfc_dropdown = WebDriverWait(browser, 10).until(EC.presence_of_all_element_located((By.XPATH, "//div[@class='mat-select-value ng-tns-c70-2' and @id='mat-select-value-3']")))
    wait = WebDriverWait(browser, 20)
    nmfc_dropdown = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-select-value ng-tns-c70-2' and @id='mat-select-value-3']")))
    # presence_of_all_element_located
    nmfc_dropdown.click()
    options = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located(By.XPATH, "//span[@class = 'mat-option-text']"))
    option_texts = []

    for option_text in option_texts:
        # option_texts.append(option.text)
        print(option_text)
    # print(LIST)

    # # print("able to click the dropdown")
    # # time.sleep(2)
    # NMFC_list = Select(NMFC_dropdown)
    # NMFC_list_options = NMFC_list.options
    #
    # print("NMFC Dropdown options:")
    # for option in NMFC_list_options:
    #     print(option.text)
    time.sleep(1)

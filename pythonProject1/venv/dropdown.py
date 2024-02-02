from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=inflex&mobileBrowserWeblabTreatment=C&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&prevRID=BHJYDHYNJGZSKQPXFGWV&openid.assoc_handle=inflex&openid.mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

wait(driver, 5).until(EC.visibility_of_element_located(
    # (By.XPATH, '//div[@class="cookie-button-wrapper"]')
    (By.CLASS_NAME, "a-dropdown-prompt"))).click()

time.sleep(10)

# #click on specific country from the dropdown
driver.find_element(By.CLASS_NAME, "a-dropdown-prompt")

dropdownlist = driver.find_elements(by=By.CLASS_NAME, value="a-dropdown-prompt")
i = 0
while i < len(dropdownlist):
    if(dropdownlist[i].text == "Albania +355"):
        dropdownlist[i].click()
    i = i+1

time.sleep(20)

driver.maximize_window()

# element = driver.find_element(By.XPATH, '//input[@data-value = "{&quot;stringVal&quot;:&quot;IN&quot;}"]')
# actions = ActionChains(driver)
# actions.move_to_element(element).perform()
#
# wait(driver, 5).until(EC.visibility_of_element_located(
#     (By.XPATH, '//input[@id = "auth-country-picker_9"]'))).click()

from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID,"exampleFormControlSelect1")
    student = (By.CSS_SELECTOR, "input[value='option1']")
    loveIcecreamCheckBox = (By.ID, "exampleCheck1")
    submitButton = (By.XPATH, "//input[@type='submit']")
    alertMessage = (By.CLASS_NAME, "alert-success")
    inputText = (By.XPATH, "(//input[@type='text'])[3]")


    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getStudent(self):
        return self.driver.find_element(*HomePage.student)

    def getIcreamChecBox(self):
        return self.driver.find_element(*HomePage.loveIcecreamCheckBox)

    def getHomeSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getAlertMessage(self):
        return self.driver.find_element(*HomePage.alertMessage)

    def getInputText(self):
        return self.driver.find_element(*HomePage.inputText)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

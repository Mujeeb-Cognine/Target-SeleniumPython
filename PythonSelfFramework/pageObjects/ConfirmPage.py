from selenium.webdriver.common.by import By


class ConfirmPage():

    def __init__(self, driver):
        self.driver = driver

    countryInput = (By.ID,"country")
    indiaCountry = (By.LINK_TEXT,"India")
    termsCheckbox = (By.CLASS_NAME,"checkbox-primary")
    submitButton = (By.XPATH,"//input[@type='submit']")
    successText = (By.CLASS_NAME,"alert-success")


    def getCountryInput(self):
        return self.driver.find_element(*ConfirmPage.countryInput)

    def getIndia(self):
        return  self.driver.find_element(*ConfirmPage.indiaCountry)

    def getTermsCheckbox(self):
        return self.driver.find_element(*ConfirmPage.termsCheckbox)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getSuccessText(self):
        return  self.driver.find_element(*ConfirmPage.successText)
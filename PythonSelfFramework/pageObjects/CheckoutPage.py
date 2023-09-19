from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage():

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.XPATH,"//h4[@class='card-title']/a")
    addCartButton = (By.XPATH,"//*[@class='card-footer']/button")
    menuIcon = (By.CLASS_NAME,"navbar-toggler-icon")
    checkoutButton = (By.CSS_SELECTOR, "a[class$='btn-primary']")
    checkoutConfirm = (By.XPATH,"//button[@class='btn btn-success']")

    def getCards(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getCardTitle(self):
        return  self.driver.find_element(*CheckoutPage.cardTitle)

    def getAddCartButton(self):
        return self.driver.find_elements(*CheckoutPage.addCartButton)

    def getMenuIcon(self):
        return  self.driver.find_element(*CheckoutPage.menuIcon)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def getCheckoutConfirm(self):
        self.driver.find_element(*CheckoutPage.checkoutConfirm).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage


import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from tests.utilitites.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        homePage =  HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("Getting all card titles")

        checkoutPage.getCards()

        for productTitle in checkoutPage.getCards():
            productName = checkoutPage.getCardTitle().text
            log.info(productName)
            if productName == "Blackberry":
                productTitle.checkoutPage.getAddCartButton().click()
                break

        checkoutPage.getCheckoutButton().click()
        confirmPage = checkoutPage.getCheckoutConfirm()
        log.info("Entering country name as India")

        confirmPage.getCountryInput().send_keys("India")

        self.verifyLinkPresense("India")

        confirmPage.getIndia().click()
        confirmPage.getTermsCheckbox().click()
        confirmPage.getSubmitButton().click()
        successMessage = confirmPage.getSuccessText().text
        log.info("Text received from application " + successMessage)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in successMessage





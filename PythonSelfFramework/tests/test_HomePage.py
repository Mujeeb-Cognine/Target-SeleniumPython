import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from tests.utilitites.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("First Name is " + getData["firstname"])
        homePage.getName().clear()
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys(getData["password"])
        homePage.getStudent().click()
        homePage.getIcreamChecBox().click()
        self.selectOptionByText(homePage.getGender(),getData["gender"])
        homePage.getHomeSubmitButton().click()
        message = homePage.getAlertMessage().text
        print(message)
        assert "Success" in message
        homePage.getInputText().send_keys(getData["myMessage"])
        homePage.getInputText().clear()
        self.driver.refresh()

    # @pytest.fixture(params = HomePageData.test_HomePage_data)
    @pytest.fixture(params = HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        return request.param
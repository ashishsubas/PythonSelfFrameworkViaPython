import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log= self.getLogger()
        homepage= HomePage(self.driver)
        log.info("The first name is"+getData["firstname"] )
        homepage.getName().send_keys(getData["firstname"])
        log.info("The emailId is" + getData["emailId"])
        homepage.getEmail().send_keys(getData["emailId"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.tickCheckbox().click()
        self.selectOptionBytext(homepage.getGender(),getData["gender"])
        homepage.finalsubmit().click()

        AlertText = homepage.getFinalText().text
        log.info("The text displayed on the page after submission is" + AlertText)
        assert ("Success" in AlertText)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    def getData(self,request):
        return request.param
    
import pytest
from selenium import webdriver
import time

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i = 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutpage.getCardFooter()[i].click()

        checkOutpage.clickCheckoutBtn().click()
        confirmpage = checkOutpage.getItemsCheckList()
        confirmpage = ConfirmPage(self.driver)
        log.info("Entering Country name as ind")
        confirmpage.getCountry().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmpage.pickCountry().click()
        confirmpage.selectCheckbox().click()
        confirmpage.confirmation().click()
        successtext = confirmpage.textCapture().text
        log.info("The text received from Application is" + successtext)
        assert "Success! Thank you!" in successtext
        self.driver.get_screenshot_as_file("screen.png")

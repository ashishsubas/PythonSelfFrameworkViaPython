from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.XPATH, "div/button")
    checkoutButton = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    itemslist = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def clickCheckoutBtn(self):
        return self.driver.find_element(*CheckOutPage.checkoutButton)

    def getItemsCheckList(self):
        self.driver.find_element(*CheckOutPage.itemslist).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

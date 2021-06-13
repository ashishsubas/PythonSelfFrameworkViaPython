from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

#self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
    country= (By.ID, "country")
    selectCountry= (By.LINK_TEXT, "India")
    checkbox= (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    confirm= (By.CSS_SELECTOR, "input[class*='btn-success']")
    captureText= (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def pickCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def selectCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def confirmation(self):
        return self.driver.find_element(*ConfirmPage.confirm)

    def textCapture(self):
        return self.driver.find_element(*ConfirmPage.captureText)
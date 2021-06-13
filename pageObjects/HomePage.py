from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop=(By.CSS_SELECTOR,"a[href*='shop']")
    name=(By.CSS_SELECTOR, "[name='name']")
    email=(By.NAME,"email")
    password=(By.ID,"exampleInputPassword1")
    checkbox=(By.CSS_SELECTOR,"#exampleCheck1")
    genderbox=(By.ID,"exampleFormControlSelect1")
    submit=(By.XPATH,"//*[@class='btn btn-success']")
    finaltext=(By.CSS_SELECTOR,"[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutpage = CheckOutPage(self.driver)
        return checkOutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def tickCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.genderbox)

    def finalsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getFinalText(self):
        return self.driver.find_element(*HomePage.finaltext)
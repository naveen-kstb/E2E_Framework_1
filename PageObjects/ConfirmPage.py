from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    cardCountry = (By.ID, "country")
    # driver.find_element(By.CLASS_NAME, "suggestions").click()
    cardSuggestions = (By.XPATH, "//div[@class='suggestions']")
    # driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
    cardCheckBox = (By.XPATH, "//label[@for='checkbox2']")

    # driver.find_element(By.XPATH, "//input[@type='submit']").click()
    Submit = (By.XPATH, "//input[@type='submit']")

    # driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    Alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.cardCountry)

    def getSuggestions(self):
        return self.driver.find_element(*ConfirmPage.cardSuggestions)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.cardCheckBox)

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.Submit)

    # driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

    def getAlert(self):
        return self.driver.find_element(*ConfirmPage.Alert)



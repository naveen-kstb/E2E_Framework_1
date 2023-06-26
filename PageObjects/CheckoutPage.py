from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardtitles = (By.XPATH, "//div[@class='card h-100']")
    # driver.find_element(By.XPATH, "div/button").click()
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    # driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    cardPrimary = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    cardCheckoutItems = (By.XPATH, "//button[@class='btn btn-success']")
    # driver.find_element(By.ID, "country").send_keys("India")


    def getcardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardtitles)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getCardPrimary(self):
        return self.driver.find_element(*CheckOutPage.cardPrimary)

    def CheckoutItems(self):
        return self.driver.find_element(*CheckOutPage.cardCheckoutItems)



import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from test.Baseclass import Baseclass
from PageObjects.HomePage import HomePage


class TestOne(Baseclass):

    def test_e2e(self):
        logging = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()  # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        checkOutPage = CheckOutPage(self.driver)
        logging.info("getting all the card titles")
        cards = checkOutPage.getcardTitles()
        confirmPage = ConfirmPage(self.driver)

        i = -1
        for product in cards:
            i = i + 1
            productName = product.find_element(By.XPATH, "div/h4/a").text
            logging.info(productName)
            if productName == "Samsung Note 8":
                checkOutPage.getCardFooter()[i].click()

                # driver.find_element(By.XPATH, "//button[@class='btn btn-info'] [2]").click()
        checkOutPage.getCardPrimary().click()
        checkOutPage.CheckoutItems().click()
        logging.info("Entering country name as ind")
        confirmPage.getCountry().send_keys("India")
        self.VerifyLinkPresence("India")
        confirmPage.getSuggestions().click()  # driver.find_element(By.LINK_TEXT, "India"),click()
        confirmPage.getCheckBox().click()
        confirmPage.getSubmit().click()
        Success = confirmPage.getAlert().text
        message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        logging.info("Text received in application is"+message)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in Success
        self.driver.close()

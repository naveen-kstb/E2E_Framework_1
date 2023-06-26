import time

import pytest

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from test.Baseclass import Baseclass


class TestHomePage(Baseclass):

    def test_formSubmission(self, getData):
        logging = self.getLogger()
        # logging.info("first name is " + getData["firstname"])
        homepage = HomePage(self.driver)
        # homepage.shopItems().click()
        # time.sleep(2)
        # homepage.getHome().click()
        homepage.getName().send_keys(getData["firstname"])
        time.sleep(5)
        homepage.getEmail().send_keys(getData["email"])
        time.sleep(5)
        logging.info("email is " + getData["email"])
        homepage.getID().send_keys("hello")
        homepage.geticecream().click()
        homepage.getgender().click()
        self.selectOptionByText(homepage.getgender(), getData["gender"])
        time.sleep(5)
        logging.info("gender is " + getData["gender"])
        homepage.getStatus().click()
        homepage.getdob().send_keys("19-01-2000")
        homepage.getsubmit().click()
        message = homepage.getclassname().text

        # message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)
        assert "Success" in message

    # @pytest.fixture(params=[("Naveen", "hello@gmail.com", "Male"), ("Saisha", "hello@gmail.com", "Female")])
    @pytest.fixture(params=HomePageData.getTestData("Testcase 1"))
    def getData(self, request):
        return request.param

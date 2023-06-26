from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    home = (By.XPATH, "//a[contains(text(),'Home')]")
    Name = (By.CSS_SELECTOR, "input[name='name']")
    Email = (By.NAME, "email")
    ID = (By.ID, "exampleInputPassword1")
    IceCream = (By.ID, "exampleCheck1")
    status = (By.CSS_SELECTOR, "#inlineRadio1")
    Gender = (By.ID, "exampleFormControlSelect1")
    Status = (By.ID, "inlineRadio1")
    DOB = (By.XPATH, "//*[@name='bday']")
    Submit = (By.XPATH, "//*[@type= 'submit']")
    ClassName = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    def getHome(self):
        return self.driver.find_element(*HomePage.home)

    def getName(self):
        return self.driver.find_element(*HomePage.Name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.Email)

    def getID(self):
        return self.driver.find_element(*HomePage.ID)

    def geticecream(self):
        return self.driver.find_element(*HomePage.IceCream)

    def getgender(self):
        return self.driver.find_element(*HomePage.Gender)

    def getStatus(self):
        return self.driver.find_element(*HomePage.status)

    def getstatus(self):
        return self.driver.find_element(*HomePage.Status)

    def getdob(self):
        return self.driver.find_element(*HomePage.DOB)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.Submit)

    def getclassname(self):
        return self.driver.find_element(*HomePage.ClassName)

from selenium import webdriver
from selenium.webdriver.common.by import By

from lib.reporter import Reporter
from lib.selenium_extensions import (Click, findElementBy, isDisplayed,
                                     isEnabled, isSelected, sendKeys,
                                     waitUntilDisplay, waitUntilExistInDOM,
                                     waitUntilHidden)


class LoginPage:
    
    
    driver = None

    def __init__(self,driver):
        self.driver = driver
    
    userName = (By.ID, 'j_username')
    password = (By.NAME,'j_password')
    loginError = (By.XPATH,'//*[@name="login"]//div[contains(@class,"alert-danger")]')
    submitButton = (By.NAME,'Submit')
   
   
    def set_userName(self, _userName):              
        # userNameElement = self.driver.find_element(*LoginPage.userName)
        userNameElement = self.driver.findElementBy(*LoginPage.userName)
        userNameElement.sendKeys(_userName)
        
    
    
    def login_error_displayed(self):
        notifcationElement = self.driver.findElementBy(*LoginPage.loginError)
        
        if notifcationElement.waitUntilDisplay(3):
            Reporter.failed("Login Failed for error : {0}".format(notifcationElement.text))
            return False
        elif notifcationElement.waitUntilHidden(3):
            Reporter.passed("Login passed")
            return True
    
    
    def set_password(self, _password):
        pwordElement = self.driver.findElementBy(*LoginPage.password)        
        pwordElement.sendKeys(_password)        
        
        
    def click_submit(self):
        submitBttn = self.driver.findElementBy(*LoginPage.submitButton)       
        submitBttn.Click()
        
        
    def login(self,tdr=dict()):
        self.set_userName(tdr["userID"])
        self.set_password(tdr["Password"])        
        self.click_submit()

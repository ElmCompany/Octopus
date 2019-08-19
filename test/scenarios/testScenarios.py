
from lib.reporter import Reporter
from lib.globals import Globals
from test.pages.loginPage import LoginPage




class TestScenarios:

    @staticmethod
    def ValidateLogin(TestDataRow=dict()):
        try:
           login_page = LoginPage(Globals.Test.Browser)
           login_page.login(TestDataRow)
           login_page.login_error_displayed()
        except Exception as error:            
            Reporter.failed("Validate Login Failed for {0}".format(error))
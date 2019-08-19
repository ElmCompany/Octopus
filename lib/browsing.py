#!/usr/bin/env python3
import os
import sys

from selenium import webdriver

from lib.configuration import Configuration




class Browsing:

    @staticmethod
    def openBrowser(sBrowserType,sUrl):
       try:
           
           if str(sBrowserType).lower()=="chrome":
               Browsing.Driver = webdriver.Chrome(executable_path=os.getcwd()+Configuration.appSettings["ChromeDriverPath"])
               Browsing.Driver.maximize_window()
               Browsing.Driver.implicitly_wait(5)
               Browsing.Driver.timeout = 5 
               Browsing.Driver.get(sUrl)
               
           elif str(sBrowserType).lower()=="firefox":
               Browsing.Driver = webdriver.Firefox(executable_path=os.getcwd()+Configuration.appSettings["FirFoxDriverPath"])
               Browsing.Driver.maximize_window()
               Browsing.Driver.implicitly_wait(5)
               Browsing.Driver.timeout = 5 
               Browsing.Driver.get(sUrl)
           else:
               Browsing.Driver = webdriver.Edge(executable_path=os.getcwd()+Configuration.appSettings["IEedgeDriverPath"])
               Browsing.Driver.maximize_window()
               Browsing.Driver.implicitly_wait(5)
               Browsing.Driver.timeout = 5 
               Browsing.Driver.get(sUrl)
                
       except:
           print("Failed to open browser ({0})  for Error: {1}".format(sBrowserType,sys.exc_info()[1]))     
       finally:                      
           return Browsing.Driver
    
    @staticmethod
    def closeBrowser():
        try:
            Browsing.Driver.quit()
        except:
           print("Failed to close browser, for Error: {0}".format(sys.exc_info()[1]))           
        



""" p = Browsing()
p.openBrowser("chrome","http://google.com")
p.closeBrowser() """

""" print(dir(p))
x = getattr(Browsing,"openBrowser")
x(Browsing,"ie","http://google.com")

y = getattr(Browsing,"closeBrowser")
y(Browsing) """

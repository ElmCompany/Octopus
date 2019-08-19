#!/usr/bin/env python3

class Configuration:
  connectionStrings =	{    
    "ExcelConn":"Driver={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};DBQ=[ControlFileName];",
    "SqlConn": "Data Source=172.16.64.104;Initial Catalog=EMC_DB;Integrated Security=false;User ID=EMC_APP;password=Axry$9986;",
    "LogDBSqlConn": "Provider=SQLOLEDB;Data Source=192.168.41.47,1433;Initial Catalog=AutoDB;User ID=sa;password=Aa123456;"
  }

  appSettings =	{
    "ControlFileName": "\\Resources\\TestData\\ControlFile.xlsx",
    "Browser.DefaultTimeout": "10",
    "ChromeDriverPath": "\\Resources\\ChromeDriver\\chromedriver.exe",
    "FirFoxDriverPath": "\\Resources\\FireFoxDriver\\geckodriver.exe",
    "IEedgeDriverPath": "\\Resources\\IEedgeDriver\\MicrosoftWebDriver.exe",
    "ReportPath":"\\Reports"
  }



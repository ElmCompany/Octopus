# Octopus Test Automation Framework.

Octopus is a test automation framework that built in python programming language. Using Selenium and APPIUM test automation tools.

Octopus is a Hybrid test automation framework, that combines features of (Modular, Keyword Driven and Data driven).

## Concepts Included:

* Data Driven.

* Keyword Driven.

* Page Object pattern and Page Factory.  [POM ](https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html)

* Common web page interaction methods.

* Common Mobile App interaction methods.

* Objects shared repository.

## Tools

* Python. [Python](https://www.python.org/downloads/release/python-350/)

* Selenium WebDriver. [seleniumhq.org](https://www.seleniumhq.org/)

* APPIUM. [appium.io](http://appium.io/)

* VS Code python editor.

## Installation

* Install Python 3.5.

* Configure python path and pip tools.

* Install selenium libraries using pip from command line.

> pip install -U selenium

* Install APPIUM libraries using pip from command line.

> pip install Appium-Python-Client

* Download Selenium Drivers.

Selenium requires a driver to interface with the chosen browser.

* Chrome: [https://sites.google.com/a/chromium.org/chromedriver/downloads]

* Edge: [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/]

* Firefox: [https://github.com/mozilla/geckodriver/releases]

* Safari: [https://webkit.org/blog/6900/webdriver-support-in-safari-10/]

## Getting Started.

* Clone the Octopus project. [https://github.com/ElmCompany/Octopus.git]

* Open the project in VS Code editor. Select the work space file.

* Project is organized as follow:

### **lib folder**:
Contains shared libraries to handle web / mobile app elements interaction and also as follow.

 * **browsing .py** : used to handle opening the web browser as per defined values in Test Data sheet.

 * **dataManager .py** : used to handle reading and updating data from excel sheet.

 * **driver .py**: used to handle the execution of the test by reading test cases from excel sheet, reading test data, invoking the test methods as per test data and reporting.

 * **globals .py** : used to create global variables in the project like [Globals.Test.Browser].

* **reporter .py** : used to report the test results to html report and set the test status to pass and fail as per execution.

### **test folder**:
Contains the test object repository (Selenium web elements) defined by using the Page Object Concept, and also the test methods to be executed.

* **Pages Folder**: it contains a python module for each page from the application under test.
* loginPage .py: in this file we are using the selenium python find by methods to define the web elements. And also write down the test methods to access these elements.

* We are passing a data collection of type dict() that will provide test data to test methods.

* The name of the test data variables is defined as per the name of column in the test data excel sheet.

### **Scenarios Folder**:
Contains the test scenario methods that will be called by the driver module, these methods can combine more than one test method from different modules.

* **testScenarios. py**: will be used to define our test scenario methods and we use the static method annotations to define our scenario functions.

### **main .py**:
This module is the main entry point for the execution.
We will run our project from the command line as follow.
* open command line.
* cd to the folder contains the main .py.
* run the command 

> python main .py

## Example used in this project:
We are using the login page for the jenkins web server. we defined the web elements of the login page under 

> test/pages/loginPage.py

Test data is defined in the excell sheet under the 

> Resources/TestData/ControlFile.xlsx

Browsers derives is stored under the path 

> Resources/ChromeDriver/chromedriver.exe

### Runing the test:

 1. Define the web elements and create the test method as per the loginpage under test/pages/loginPage.py
 2. Make sure to use pass a data collection of type dictionary to the test method.
 3. define a test scenario method as per the ValidateLogin example under test/scenarios/testScenarios.py
 4. Configure the Excel Control file , Driver sheet with the name of your test scenario method as per the example under Driver sheet in file Resources/TestData/ControlFile.xlsx
 5. Define your test data as in Excel Control file , Login sheet as per the Login sheet under Resources/TestData/ControlFile.xlsx
 6. Make sure to use the column names in Login sheet to be same names you are using in the data dictionary passed to the test method.
 7. Save all you work.
 8. run the test by using the /main.py file as in previous section.
 9. The system will run the test and generate a HTML report with date and time stamp name as per the bellow example Reports/Automation_Result_20190819124044/Automation_Report_Jenkins.html
 

Please for more details do not hesitate to contact me at [LinkedIn](https://www.linkedin.com/in/abdelghany-abdelaziz)
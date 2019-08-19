#!/usr/bin/env python3

import datetime
import os
import sys

from lib.browsing import Browsing
from lib.configuration import Configuration
from lib.dataManager import DataManager
from lib.globals import Globals
from lib.executer import Executer
from lib.reporter import Reporter


class Driver:
    # this clas is the core of the frmaework and will be responsible for mabaging test environment , test data, and test scenarios.
    tblDriver=dict()
    tblEnvironment=dict()
    query = ""
    TestEnvironment=""
    RQMID = ""

    @staticmethod
    def runSequentialTest():
        try:

            # Initializing all global variables and report configurations
            tblEnvironment = DataManager.getDictionaryFrom2ColumnsInExcellSheet("select Name,Value from [Environment$] WHERE Name <> \'\'")            
            Globals.Test.initializeTestGlobals(tblEnvironment)
            Globals.Report.initializeRepoeterGlobals(tblEnvironment)

            # Get the RQM Variables             
            if os.getenv("qm_RQM_TESTCASE_WEBID") == None:
                RQMID="" 
            else :
                RQMID = os.getenv("qm_RQM_TESTCASE_WEBID")

            if RQMID == "":
                query = "select * from [Driver$] where Execution_Flag in ('Yes','yes','YES')"
            else :
                query = "select * from [Driver$] where RQMID = '" + RQMID + "' And Execution_Flag in ('Yes','yes','YES')"
            
            # get all selected test cases for execution in Driver sheet
            tblDriver = DataManager.getDictionaryTableFromExcell(query)

            if len(tblDriver) == 0:
                raise Exception("There is no Data in Driver Sheet for query ("+query+")")
            
            # Opening the report HTML file
            Reporter.startHtmlReport(Globals.Test.ProjectName)

            # Opening the test environment [Browser]
            Globals.Test.Browser = Browsing.openBrowser(Globals.Test.BrowserName,Globals.Test.URL)

            # Loop through the Driver sheet test functions with Execution_Flag = YES 
            for row in tblDriver:
                Executer.executeTestCase(tblDriver[row])

            Reporter.writeFinalStatus()

            Browsing.closeBrowser()

        except:
            if Globals.Test.Browser != None:
                Browsing.closeBrowser()
            print("\t\t Driver Error <<<{0}>>> ".format(sys.exc_info()[1]))
            print("\n\n ========= END OF EXEC ========= Test Status [FAIL] =========")
#!/usr/bin/env python3
import sys

from lib.common import Common
from lib.globals import Globals
from lib.reporter import Reporter
from lib.dataManager import DataManager
from test.scenarios.testScenarios import TestScenarios

class Executer:
    # This calss will be responsible for invoking the test methods recived from driver.
    RowID=""
    TestCaseID=""    
    Function_Name=""
    SheetName=""
    SheetRowNo=""    
    Status=""
    StartTime=""
    EndTime=""
    TestDataRow=None


    @staticmethod
    def executeTestCase(row):
        lstRowsNo = list()
        try:
            # Initialize variables by current Driver Sheet row
            Function_Name = str(row["Function_Name"])
            SheetName = str(row["TestDataSheetName"])
            RowNo = str(row["TestDataSheetRowNo"])            
            RowID = str(row["RowID"])                        
            TestCaseID = str(row["TestCaseID"])           
            TestDataRow = None
            testFunction = None

            lstRowsNo = Common.GetIterations(RowNo,',')

            if len(lstRowsNo) < 1:
                raise Exception("Test Data Sheet RowNo is empty for function ({0}) in Driver sheet row ({1})".format(Function_Name,RowID))
            else:
                Globals.Report.TestCaseIterations = len(lstRowsNo)
                Globals.Report.TestCaseStatus = True
                Reporter.startTest(TestCaseID)
                for rowNum in lstRowsNo:                    
                    Reporter.startIteration(Function_Name, rowNum)
                    TestDataRow = DataManager.getDictionaryTableFromExcell("select * from [" + SheetName + "$] where RowID=" + rowNum )[0]                    
                    if TestDataRow != None:
                        if hasattr(TestScenarios,Function_Name):
                            testFunction = getattr(TestScenarios,Function_Name)
                            testFunction(TestDataRow)
                        else:
                            raise Exception("TestFunction ( {0} ) Not Exist In TestScenarios".format(Function_Name))  
                    else:
                        raise Exception("Test Data Row ( {0} ) Not Exist In Sheet ( {1} )".format(rowNum,SheetName))                        

                    Reporter.endIteration()
                
                Reporter.endTest()

        except:
            print("Failed to execute Test Case for Error {0}".format(sys.exc_info()[1]))
        finally:
            pass
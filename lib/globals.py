#!/usr/bin/env python3
 
import datetime
import os
import sys

from lib.configuration import Configuration


class Globals:
    # Global class hold a global variables for reporting and environment managmaent
    class Report:
        # Reporter class is defining a SET OF VARIABLES that eill be used to handle custom html report
        CycleTotalTestCases=0
        ReportFolder=""                
        ResultFolder=""
        ScreenShootFolder=""
        FinalResults=""
        StartTime=""
        EndTime=""
        TestCaseIterations=0
        PassCount=0
        FailCount=0
        TotalPassCount=0
        TotalFailSteps=0
        TotalFailCount=0
        TotalTestCaseCount=0
        ScreenCaptureCount=0
        IterationStartTime=""
        ReportFileName=""
        ReportHTML=""
        TestCaseStatus=False

        @staticmethod
        def initializeRepoeterGlobals(envVars):
            try:
                Globals.Report.CycleTotalTestCases=0
                Globals.Report.ReportFolder=os.getcwd()+Configuration.appSettings["ReportPath"]            
                Globals.Report.SnapshotCaptureLevel=""
                Globals.Report.ResultFolder=Globals.Report.ReportFolder+"\\Automation_Result_" + datetime.datetime.today().strftime("%Y%m%d%H%M%S")
                Globals.Report.ScreenShootFolder=Globals.Report.ResultFolder+"\\ScreenShots_" + (envVars["ProjectName"] if "ProjectName" in envVars else "Project")
                Globals.Report.ReportFileName=Globals.Report.ResultFolder+"\\Automation_Report_" + (envVars["ProjectName"] if "ProjectName" in envVars else "Project") +".html"
                Globals.Report.FinalResults=""
                Globals.Report.StartTime=""
                Globals.Report.EndTime=""
                Globals.Report.TestCaseIterations=""
                Globals.Report.PassCount=0
                Globals.Report.FailCount=0
                Globals.Report.TotalPassCount=0
                Globals.Report.TotalFailSteps=0
                Globals.Report.TotalFailCount=0
                Globals.Report.TotalTestCaseCount=0
                Globals.Report.ScreenCaptureCount=0
                Globals.Report.IterationStartTime=""            
                Globals.Report.TestCaseStatus=False
                if not os.path.exists(Globals.Report.ResultFolder):
                    os.makedirs(Globals.Report.ResultFolder)
                if not os.path.exists(Globals.Report.ScreenShootFolder):
                    os.makedirs(Globals.Report.ScreenShootFolder)
                if not os.path.exists(Globals.Report.ReportFileName):
                    open(Globals.Report.ReportFileName, 'a+').close() 
            except:
                print(f'Failed to initialize Report global variables for error : {sys.exc_info()[1]}')

    class Test:
        # Test class will define a set of variables to used for managing the test
        BrowserTimeOut=0
        isFirstLogin=False
        Browser=None
        RunEnvironment=""
        URL=""
        BrowserName=""
        RunType=""
        ProjectName=""
        CustomReportEnable=False
        LogedInUserName=""
        IsLogedIn=False
        FrameworkPath=""
        MobileServerURL=""
        isTestParallel=False
        MobileAPP=None
        AndriodDeviceDesc=None
        IOSDeviceDesc=None
        TestStatus=0

        @staticmethod
        def initializeTestGlobals(envVars):
            try:
                Globals.Test.BrowserTimeOut=0
                Globals.Test.isFirstLogin=False
                Globals.Test.Browser=None
                Globals.Test.RunEnvironment=envVars["RunEnvironment"] if "RunEnvironment" in envVars else "WEB"
                Globals.Test.URL=envVars["URL"] if "URL" in envVars else "http://localhost:8080"
                Globals.Test.BrowserName=envVars["Explorer"] if "Explorer" in envVars else "CHROME"
                Globals.Test.RunType=envVars["RunType"] if "RunType" in envVars else "DEBUG"
                Globals.Test.ProjectName=envVars["ProjectName"] if "ProjectName" in envVars else "project"
                Globals.Test.CustomReportEnable=False
                Globals.Test.LogedInUserName=""
                Globals.Test.IsLogedIn=False
                Globals.Test.FrameworkPath=os.getcwd()
                Globals.Test.MobileServerURL=""
                Globals.Test.isTestParallel=False
                Globals.Test.MobileAPP=None
                Globals.Test.AndriodDeviceDesc=None
                Globals.Test.IOSDeviceDesc=None
                Globals.Test.TestStatus=0
            except:
                print(f'Failed to initialize Test global variables for error : {sys.exc_info()[1]}')
    
    # storage for the instance reference
    __Report = None
    __Test = None

    def __init__(self,subCls):
        """ Create singleton instance """
        # Check whether we already have an instance
        if type(subCls) is Globals.Report:
            if Globals.__Report is None:
                # Create and remember instance
                Globals.__Report = Globals.Report()
                # Store instance reference as the only member in the handle
                self.__dict__['_Globals__Report'] = Globals.__Report
        elif type(subCls) is Globals.Test:
            if Globals.__Test is None:
                # Create and remember instance
                Globals.__Test = Globals.Test()
                # Store instance reference as the only member in the handle
                self.__dict__['_Globals__Test'] = Globals.__Test
    

    """ def __getattr__(self, attr):
        # Delegate access to implementation 
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        # Delegate access to implementation
        return setattr(self.__instance, attr, value) """

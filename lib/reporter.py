#!/usr/bin/env python3
 
import datetime
import os
import sys

from selenium import webdriver

from lib.browsing import Browsing
from lib.configuration import Configuration
from lib.dataManager import DataManager
from lib.globals import Globals


class Reporter:
    #  This class will be responsible for reporting status to html report and collect test statistics.    
    
    @staticmethod
    def startTest(sTestCaseName):
        try:
            print("\n\n_________ Start Test Case [ " + sTestCaseName + " ] _________")
            Globals.Report.StartTime = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            Globals.Report.TotalTestCaseCount += 1             
            objFile = open(Globals.Report.ReportFileName, 'a+')
            if objFile.writable:
                objFile.write("<HTML><head><meta charset=\"UTF-8\"></head><BODY><TABLE BORDER=1 CELLPADDING=3 CELLSPACING=1 WIDTH=100%>")
                            #   "<tr><td bgcolor="#5B2C6F" width="15%"><font face="Segoe UI Semilight" color="WHITE" size="3"><b>&nbsp;&nbsp;Test Case ID:</b></font></td><td bgcolor="#5B2C6F" colspan="5"><font face="Segoe UI Semilight" color="WHITE" size="5"><b><center>test case01</center></b></font></td></tr>"
                objFile.write("<TR><TD BGCOLOR=#5B2C6F WIDTH=15%><FONT FACE=\"Segoe UI Semilight\" COLOR=WHITE SIZE=3><B>&nbsp&nbspTest Case ID:</B></FONT></TD><TD BGCOLOR=#5B2C6F COLSPAN=5><FONT FACE=\"Segoe UI Semilight\" COLOR=WHITE SIZE=5><B><Center>" + sTestCaseName + "</Center></B></FONT></TD></TR>")
                Globals.Report.PassCount = 0
                Globals.Report.FailCount = 0  
            else:
                raise IOError("issue in writing to html report.")
        except:
            print("\t\t[Failed]  Starting New Test : {0}".format(sys.exc_info()[1]))         
        finally:
            objFile.close()

    @staticmethod
    def endTest():
        try:
            print("\n_________ End Test Case _________")
            Globals.Report.EndTime = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")            
            objFile = open(Globals.Report.ReportFileName, 'a+')
            if objFile.writable:
                objFile.write("<TR COLS=5><TD BGCOLOR=#C39BD3 WIDTH=15%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B>&nbsp;&nbsp;Start Time: </B></FONT></TD><TD BGCOLOR=C39BD3 WIDTH=30%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B><Center>" + str(Globals.Report.StartTime) + "</Center></B></FONT></TD><TD BGCOLOR=C39BD3 WIDTH=15%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B>&nbsp;&nbsp;End Time: </B></FONT></TD><TD BGCOLOR=C39BD3 WIDTH=30%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B><Center>" + str(Globals.Report.EndTime) + "</Center></B></FONT></TD></TR>")
                if Globals.Report.FailCount > 0:
                    Globals.Report.FinalResults = "FAIL"
                    Globals.Report.TotalFailCount +=1
                    objFile.write("<TR COLS=5><TD BGCOLOR=#C39BD3 WIDTH=15%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B><Center>End of Test Case</Center></B></FONT></TD><TD BGCOLOR=C39BD3 WIDTH=30%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B><Center>Test Steps Passed : &nbsp;" + str(Globals.Report.PassCount) + "</Center></B></FONT></TD><TD BGCOLOR=C39BD3 WIDTH=15%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B><Center>Test Steps Failed : &nbsp;" + str(Globals.Report.FailCount) + "</Center></B></FONT></TD><TD BGCOLOR=C39BD3 WIDTH=30%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B><Center>Final Test Result : </B></FONT><FONT COLOR=RED><B>&nbsp;" + str(Globals.Report.FinalResults) + "</Center></B></FONT></TD></TR>")
                else:
                    Globals.Report.FinalResults = "PASS"
                    Globals.Report.TotalPassCount +=1
                    objFile.write("<TR COLS=5><TD BGCOLOR=#C39BD3 WIDTH=15%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B><Center>End of Test Case</Center></B></FONT></TD><TD BGCOLOR=C39BD3 WIDTH=30%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B><Center>Test Steps Passed : &nbsp;" + str(Globals.Report.PassCount) + "</Center></B></FONT></TD><TD BGCOLOR=C39BD3 WIDTH=15%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B><Center>Test Steps Failed :&nbsp;" + str(Globals.Report.FailCount) + "</Center></B></FONT></TD><TD BGCOLOR=C39BD3 WIDTH=30%><FONT FACE=\"Microsoft YaHei UI\" COLOR=WHITE SIZE=2><B><Center>Final Test Result : </B></FONT><FONT COLOR=#008000><B>&nbsp;" + str(Globals.Report.FinalResults) + "</Center></B></FONT></TD></TR>")

                objFile.write("</TABLE></BODY></HTML>")
                Globals.Report.PassCount = 0
                Globals.Report.FailCount = 0  
            else:
                raise IOError("issue in writing to html report.")
        except:
            print("\t\t[Failed]  Ending Test : {0}".format(sys.exc_info()[1]))         
        finally:
            objFile.close()

    @staticmethod
    def startIteration(sTestCaseName,iIterID):
        try:
            print("\n\t............ Start Iteration With ROW [ " + str(iIterID) + " ]............\n")                            
            objFile = open(Globals.Report.ReportFileName, 'a+')
            if objFile.writable:
                objFile.write("<TR COLS=6><TD BGCOLOR=#3498DB WIDTH=15%><FONT FACE=\"Segoe UI Semilight\" COLOR=WHITE SIZE=3><B>&nbsp;&nbsp;Test Case Description:</B></FONT></TD><TD BGCOLOR=#3498DB WIDTH=30%><FONT FACE=\"Segoe UI Semilight\" COLOR=WHITE SIZE=3><B><Center>" + sTestCaseName + "</Center></B></FONT></TD><TD BGCOLOR=#3498DB WIDTH=15%><FONT FACE=\"Segoe UI Semilight\" COLOR=WHITE SIZE=3><B>&nbsp;&nbsp;Iteration Id: </B></FONT></TD><TD BGCOLOR=#3498DB WIDTH=30%><FONT FACE=\"Segoe UI Semilight\" COLOR=WHITE SIZE=3><B><Center>" + str(iIterID) + "</Center></B></FONT></TD></TR>")
                objFile.write("<TR COLS=6><TD BGCOLOR=#3498DB WIDTH=15%><FONT FACE=\"Segoe UI Semilight\" COLOR=WHITE SIZE=3><B>&nbsp;&nbsp;Step Status</B></FONT></TD><TD BGCOLOR=#3498DB COLSPAN=5><FONT FACE=\"Segoe UI Semilight\" COLOR=WHITE SIZE=3><B>&nbsp;&nbsp;Step Details</B></FONT></TD></TR>")
            else:
                raise IOError("issue in writing to html report.")
        except:
            print("\t\t[Failed]  Starting New Iteration : {0}".format(sys.exc_info()[1]))         
        finally:
            objFile.close()

    @staticmethod
    def endIteration():
        try:
            print("\n\t............ End Iteration ............")                                       
        except:
            print("\t\t[FAIL]  Ending  Iteration  : {0}".format(sys.exc_info()[1]))    

    @staticmethod
    def writeFinalStatus():
        try:            
            objFile = open(Globals.Report.ReportFileName, 'a+')
            if objFile.writable:
                objFile.write("<TABLE><TR><TD COLSPAN=2> </TD></TR></TABLE>")
                objFile.write("<HTML><head><meta charset=\"UTF-8\"></head><BODY><TABLE BORDER=1 CELLPADDING=3 CELLSPACING=1 WIDTH=100%><br/><br/><br/><Caption><font FACE=\"Microsoft YaHei UI\" COLOR=#009900 SIZE=3><b> Test Automation Result Summary </b></font></caption>")
                objFile.write("<TR COLS=6><TD BGCOLOR=#6d7b8d WIDTH=33%><FONT FACE=\"Microsoft YaHei UI\" COLOR=White SIZE=2><B><Center>Total No Of Test Cases</Center></B></FONT></TD><TD BGCOLOR=#6d7b8d WIDTH=33%><FONT FACE=\"Microsoft YaHei UI\" COLOR=White SIZE=2><B><Center>Passed</Center></B></FONT></TD><TD BGCOLOR=#6d7b8d WIDTH=33%><FONT FACE=\"Microsoft YaHei UI\" COLOR=White SIZE=2><B><Center>Failed</Center></B></FONT></TD></TR>")
                objFile.write("<TR><TD BGCOLOR=#6d7b8d WIDTH=33%><FONT FACE=\"Microsoft YaHei UI\" COLOR=White SIZE=2><B><Center>" + str(Globals.Report.TotalTestCaseCount) + "</Center></B></FONT></TD><TD BGCOLOR=#6d7b8d WIDTH=33%><FONT FACE=\"Microsoft YaHei UI\" COLOR=#00E600 SIZE=2><B> <Center>" + str(Globals.Report.TotalPassCount) + "</Center></B></FONT></TD><TD BGCOLOR=#6d7b8d WIDTH=33%><FONT FACE=\"Microsoft YaHei UI\" COLOR=Red SIZE=2><B> <Center>" + str(Globals.Report.TotalFailCount) + "</Center></B></FONT></TD></TR>")
                objFile.write(" </table></body></html>")
            else:
                raise IOError("issue in writing to html report.")
            
            if Globals.Report.TotalFailCount > 0:
                Globals.Report.FinalResults = "FAIL"
                print("\n\n___Executed:"+str(Globals.Report.TotalTestCaseCount)+", Passed:"+str(Globals.Report.TotalPassCount)+", Failed:"+str(Globals.Report.TotalFailCount)+
                    " ______ Test Status [ FAIL ] _________\n")
            else:
                Globals.Report.FinalResults = "PASS" 
                print("\n\n___ Executed: "+str(Globals.Report.TotalTestCaseCount)+", passed: "+str(Globals.Report.TotalPassCount)+", failed: "+str(Globals.Report.TotalFailCount)+
                    " ______ Test Status [ PASS ] _________\n")          

        except:
            print("\t\t[Failed]  Reporting Test Status: {0}".format(sys.exc_info()[1]))         
        finally:
            objFile.close()     
    
    @staticmethod
    def passed(sDetails):
        try:
            print("\t\t[PASS]  " + sDetails)
            Globals.Report.PassCount +=1
            objFile = open(Globals.Report.ReportFileName, 'a+')
            if objFile.writable:
                screenFile = Reporter.saveScreenShot()                
                objFile.write("<TR COLS=5><TD BGCOLOR=#EEEEEE WIDTH=15%><FONT FACE=\"Times New Roman (Headings CS)\" SIZE=3 COLOR=#008000><Center><b>PASS</b></Center></FONT></TD><TD BGCOLOR=#EEEEEE COLSPAN=5><FONT FACE=\"WINGDINGS\"  SIZE=4>2</FONT><FONT FACE=\"Times New Roman (Headings CS)\" SIZE=2><A HREF='" + screenFile + "'>&nbsp;" + sDetails + "</A></FONT></TD></TR>")
            else:
                raise IOError("issue in writing to html report.")
        except:
            print("\t\t[Failed]  reporting status : {0}".format(sys.exc_info()[1]))         
        finally:
            objFile.close()
    
    @staticmethod
    def failed(sDetails):
        try:
            print("\t\t[FAIL]  " + sDetails)
            Globals.Report.FailCount +=1
            objFile = open(Globals.Report.ReportFileName, 'a+')
            if objFile.writable:
                screenFile = Reporter.saveScreenShot()                
                objFile.write("<TR COLS=5><TD BGCOLOR=#EEEEEE WIDTH=15%><FONT FACE=\"Times New Roman (Headings CS)\" SIZE=3 COLOR=RED><Center><b>FAIL</b></Center></FONT></TD><TD BGCOLOR=#EEEEEE COLSPAN=5><FONT FACE=\"WINGDINGS\"  SIZE=4>2</FONT><FONT FACE=\"Times New Roman (Headings CS)\" SIZE=2><A HREF='" + screenFile + "'>&nbsp;" + sDetails + "</A></FONT></TD></TR>")
                            
            else:
                raise IOError("issue in writing to html report.")
        except:
            print("\t\t[Failed]  reporting status : {0}".format(sys.exc_info()[1]))         
        finally:
            objFile.close()

    @staticmethod
    def info(sDetails):
        try:
            print("\t\t[INFO]  " + sDetails)            
            objFile = open(Globals.Report.ReportFileName, 'a+')
            if objFile.writable:                
                objFile.write("<TR COLS=5><TD BGCOLOR=#EEEEEE WIDTH=15%><FONT FACE=\"Times New Roman (Headings CS) \" SIZE=3 COLOR=#FF8C00></FONT><FONT FACE=\"Times New Roman (Headings CS)\"  SIZE=3 COLOR=#0000FF><Center><b>INFO</b></Center></FONT></TD><TD BGCOLOR=#EEEEEE COLSPAN=5><FONT FACE=\"Times New Roman (Headings CS)\"  SIZE=2>" + sDetails + "</FONT></TD></TR>")
            else:
                raise IOError("issue in writing to html report.")
        except:
            print("\t\t[Failed]  reporting status : {0}".format(sys.exc_info()[1]))         
        finally:
            objFile.close()

    @staticmethod
    def startHtmlReport(sProjectName):
        try:
            Globals.Report.PassCount = 0
            Globals.Report.FailCount = 0
            Globals.Report.ScreenCaptureCount = 0
            Globals.Report.TotalPassCount = 0
            Globals.Report.TotalFailCount = 0
            Globals.Report.TotalTestCaseCount = 0      
            
            objFile = open(Globals.Report.ReportFileName, 'w+')
            if objFile.writable:
                objFile.write("<HTML><head><meta charset=\"UTF-8\"></head><BODY><TABLE BORDER=0 CELLPADDING=3 CELLSPACING=1 WIDTH=100%>")
                objFile.write("<TR COLS=2><TD BGCOLOR=WHITE ><IMG SRC=http://www.elm.sa/_LAYOUTS/AlElmPortal/Images/elm_logo.png> </TD> <TD WIDTH=100% BGCOLOR=WHITE><Center><FONT FACE=\"Microsoft YaHei UI\" COLOR=#088A08 SIZE=4><B>&nbsp;" + sProjectName + "  Automation Execution Report <br/>" + datetime.datetime.today().strftime("%Y-%m-%d") + " - " + datetime.datetime.today().strftime("%H:%M:%S") + " <br/> Tested on Machine " + os.getenv("COMPUTERNAME") + "</B></FONT></Center></TD></TR></TABLE>")
                objFile.write("</BODY></HTML><BR>")
            else:
                raise IOError("issue in writing to html report.")
        except:
            print("\t\t[Failed]  opening HTML Report File : {0}".format(sys.exc_info()[1]))         
        finally:
            objFile.close()

    @staticmethod
    def saveScreenShot():
        imgPath=""
        try:
            if Globals.Test.Browser != None:
                Globals.Report.ScreenCaptureCount+=1
                imgPath=Globals.Report.ScreenShootFolder+"\\Img_"+str(Globals.Report.ScreenCaptureCount)+".png"
                Globals.Test.Browser.save_screenshot(imgPath)
        except:
            print("\t\t[Failed]  Take a screen shoot : {0}".format(sys.exc_info()[1]))
        finally:
            return imgPath

#!/usr/bin/env python3

import os
import sys

import pyodbc
from lib.configuration import Configuration


class DataManager:
        cfg = Configuration()
        qry=""
        @staticmethod
        def getDictionaryTableFromExcell(strQuery):
                dataTable=dict()
                colNmaes=dict()
                rowID = 0
                colID =0
                try:
                        DataManager.qry=strQuery
                        cStr = DataManager.cfg.connectionStrings["ExcelConn"].replace("[ControlFileName]",os.getcwd()+DataManager.cfg.appSettings["ControlFileName"])
                        cnxn = pyodbc.connect(cStr,autocommit=True)
                        cursor = cnxn.cursor()
                        cursor.execute(DataManager.qry)
                        # create a dictionary of column names
                        for desc in cursor.description:
                                colNmaes[colID]=desc[0]
                                colID+=1   
                        # Loop through returned data rows                                             
                        for row in cursor: 
                                colID =0   
                                dataRow=dict() 
                                #  create a dictionary using column name and value
                                for column in row:     
                                        dataRow[colNmaes[colID]]= str(column)
                                        colID+=1  
                                # Add the dictionary to the table dictionary
                                dataTable[rowID] = dataRow
                                rowID+=1     
                except:
                        print("Failed to execute query ({0}) on database for Error: {1}".format(strQuery,sys.exc_info()[1]))
                        cnxn.rollback()
                finally:                       
                        cursor.close()
                        cnxn.close()
                        return dataTable
        
        @staticmethod
        def getDictionaryFrom2ColumnsInExcellSheet(strQuery):
                dataTable=dict()                                
                try:
                        DataManager.qry=strQuery
                        cStr = DataManager.cfg.connectionStrings["ExcelConn"].replace("[ControlFileName]",os.getcwd()+DataManager.cfg.appSettings["ControlFileName"])
                        cnxn = pyodbc.connect(cStr,autocommit=True)
                        cursor = cnxn.cursor()
                        cursor.execute(DataManager.qry)                       
                        # Loop through returned data rows                                             
                        for row in cursor: 
                                dataTable[row[0]] = row[1]
                                  
                except:
                        print("Failed to execute query ({0}) on database for Error: {1}".format(strQuery,sys.exc_info()[1]))
                        cnxn.rollback()
                finally:                       
                        cursor.close()
                        cnxn.close()
                        return dataTable

        @staticmethod
        def executeQueryOnExcell(strQuery):               
                try:
                        DataManager.qry=strQuery
                        cStr = DataManager.cfg.connectionStrings["ExcelConn"].replace("[ControlFileName]",os.getcwd()+DataManager.cfg.appSettings["ControlFileName"])
                        cnxn = pyodbc.connect(cStr,autocommit=True)
                        cursor = cnxn.cursor()
                        cursor.execute(DataManager.qry)
                        print("query (%s) executed successfully.!"%(strQuery) )                   
                except:
                        print("Failed to execute query ({0}) on database for Error: {1}".format(strQuery,sys.exc_info()[1]))
                        cnxn.rollback()
                finally:
                        cursor.close()
                        cnxn.close()
                        print("connection is closed")                                
        @staticmethod
        def getDictionaryTableFromSource(strConn,strQuery):
                dataTable=dict()
                colNmaes=dict()
                rowID = 0
                colID =0
                try:
                        DataManager.qry=strQuery
                        cStr = DataManager.cfg.connectionStrings[strConn]
                        cnxn = pyodbc.connect(cStr,autocommit=True)
                        cursor = cnxn.cursor()
                        cursor.execute(DataManager.qry)
                        # create a dictionary of column names
                        for desc in cursor.description:
                                colNmaes[colID]=desc[0]
                                colID+=1   
                        # Loop through returned data rows                                             
                        for row in cursor: 
                                colID =0   
                                dataRow=dict() 
                                #  create a dictionary using column name and value
                                for column in row:     
                                        dataRow[colNmaes[colID]]= str(column)
                                        colID+=1  
                                # Add the dictionary to the table dictionary
                                dataTable[rowID] = dataRow
                                rowID+=1          
                                              
                except:
                        print("Failed to execute query ({0}) on database for Error: {1}".format(strQuery,sys.exc_info()[1]))
                        cnxn.rollback()
                finally:
                        cursor.close()
                        cnxn.close()
                        return dataTable

#!/usr/bin/env python3

import sys

class Common:

    @staticmethod
    def SwapArgs(_min, _max):
        swaplist=list()
        try:            
            __min = _max
            __max = _min
            swaplist = {str(__min),str(__max)}
        except:
            print("Failed to swap arguments for Error ({0})".format(sys.exc_info()[1]))
        finally:
            return swaplist
        

    @staticmethod
    def GetIterations( sIterations, Separator):
        lstIterations = list()
        lstSwap=list()
        arrTmp = str(sIterations).split(Separator)
        for num in arrTmp:
            arrRange = str(num).split('-')
            if len(arrRange) > 1:
                _min = arrRange[0]
                _max = arrRange[1]
                if int(_min) > int(_max):
                    lstSwap = Common.SwapArgs(_min,_max)
                    _min = lstSwap[0]
                    _max = lstSwap[1]

                for j in range(int(_min),(int(_max)+1)):
                    lstIterations.append(str(j))
            else :
                lstIterations.append(str(num))
        try:
            pass
        except:
            print("Failed to get Iterations from ({0}) for Error ({1})".format(sIterations,sys.exc_info()[1]))
        finally:
            return lstIterations

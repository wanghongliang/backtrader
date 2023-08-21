import backtrader.indicators as btind
from backtrader.metabase import AutoInfoClass
from collections import OrderedDict
#sma = btind.MovAv.SMA([], period=15)

a = AutoInfoClass()

class Ta(object):
    _a=dict()
    _getpairsbase = classmethod(lambda cls: OrderedDict())
    @classmethod
    def fun1(cls):
        plotinfo = getattr(cls, 'plotinfo', AutoInfoClass)
        print(Ta._getpairsbase)
        print(type(Ta._getpairsbase))
        print( plotinfo )

print(type(a), a)
print(Ta.fun1())


romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5 }
value = romanNums.setdefault('I','')

print("The return value is: ", romanNums)
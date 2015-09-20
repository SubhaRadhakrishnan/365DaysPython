__Date__ = '9/22/2015'
import math
from fractions import Fraction
import cmath
from decimal import Decimal
def numberCalc(inNum):
    const=Decimal(3+Decimal(math.sqrt(5)))
    powNum=Decimal(math.pow(const,inNum))
    resultPowFloor = math.trunc(powNum)
    resultStr = str('{0:03d}'.format(resultPowFloor))
    strLength = len(resultStr)
    return  resultStr[strLength-3:strLength] + '\n'
from sys import argv
script, inFilename = argv
print( "File Name is",inFilename)
outFileName = inFilename.rstrip('in')+'out'
writeFile = open(outFileName,'w')
count=0
print(numberCalc(19))
for line in open(inFilename):
    if(count !=0):
        numInput = int(line.rstrip('\n'))
        print(numInput,"Case #"+ str(count) + ': ' + numberCalc(numInput))
        writeFile.write("Case #"+ str(count) + ': ' + numberCalc(numInput))
    count+=1

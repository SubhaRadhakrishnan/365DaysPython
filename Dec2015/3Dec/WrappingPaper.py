"""
Advent Day 2
http://adventofcode.com/day/2
"""
from sys import argv
script, inFilename = argv
print( "File Name is",inFilename)
sumArea = 0
ribbonLength=0
firstFloor = False
for line in open(inFilename):
    measures = line.split('x')
    #print(line)
    #print(measures)
    area1= int(measures[0]) * int(measures[1])
    area2= int(measures[0]) * int(measures[2])
    area3= int(measures[1]) * int(measures[2])
    minArea = min(area1,area2,area3)
    sumArea += (2*area1+2*area2+2*area3+minArea)

    firstOne = int(measures[0]) + int(measures[1]) + int(measures[2]) - max(int(measures[0]),int(measures[1]),int(measures[2]))
    ribbonLength +=(2* firstOne)+(int(measures[0])*int(measures[1])*int(measures[2]))

print("    Sum Area -- >" + str(sumArea))
print("RibbonLength -- >" + str(ribbonLength))
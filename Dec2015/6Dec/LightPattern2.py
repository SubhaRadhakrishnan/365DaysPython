"""
Advent Day 6
http://adventofcode.com/day/6
"""
from sys import argv
script, inFilename = argv
print( "File Name is",inFilename)
def switchIt(value,str):
    midIndex = str.index("through")
    x,y =  (int(xyz) for xyz in str[0:midIndex-1].split(","))
    v,w = (int(xyz) for xyz in str[midIndex+8:len(str)].split(","))
    for i in range(x,v+1):
       for j in range(y,w+1):
           if(value==0 ):
               if(matrix[i][j] is not 0):
                   matrix[i][j]-=1
           elif(value==1):
               matrix[i][j]+=1
           else:
               matrix[i][j]+=2

def countBrightnessMatrix():
    count=0
    for i in matrix:
        for j in i:
                count+=j
    return count
matrix = [[0]*1000 for x in range(1000)]
print(countBrightnessMatrix())
#switchIt(1,"0,0 through 999,999")
#print(countMatrix())
#switchIt(2,"0,0 through 999,999")
#switchIt(2,"0,0 through 999,999")
switchIt(0,"0,0 through 0,0")
print(countBrightnessMatrix())
for line in open(inFilename):
    if(line[0:7])=="turn on":
        switchIt(1,line[8:-1])
    elif (line[0:8])=="turn off":
        switchIt(0,line[9:-1])
    else:
        switchIt(2,line[7:-1])
print(countBrightnessMatrix())
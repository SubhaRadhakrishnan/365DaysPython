"""
Advent Day 1
http://adventofcode.com/day/1
"""
from sys import argv
script, inFilename = argv
print( "File Name is",inFilename)
count=0
charCount=0
firstFloor = False
for line in open(inFilename):
   for charItem in line:
       charCount+=1
       if(charItem=='('):
           count+=1
       else:
           count-=1
           if(count==-1 and not firstFloor):
               print("First basement count-->" + str(charCount))
               firstFloor=True
print("Floor is -->" + str(count))
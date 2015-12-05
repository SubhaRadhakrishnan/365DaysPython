"""
Advent Day 5
http://adventofcode.com/day/5
"""
import re
from sys import argv
script, inFilename = argv
print( "File Name is",inFilename)
def repeatValue(str):
    strVal=""
    repeatVal = False
    for char in str:
        if(strVal==char):
            repeatVal = True
            break
        else:
            strVal=char
    return repeatVal
def niceOne(str):
    countVowels= len(re.findall('[aeiou]',str))
    countWrong= len(re.findall('ab|cd|pq|xy',str))
    isRepeat = repeatValue(str)
    if(countVowels >=3  and countWrong==0 and isRepeat):
        return True
    else:
        return False
def repPair(str):
    i=0
    while i<len(str)-3:
        if(str[i:i+2] in str[i+2:len(str)]):
            #print(str[i:i+2])
            #print(str[i+2:len(str)])
            return True
        i+=1
    return False
def repChars(str):
    i=0
    while i<len(str)-3:
        if(str[i]+str[i+1]+str[i] == str[i]+str[i+1]+str[i+2]):
            #print(str[i]+str[i+1]+str[i])
            #print(str[i]+str[i+1]+str[i+2])
            return True
        i+=1
    return False
def niceOne2(str):
    isRepPair = repPair(str)
    isRepChars = repChars(str)
    if(isRepPair and isRepChars):
        return True
    else:
        return False
count=0
for line in open(inFilename):
    if(niceOne(line)):
        count+=1
print("Nice one -->" + str(count))

#print(niceOne2("uurcxstgmygtbstg"))

count=0
for line in open(inFilename):
    if(niceOne2(line)):
        count+=1
print("Nice one -->" + str(count))

"""
Advent Day 4
http://adventofcode.com/day/4
"""
import hashlib

##abcdef609043
startString = "iwrupvqb"
count=0
while True:
    strToTest = startString+str(count)
    hexHash = hashlib.md5(strToTest.encode('utf-8')).hexdigest()
    if(hexHash[0:6]=='000000'):
        break
    count+=1
print(hexHash)
print(strToTest)
print(count)
print("program exit")
"""
Advent Day 3
http://adventofcode.com/day/3
"""
from sys import argv
script, inFilename = argv
def returnTuple(x,y,charItem):
    if(charItem=='>'):
        x+=1
    elif (charItem=='<'):
        x-=1
    elif (charItem=='^'):
        y+=1
    else:
        y-=1
    #print(x,y)
    return x,y

print( "File Name is",inFilename)
items = set()
print(items)
x,v,y,w=0,0,0,0
isSanta = False
#line = "^>v<"
items.add((x,y))
for line in open(inFilename):
    for charItem in line:
        isSanta = not isSanta
        if(isSanta):
            x,y = returnTuple(x,y,charItem)
            print(x,y,charItem)
            items.add((x,y))
        else:
            v,w = returnTuple(v,w,charItem)
            items.add((v,w))
print(items)
print(len(items))

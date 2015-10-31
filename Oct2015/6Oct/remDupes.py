__Date__ = '10/31/2015'
"""From "http://www.practicepython.org/"*****************
14)Write a program (function!) that takes a list and returns a new list that contains all the elements of the
first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""

import random
#firstArr = random.sample(range(50),random.randint(1,40))
firstArr=[1,2,3,4,3,2,1]
print(firstArr)

def remDupes(inArr):
    return list(set(inArr))


def remDupesLoops(loopArr):
    resultArr=[]
    for i in loopArr:
        if i not in resultArr:
            resultArr.append(i)
    return resultArr

print(remDupes(firstArr))
print(remDupesLoops(firstArr))
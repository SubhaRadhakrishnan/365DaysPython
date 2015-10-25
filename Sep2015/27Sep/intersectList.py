__Date__ = '9/27/2015'
"""From "http://www.practicepython.org/"*****************
5)Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
Extras:
1.Randomly generate two lists to test this
2.Write this in one line of Python (don't worry if you can't figure this out at this point - we'll get to it soon)
"""
import random
firstArr = random.sample(range(100),random.randint(1,50))
secArr = random.sample(range(100),random.randint(1,50))
print(firstArr)
print(secArr)
resultArr=[]
for x in firstArr:
    if x in secArr:
        resultArr.append(x)
print(resultArr)
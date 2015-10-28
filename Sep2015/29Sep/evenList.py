__Date__ = '9/29/2015'
"""From "http://www.practicepython.org/"*****************
7)Let's say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""
import random
inArr = random.sample(range(1000),random.randint(1,40))
print("Input array",inArr)
for x in inArr:
    if(x%2==1):
        inArr.remove(x)
print("Even Array",inArr)
__Date__ = '10/31/2015'
""" From "http://www.practicepython.org/"*****************
12)Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""
import random
def shrink_list(inlist):
    return [inlist[0],inlist[len(inlist)-1]]

inArr = random.sample(range(1000),random.randint(2,40))
print(inArr)
print(shrink_list(inArr))

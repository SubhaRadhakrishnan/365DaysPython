__Date__ = '10/30/2015'
"""
From "http://www.practicepython.org/"*****************
10)This week's exercise is going to be revisiting an old exercise (see Exercise 5),
except require the solution in a different way.
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.
Write this in one line of Python using at least one list comprehension.
(Hint: Remember list comprehensions from Exercise 7).
Extra:
Randomly generate two lists to test this
"""
import random
firstArr = random.sample(range(50),random.randint(1,40))
secArr = random.sample(range(50),random.randint(1,40))
print(firstArr)
print(secArr)
result = [i for i in set(firstArr) if i in secArr]
print(result)
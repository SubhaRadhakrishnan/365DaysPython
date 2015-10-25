__Date__ = '9/26/2015'
"""From "http://www.practicepython.org/"*****************
4)Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
 (If you don't know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26/13 has no remainder.)
"""
number=int(input("Please enter a number greater than 2:"))
divisorList = []
for x in range(2,(number//2)+1):
    if (number %x)==0:
        divisorList.append(x)
print(divisorList)



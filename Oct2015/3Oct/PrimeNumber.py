__Date__ = '10/31/2015'
"""From "http://www.practicepython.org/"*****************
11)Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to [Exercise 4](/exercise/2014/02/26/04-divisors.html to help you.
Take this opportunity to practice using functions, described below.
"""


def is_prime_num(num):
    if num<3:
        return False
    for x in range(2,(number//2)+1):
        if (number %x)==0:
            return False
    return True

number=int(input("Please enter a number greater than 2:"))
if(is_prime_num(number)):
    print("Number "+ str(number) + " is prime")
else:
    print("Number "+ str(number) + " is not prime")


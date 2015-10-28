__Date__ = '9/28/2015'
"""From "http://www.practicepython.org/"*****************
6)Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""
inStr=input("Please enter a string:")
rvs=inStr[::-1]

if rvs==inStr:
    print(inStr, " is a Palindrome")
else:
    print(inStr, " is not a Palindrome")
__Date__ = '9/24/2015'
""" ********http://www.practicepython.org/
1)Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old. **/ """
from datetime import date
name = input("Give me your name: ")
age = input("Give me your age: ")
print("Hi " + name +",You will turn 100 years in " + str(date.today().year+(100-int(age))))

__Date__ = '9/25/2015'
"""http://www.practicepython.org/"*****************
2)Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
Extras:
1.If the number is a multiple of 4, print out a different message.
2.Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
number = int(input("Hey give me a number of your choice!:"))
if (number %2)==1 :
    print ("Number you entered is odd!")
elif(number%4)==0 :
    print("Number you entered is multiple of 4!!")
else:
    print("Number you entered is even!")
check=int(input("Give one more number:"))

if((number%check)==0):
    print(str(number)+ " is evenly divisible by "+str(check))
else:
    print(str(number)+ " is not evenly divisible by "+str(check))


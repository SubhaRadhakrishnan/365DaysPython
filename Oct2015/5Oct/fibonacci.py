__Date__ = '10/31/2015'
"""From "http://www.practicepython.org/"*****************
13)Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum
of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13,...)
"""

def fib(inNum):
    if(inNum==0):
        fibArr=[]
    elif inNum==1:
        fibArr=[1]
    elif inNum==2:
        fibArr=[1,1]
    elif inNum>2:
        counter=2
        fibArr=[1,1]
        while counter < inNum:
            fibArr.append(fibArr[counter-1]+fibArr[counter-2])
            counter+=1
    return fibArr
inNum =  int(input("Enter a number for Fibonacci series"))
print(fib(inNum))

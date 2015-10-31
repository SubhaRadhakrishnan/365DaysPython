__Date__ = '10/29/2015'
"""From "http://www.practicepython.org/"*****************
9)Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
Keep the game going until the user types 'exit'
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random
totalcount=0
succ=0
misses=0
while True:
    randNum=random.randint(2,40)
    strin = input("Guess a number or type E(xit)")
    if strin=="E":
        print("Total guesses:" + str(totalcount) + ", success:"+str(succ)+",misses:"+str(misses))
        print("Bbye!!")
        break
    elif (int(strin)==randNum):
        print("You Guessed right!!")
        succ+=1
    else:
        print("Sorry, wrong guess. Correct number was "+str(randNum))
        misses+=1
    totalcount+=1




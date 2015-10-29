__Date__ = '10/25/2015'
"""From "http://www.practicepython.org/"*****************
8)Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock

Other names for the game in the English-speaking world include roshambo and other orderings of the three items, sometimes with "rock" being called "stone"
"""
import random
combis={"R1":"Its a tie!!","S2":"Its a tie!!",
            "P3":"Its a tie!!","R2":"Sorry, you lose!"
            ,"S3":"Sorry, you lose!","P1":"Sorry, you lose!",
            "S1":"Great, You Win!!","P2":"Great, You Win!!",
            "R3":"Great, You Win!!"}
options=["R","S","P"]
cOption=random.choice(options)
userOption = input("Play your option - 1(Rock),2(Scissors),3(Paper)")
print(cOption)
print(userOption)
print(combis[cOption+userOption])
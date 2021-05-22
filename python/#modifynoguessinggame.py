#modifynoguessinggame
import random
winning_number = random.randint(1,100)
number = int(input("guess the number"))
game_over = False
while not game_over:
    if number == winning_number :
        print("you win")
        game_over = true
    else:
        if number < winning_number:
            print("too low")
            guess += 1
            number = int(input("guess again :"))
        else:
            print("too high")
            guess += 1
            number = int(input("guess again")
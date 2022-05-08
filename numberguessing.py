import random
print("guess a number 1-9")
number = random.randint(1,9)
chances=0
print("guess a number from 1-9")
while chances<4:
    guess = int (input("enter your guess"))
    if (guess==number):
        print("ur right", guess)
    elif(guess<number):
        print("too low", guess)
    else: 
        print("too high", guess)
    chances = chances+1
if not chances<4:
    print("you lose")

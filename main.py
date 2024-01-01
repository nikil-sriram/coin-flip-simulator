import random
wouldyouliketoplay = input("Would you like to start the game y/n?")
choices = ['h', 't']
turns = 0
heads = 0
tails = 0
correct = 0
incorrect = 0

while True:
    if wouldyouliketoplay == "y":
        choosingone = random.choice(choices)
        turns += 1
        headsortails = input("Choose heads or tails (h/t)")
        if headsortails == "h":
            heads += 1
        elif headsortails == "t":
            tails += 1
        if headsortails == choosingone:
            print("You got it correct")
            correct += 1
        else:
            print("You got it incorrect")
            incorrect += 1
        print(f"You have played {turns} turns")
        print(f"Amount of times chosen heads: {heads}")
        print(f"Amount of times chosen tails: {tails}")
        print(f"You have guessed correctly {correct} time/times")
        print(f"You have guessed incorrect {incorrect} time/times")
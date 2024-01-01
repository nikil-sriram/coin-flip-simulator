import random
headsortails = input("Choose heads or tails (h/t)")
choices = ['h', 't']
choosingone = random.choice(choices)

if headsortails == choosingone:
    print("You got it correct")
else:
    print("You got it incorrect")
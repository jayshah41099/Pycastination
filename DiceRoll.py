import random

# rang of values of a dice
min_val = 1
max_val = 6

# To loop rolling through user input
roll_again = "yes"

#loop
while roll_again == "yes" or roll_again == "y":
    print(" \n Rolling the dice ... \n The values are : ", random.randint(min_val, max_val))

    # Asking user to roll dice again
    roll_again = input(" Roll the Dice Again? (yes/y) : ")
import random
import math

def main():
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))
    x = random.randint(lower, upper)

    print("\n\t You have only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer! \n")

    count = 0
    while count < math.log(upper - lower + 1, 2):
        count += 1

        guess = int(input("Guess a number:- "))

        if x == guess:
            print("Congratulations you did it in ", count, " try")
            break
        elif x > guess:
            print ("you guessed too small! ")
        elif x < guess:
            print ("You guessed too high! ")

    if count >= math.log(upper - lower + 1, 2):
        print ("\n The number is %d" % x)
        print("\t Better Luck Next Time! ")


if __name__ == '__main__':
    main()
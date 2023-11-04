import random

cards = ['Heart', 'Diamond', 'Clubs', 'Spades']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def pick_a_card():
    card = random.choices(cards)
    number = random.choices(numbers)
    print (f" you have got {card} of {number}.")

if __name__ == '__main__':
    pick_a_card()
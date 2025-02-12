'''This program helps with game wordler.
It gives you word suggestion based on already found letters. 
You can also select position of letters and it will search the dictonary for words that fits the critera.
'''

import nltk
from nltk.corpus import words

# Download the words corpus (if not already downloaded)
nltk.download('words')

# Function to suggest words based on known letter positions
def suggest_words(known_letters, known_positions, max_suggestions=15):
    """
    known_letters: a string with the known letters (e.g., 'apple' means a, p, p, l, e are known).
    known_positions: a dictionary where key = position (1-5) and value = letter at that position.
    max_suggestions: Maximum number of word suggestions to return (default: 15).
    """
    valid_words = []

    # Filter out only 5-letter words from the word list
    word_list = [word.lower() for word in words.words() if len(word) == 5]

    for word in word_list:
        # Check if the word has the correct known letters at their respective positions
        is_valid = True
        for pos, letter in known_positions.items():
            if word[pos - 1] != letter:
                is_valid = False
                break
        
        # Also check if the word contains the known letters in the correct positions
        for idx, letter in enumerate(known_letters):
            if letter != " " and word[idx] != letter:
                is_valid = False
                break
        
        # If it's valid, add to the result list
        if is_valid:
            valid_words.append(word)
        
        # Stop once we've reached the max suggestions
        if len(valid_words) >= max_suggestions:
            break

    return valid_words

# Function to ask the user for solved letters and letter positions
def get_user_input():
    # Ask for known letters in each position
    known_letters = input("Enter the known letters in the word (e.g., 'a _ p _ e' for 'apple'): ").lower()
    
    # Ask if the position of any letter is confirmed
    known_positions = {}
    for i in range(1, 6):
        letter = input(f"Enter the letter in position {i} (leave blank if unknown): ").lower()
        if letter:
            known_positions[i] = letter

    return known_letters, known_positions

def main():
    # Game loop
    print("Welcome to the Wordle Helper!")
    while True:
        print("\nPlease provide the solved letters and known positions.")
        
        # Get user input for known letters and positions
        known_letters, known_positions = get_user_input()

        # Suggest possible words (limit to 15 words)
        possible_words = suggest_words(known_letters, known_positions)

        # If possible words are found
        if possible_words:
            print("\nPossible words based on your input:")
            for word in possible_words:
                print(word)
        else:
            print("\nNo valid words found based on the provided information.")
        
        # Ask the user if they want to continue or quit
        play_again = input("\nDo you want to continue? (y/n): ").lower()
        if play_again != 'y':
            print("Good luck with your Wordle game!")
            break

# Run the program
if __name__ == "__main__":
    main()

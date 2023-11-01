# it identifies the word that spells same from forward or backword - Palindrome Words

def palindrome(sentence):
    special_char = ",.'/?<>}{[]:;"
    for i in special_char:
        sentence = sentence.replace(i, "")

    palindrome = []
    words = sentence.split(' ')
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    
    return palindrome

def main():
    sentence = input(" Enter a sentence: ")
    print(palindrome(sentence))

if __name__ == '__main__':
    main()
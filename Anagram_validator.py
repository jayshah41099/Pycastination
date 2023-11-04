
def Anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

def main():
    print(" the charcter comparision of 'cinema' and 'iceman' is ", Anagram('cinema','iceman'))
    print(" the charcter comparision of 'cool' and 'loco' is ", Anagram('cool','loco'))
    print(" the charcter comparision of 'cinema' and 'niceman' is ", Anagram('cinema','niceman'))


if __name__ == '__main__':
    main()
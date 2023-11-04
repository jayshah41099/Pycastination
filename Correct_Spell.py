from textblob import TextBlob

def convert(string):

    words = list(string.split())

    Correct_words = []

    for i in words:
        Correct_words.append(TextBlob(i).correct())

    for i in Correct_words:
        print(i, end=" ")


def main():
    text = input(" Enter words to check for spelling: ")
    print( " Corrrect spelling: ")
    convert(text)
    
if __name__ == '__main__':
    main()
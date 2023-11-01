# it counts charcter occorences in the single statement.

def count_charcaters(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    print (count)

def main():
    word = input("Enter your String: ")
    print(count_charcaters(word))

if __name__ == '__main__':
    main()
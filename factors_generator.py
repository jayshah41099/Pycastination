def factors(num):
    list = []
    length = num
    for i in range(1, length + 1):
        if num % i == 0:
            length = num // i
            list.append(i)
    
    return list

def main():
    # Prompt the user for the number
    num = int(input("Enter the number to find factors: "))
    print(" Here are the factors: \n", factors(num))

if __name__ == '__main__':
    main()
def fibonacci(num1, num2, length):
    list = []
    list.append(num1)
    list.append(num2)
    for i in range(2, length):
        sum = num1 + num2
        list.append(sum)
        num1 = num2
        num2 = sum

    print(f"The fiboannci sequence starting from {num1} and {num2} for lenght of {length} is : \n", list)


def main():
    # Prompt the user for the number of terms
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num_terms = int(input("Enter the number of terms to generate: "))
    fibonacci(num1, num2, num_terms)

if __name__ == '__main__':
    main()


def Disarium_num(num):
    length = len(str(num))
    temp = num
    sum = 0
    rem = 0
    while temp > 0:
        rem = temp % 10
        sum = sum + int(rem**length)
        temp = temp // 10
        length = length - 1
    
    return sum


def main():
    number = int(input("Enter the Number to check Disarium Number = "))
    sum = Disarium_num(number)
    print("The Sum of the Digits = ", sum)
    if sum == number:
        print("\n %d is a Disarium Number." % number)
    else:
         print("\n %d is not a Disarium Number." % number)

if __name__ == '__main__':
    main()
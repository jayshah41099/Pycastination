def Armstrong_Num(num):
    sum = 0
    temp = num
    power = (len(str(temp)))
    while temp > 0:
        digit = temp % 10
        sum += digit ** power
        temp //= 10

    if num == sum:
        print (num, "is an Armstrong Number.")
    else:
        print (num, "is not an Armstrong Number.")

def main():
    num = int(input("Enter a number: "))
    Armstrong_Num(num)

if __name__ == '__main__':
    main()
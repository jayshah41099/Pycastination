import sys

def perfect_number(num):
    sum = 0
    for i in range (1, num):
        if num % i == 0:
            sum += i
    
    return sum == num

def main():
    num = int(sys.argv[1])
    print(f" Is number {num} a perfect number : {perfect_number(num)}")

if __name__ == "__main__":
    main()


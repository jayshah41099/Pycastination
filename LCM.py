# it finds out least common number, which is divisible by both entered numbers.

def least_common_multiple(a,b):

    if a > b:
        greater = a
    elif b > a:
        greater = b 
    
    while (True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater = greater + 1
    
    return lcm

def main():

    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(least_common_multiple(a,b))

if __name__ == '__main__':
    main()

'''
                                How it works!!
Entered number n=12. it will create the list of true for n + 1.
list = [True, True, True, True, True, True, True, True, True, True, True, True, True]
first two prime we know so it is easy that all we gotta fix is from number 4. 
ignore index (0, 1) and index (2, 3) is rue because it represents prime number 2 and 3.
list = [True, True, **True**, True, True, True, True, True, True, True, True, True, True] --> index 2 is True
we will change the value from true to false. Starting from p * 2 = 4 and skipping a step
list = [True, True, True, True, **True**, True, **True**, True, **True**, True, **True**, True, **True**]
list = [True, True, True, True, False, True, False, True, False, True, False, True, False]
now the value of p is increased by 1. p = 3. we will again change value starting from p * 2 = 6 and skipping a step.
list = [True, True, True, True, False, True, **False**, True, **False**, True, False, True, False]


'''

def sieveofEratosthenes(n):
    primes = [True] * (n + 1) # it will create the list of true for n + 1 numbers.
    p = 2 # knowing the smallest prime
    while (p * p <= n): 
        print(primes)
        if (primes[p]) == True: 
            for i in range( p * 2, n + 1, p): # it will start changing the list value starting from first multiple
                primes[i] = False       # and skipping a step
        p += 1   # increasing the value of p to check for it multiple

    for i in range(2, n):
        if primes[i]: # if the index of the list true it prints the index.
            print(i)

def main():
    n = int(input(" enter a number to check all smaller prime numbers : "))
    sieveofEratosthenes(n)

if __name__ == '__main__':
    main()





tallies = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def RomanToDecimal(roman):
    sum = 0
    for i in range(len(roman)):
        # Check if it's the last numeral
        if i + 1 < len(roman):
            left = roman[i]
            right = roman[i + 1]
            if tallies[left] < tallies[right]:
                sum -= tallies[left]
            else:
                sum += tallies[left]
        else:
            sum += tallies[roman[i]]
    return sum

def main():
    roman = input("Enter Roman Number: ")
    decimal = RomanToDecimal(roman.upper())
    print(f"The decimal value of {roman.upper()} is: {decimal}")

if __name__ == '__main__':
    main()

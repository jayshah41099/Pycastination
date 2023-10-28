# Requirement : pip install python-barcode
# command : python3 barcode.py

import barcode
from barcode import Code128

def generate_barcode(data):
    code = Code128(data)
    code.save("barcode")
    print("Barcode generated.")

def main():
    data = "2468-0369-157"
    generate_barcode(data)

if __name__ == '__main__':
    main()
# it calculates celsius for the entered fahrenheit

fahrenheit = input("Enter the Fahrenheit number : ")
f = float(fahrenheit)

c = (f - 32) * 5/9

print(f" {f} degree fahrenheit is equal to {c} degree celsius. ")
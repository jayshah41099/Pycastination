# requirement : pip install forex_python
# command : python3 Currency_Converter.py

import requests
# from forex_python.converter import CurrencyRates - python library (another method)

def convert_currency(amount, from_currency, to_currency):
    # Replace 'YOUR_API_KEY' with your Fixer.io API key
    api_key = 'YOUR_API_KEY'
    base_url = f'https://api.apilayer.com/exchangerates_data/{api_key}/'

    # Get the latest exchange rates
    response = requests.get(base_url + 'latest')
    data = response.json()

    if response.status_code == 200:
        rates = data['rates']

        if from_currency != 'EUR':
            amount = amount / rates[from_currency]
        
        # Convert to the target currency
        converted_amount = round(amount * rates[to_currency], 2)
        return converted_amount

    else:
        return None

def main():
    print("Currency Converter")
    amount = float(input("Enter the amount: "))
    from_currency = input("From Currency (e.g., USD): ").upper()
    to_currency = input("To Currency (e.g., EUR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")



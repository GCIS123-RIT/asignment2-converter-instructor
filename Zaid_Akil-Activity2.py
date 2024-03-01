# activity2.py
"""
Group members:
- Member 1: Zaid Akil
Description: This module facilitates currency conversion between AED and major currencies (Euro, British Pound, and US Dollar).
"""

# Constants for conversion rates
AED_TO_EURO_RATE = 0.25
AED_TO_POUND_RATE = 0.22
AED_TO_DOLLAR_RATE = 0.27

EURO_TO_AED_RATE = 1 / AED_TO_EURO_RATE
POUND_TO_AED_RATE = 1 / AED_TO_POUND_RATE
DOLLAR_TO_AED_RATE = 1 / AED_TO_DOLLAR_RATE

def aed_to_euro(money):
    """Converts AED to Euro."""
    return money * AED_TO_EURO_RATE

def aed_to_british_pound(money):
    """Converts AED to British Pound."""
    return money * AED_TO_POUND_RATE

def aed_to_dollar(money):
    """Converts AED to US Dollar."""
    return money * AED_TO_DOLLAR_RATE

def euro_to_aed(amount):
    """Converts Euro to AED."""
    return amount * EURO_TO_AED_RATE

def british_pound_to_aed(amount):
    """Converts British Pound to AED."""
    return amount * POUND_TO_AED_RATE

def dollar_to_aed(amount):
    """Converts US Dollar to AED."""
    return amount * DOLLAR_TO_AED_RATE

def main():
    while True:
        print('Welcome to Currency Converter by Zaid Akil\n Main Menu\n---------------------------------')
        print('1. AED to other currencies\n2. Other currencies to AED\n3. Exit')
        choice = input('Enter the conversion direction - choice (1/2/3): ')
        
        if choice == '1':
            amount = float(input('Enter the amount you want to convert: '))
            if amount <= 0:
                print('Invalid amount')
                continue
            print('1. AED to Euro (EUR)\n2. AED to British Pound (GBP)\n3. AED to US Dollar')
            currency_choice = input('Enter the target currency from the above menu - choice (1/2/3): ')
            if currency_choice == '1':
                print(f'{amount} AED is equal to {aed_to_euro(amount):.2f} EUR')
            elif currency_choice == '2':
                print(f'{amount} AED is equal to {aed_to_british_pound(amount):.2f} GBP')
            elif currency_choice == '3':
                print(f'{amount} AED is equal to {aed_to_dollar(amount):.2f} USD')
            else:
                print('Invalid currency choice')
        
        elif choice == '2':
            amount = float(input('Enter the amount you want to convert: '))
            if amount <= 0:
                print('Invalid amount')
                continue
            print('1. Euro (EUR) to AED\n2. British Pound (GBP) to AED\n3. US Dollar to AED')
            currency_choice = input('Enter the target currency from the above menu - choice (1/2/3): ')
            if currency_choice == '1':
                print(f'{amount} EUR is equal to {euro_to_aed(amount):.2f} AED')
            elif currency_choice == '2':
                print(f'{amount} GBP is equal to {british_pound_to_aed(amount):.2f} AED')
            elif currency_choice == '3':
                print(f'{amount} USD is equal to {dollar_to_aed(amount):.2f} AED')
            else:
                print('Invalid currency choice')
        
        elif choice == '3':
            print('Bye!!')
            break
        else:
            print('Invalid choice')
            continue
        
        another_conversion = input('Do you want to do another conversion (y/n): ')
        if another_conversion.lower() != 'y':
            print('Bye!!')
            break

if __name__ == "__main__":
    main()

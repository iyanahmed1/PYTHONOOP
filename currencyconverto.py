#install currency convertor
from currency_converter import CurrencyConverter

def convert_currency(amount, base_currency, target_currency):
    c=CurrencyConverter()
    result=  c.convert(amount, base_currency, target_currency)
    return result

amount=float(input('enter the amount to convert: '))
base_currency= input('Enter the base currency: ').upper()
target_currency=input('Enter the target currency: ').upper()

#PERFORM the conversions
converted_amount=convert_currency(amount, base_currency, target_currency)
print(f'{amount} {base_currency} = {converted_amount: } {target_currency}')
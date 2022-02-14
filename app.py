#Jasn Rodgers Assignment 2C

# USD to EUR = 0.86 , EUR to USD = 1.16, USD to RMB = 6.45,
# RMB to USD = 0.16 , RMB to EUR = 0.13, EUR to RMB = 7.48

amount = int(input('Please enter the amount: '))
currency = input('Do you have USD, RMB, or EUR?: ').upper()
concurrency = input('Which currency are you converting to?: ').upper()
USD2EUR =(amount*0.86)
EUR2USD =(amount*1.16)
EUR2RMB =(amount*7.48)
RMB2EUR =(amount*0.13)
USD2RMB =(amount*6.45)
RMB2USD =(amount*0.16)
if currency == 'USD':
    if concurrency == 'RMB':
        print (f' You have {USD2RMB:.2f} RMB')
    elif concurrency == 'EUR':
        print(f' You have {USD2EUR:.2f} EUR')
    else:
        print('type either "USD"/"EUR"/"RMB" to convert to the other currency')
elif currency == 'EUR':
    if concurrency == 'USD':
        print (f' You have {EUR2USD:.2f} USD')
    elif concurrency == 'RMB':
        print(f' You have {EUR2RMB:.2f} RMB')
    else:
        print('type either "USD"/"EUR"/"RMB" to convert to the other currency')
elif currency == 'RMB':
    if concurrency == 'EUR':
        print(f' You have {RMB2EUR:.2f} EUR')
    elif concurrency == 'USD':
        print(f' You have {RMB2USD:.2f} USD')
    else:
        print('type either "USD"/"EUR"/"RMB" to convert to the other currency')
else:
    print('type either "USD"/"EUR"/"RMB" to convert to the other currency')

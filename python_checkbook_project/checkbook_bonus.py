import json
import os
# import sys
# import simple_bank_data.txt
# json.load(open('bank_data.json'))


# b_d = open(simple_bank_data.txt)
# b_d = bank_data.json

# import from json read files
# balance is an int
with open ('bank_data.json', 'r') as b_d:
    balance = json.load(b_d)
# print(balance)


# defined balnce as as int
# print(type(balance))

# Landing Page
print()
print()
print('~~~ Welcome to your terminal checkbook! ~~~')
print(' What would you like to do?')
print(' 1) view current balance')
print(' 2) record a debit (withdraw)')
print(' 3) record a credit (deposit)')
print(' 4) exit')
print()

# options
## 
while True:
    fi = input('what would you like to do?')
    print('~~~ Welcome to your terminal checkbook! ~~~')
    print(' What would you like to do?')
    print(' 1) view current balance')
    print(' 2) record a debit (withdraw)')
    print(' 3) record a credit (deposit)')
    print(' 4) exit')

    if fi == '4':
        print()
        print()
        print('Good bye!')
        with open ('bank_data.json', 'w') as b_d:
            json.dump(balance, b_d)
        break

    elif fi == '1':
        print()
        print()
        print('This is your current balance:')
        print()
        print(balance)
        print()

    elif fi == '2':
        print()
        print()
        d = int(input('Please enter amout to debit from your account!'))
        balance -= d

    elif fi == '3':
        c = int(input('Please enter amount to credit to your account!'))
        balance += c
        
    else:
        print()
        print()
        print('PLEASE ENTER A VALID RESPONSE.')
        continue


# write to files
#with open ('bank_data.json', 'w') as b_d:
#    json.dump(balance, b_d)
 
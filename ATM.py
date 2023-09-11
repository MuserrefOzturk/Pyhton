Account1={'name':'Muserref Ozturk', 'AccountNo':'123456','balance':3000,'exbalance':2000}

Account2={
           'name':'Ali Ozturk',
           'AccountNo':'13559',
           'balance':4000,
           'exbalance':3000
        }

def withdrawMoney(acc,amount):
    print(f"Hello {acc['name']}")

    if(acc['balance']>=amount):
        acc['balance'] -= amount
        print('You can withdraw your money')
    else:
        sum= acc['balance']+acc['exbalance']

        if(sum>=amount):
            useExbalance=input('Would you like to use exbalance (y/n)')

            if useExbalance=='y':
                print('withdraw your money.')
            else:
                print(f" You have {acc['balance']} in your account with {acc['AccountNo']} number.")



        else:
            print('Sorry, your balance is insufficient')   


withdrawMoney(Account1,3000)
withdrawMoney(Account1,3000)



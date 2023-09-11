liste=['1','2','5a','10b','abc','10','20']
# find the digits in liste
for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue 
        

# unless user enter 'q' , be sure that you get digit from input

while True:
    number= input('number: ')
    if number == 'q':
        break

    try:
        result=int(number)
        print('You entered: ',result)
    except ValueError:
        print('invalid value')
        continue 

# the password mustn't include turkish char.

def check_password(password):
    
    tur_char='şçüğıİö'
    for i in tur_char:
        if i in password:
            raise TypeError('Password can not include Turkish Characters')
        else:
            pass
    print('valid password')

password=input('password: ')
try:
    check_password(password)
except TypeError as err:
    print(err)


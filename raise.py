'''
x=int(input('x: '))
x=6
if x>5:
    raise Exception("x can not be grater than 5")
'''
def check_password(psw):
    import re
    if (len(psw)) < 8:
        raise Exception ("Password must be at least 7 characters")
    elif not re.search("[a-z]",psw):
        raise Exception ("Password must include lowercase")
    elif not re.search("[A-Z]",psw):
        raise Exception ("Password must include uppercase")
    elif not re.search("[0-9]",psw):
        raise Exception ("Password must include digit")
    elif not re.search("[_@$]",psw):
        raise Exception ("Password must include alpha numeric character")
    elif re.search("\s",psw):
        raise Exception ("Password mustn't include space")
    else:
        print('Pasword valid')

try:
    check_password("12345")
except Exception as e:
    print(e)


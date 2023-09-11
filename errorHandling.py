try:
    x=int(input('x: '))
    y=int(input('y: '))
    print(x/y)
except ZeroDivisionError:
    print('You can not enter 0 for y' )
except ValueError:
    print('enter digit for x and y')

'''
try:
    x=int(input('x: '))
    y=int(input('y: '))
    print(x/y)
except (ZeroDivisionError,ValueError):
    print('You entered incorrect information' )
'''
'''
try:
    x=int(input('x: '))
    y=int(input('y: '))
    print(x/y)
except:
    print('You entered incorrect information' )
else:
    print('everything ok')
'''
'''
while True:
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        print(x/y)
    except:    
        print('You entered incorrect information' )
    else:
        break

'''
#if we want to see the error resource :


'''
while True:
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        print(x/y)
    except Exception as e :    
        print('You entered incorrect information' )
        print(e)
    else:
        break
    finally:
        print('try except ended')

'''
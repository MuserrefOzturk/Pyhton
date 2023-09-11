def add(*params):
    sum=0
    for n in params:
        sum += n
    return sum

print(add(19,23,45,67))


def displayUser(**params):
    for key,value in params.items():
        print(key + ' is',value)
        #print('{} is {}'.format(key,value))
displayUser(name='Muserref', age=39, city='istanbul')
displayUser(name='Ada', age=9, city='izmir', phone='123456')

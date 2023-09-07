number=int(input('Enter a number: '))
isprime=True
if number==1:
    isprime=False
    print('1 is not prime number')

for i in range(2,number):
    if (number % i == 0):
        isprime=False
        break
if isprime:
    print('The number is prime.')
else:
    print('The number is not prime')

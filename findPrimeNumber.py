def findprime(num1,num2):
    for number in range(num1,num2):
        if number>1:
            for nums in range(2,number):
                if number % nums == 0:
                    break
            else: 
                print(number)

num1=int(input('num1: '))
num2=int(input('num2: '))
findprime(num1,num2)
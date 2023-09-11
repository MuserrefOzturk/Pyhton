numbers=[1,3,5,7,9,12,19,21]
i=0
while(i<=len(numbers)):
    print(numbers[i])
    i+= 1
    

start=int(input('type a beginning number: '))
end=int(input('type an ending number: '))
i=start
while (i<end):
    i+=1
    if(i%2==1):
        print(i)



import random

result1= random.random()
result2= random.random()*100
result3= random.uniform(20,50)
result4= random.randint(1,10)

print(result1)
print(result2)
print(result3)
print(result4)

names=['muserref','mert','samet','joseph']
r=names[0]
print(r)

rslt=names[random.randint(0,len(names)-1)]
#rslt=random.choice(names)
print(rslt)

greeting='Hello'
gr=random.choice(greeting)
print(gr)
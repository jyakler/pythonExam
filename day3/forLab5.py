import random
start=random.randint(1,10)
end=random.randint(30,40)
sum=0
for a in range(start,end+1):
    if a%2==0:
        sum+=a
print(start,"부터",end,"까지 짝수의 합: ",sum)
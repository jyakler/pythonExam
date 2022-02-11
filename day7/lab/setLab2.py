import random
lotto=set()
while len(lotto)<6:
    rand=random.randint(1,45)
    lotto.add(rand)

print("행운의 로또번호 :",end="")
i=0
for a in lotto:
    if i!=5:
        print(a,end=", ")
        i+=1
    else:
        print(a)
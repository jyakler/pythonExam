import random
list1=[]
for _ in range(0,6):
    rand=random.randint(1,45)
    if rand not in list1:
        list1.append(rand)
    else:
        _=_-1

print("행운의 로또번호 :",end="")
for i in range(len(list1)):
    if i<len(list1)-1:
        print(list1[i],", ",sep="",end="")
    else:
        print(list1[i])
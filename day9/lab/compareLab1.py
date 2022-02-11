def createList(*num,type=1):
    temp=[]
    if len(num)==0:
        temp=[d for d in range(1,31)]
    else:
        for a in num:
            temp.append(a)
    if type==2:
        list1=[d for d in temp if d%2==0]
    elif type==3:
        list1 = [d for d in temp if d % 2]
    elif type==4:
        list1=[d for d in temp if d>10]
    else:
        list1=temp
    return list1

print(createList(0,1,2,3,4,5,6))
print(createList(0,1,2,3,4,5,6,type=2))
print(createList(0,1,2,3,4,5,6,type=3))
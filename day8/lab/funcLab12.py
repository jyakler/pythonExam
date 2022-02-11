dic={}
def mydict(**num):
    if len(num)==0:
        return dic
    for key,value in num.items():
        dic['my'+key]=value
    return dic

mydict(begin=1,start=2,end=3)
print(dic)

mydict(seq=1,asd=2,qsc=3,qq=44)
print(dic)
import random
oper_num=random.randint(1,10)
print("결과값 :",end="")
if oper_num%5==1:
    print(300+50)
elif oper_num%5==2:
    print(300-50)
elif oper_num%5==3:
    print(300*50)
elif oper_num%5==4:
    print(300/50)
else:
    print(300%50)
def differtwovalue(num1,num2):
    dif=int(num1)-int(num2)
    if dif<0:
        dif=-dif
    return dif

import random
num1=random.randint(1,30)
num2=random.randint(1,30)
result=differtwovalue(num1,num2)
print("%d 와 %d 의 차는 %d입니다."%(num1,num2,result))

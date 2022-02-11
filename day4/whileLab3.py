import random
count=0
while 1:
    a=random.randint(0,30)
    if a==0 or a>=27:
        break
    print("%s(%d)"%(chr(a+0x40),a))
    count+=1
print("수행횟수는 %d 번입니다"%count)
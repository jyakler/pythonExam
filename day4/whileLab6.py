while 1:
    sum=1
    a=int(input("숫자 입력: "))
    if a==0:
        print("종료")
        break
    if a<-10 or a>10:
        continue
    if a>0:
        print("입력값 :%d"%a)
        for _ in range(1,a+1):
            sum*=_
        print(sum)
    elif a<0:
        print("입력값(부호변경) :%d"%(a*-1))
        for _ in range(1,a*-1+1):
            sum*=_
        print(sum)
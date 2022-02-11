while 1:
    a=int(input("1~12 사이의 값을 입력하세요 :"))
    if not(a>=1 and a<=12):
        print("1~12사이의 값을 입력하세요!")
        break
    else:
        if a>=3 and a<=5:
            print("%d월은 봄"%a)
        elif a>=6 and a<=8:
            print("%d월은 여름"%a)
        elif a>=9 and a<=11:
            print("%d월은 가을"%a)
        else:
            print("%d월은 겨울"%a)
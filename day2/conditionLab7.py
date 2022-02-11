num=int(input("1부터 10사이의 숫자를 하나 입력하세요 : "))
if num in range(1,11):
    print(num,": ",end="")
    if num%2==0:
        print("짝수")
    else:
        print("홀수")
else:
    print("1부터 10사이의 값이 아닙니다.")
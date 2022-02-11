def expr(num1,oper,num2):
    if oper=="+":
        return int(num1)+int(num2)
    elif oper=="-":
        return int(num1)-int(num2)
    elif oper=="*":
        return int(num1)*int(num2)
    elif oper=="/":
        return int(num1)/int(num2)
    else:
        return None

num1=input("입력 숫자: ")
oper=input("입력 연산자: ")
num2=input("입력 숫자: ")
result= expr(num1,oper,num2)
if result==None:
    print("수행불가")
else:
    print("연산결과 :%d"%result)
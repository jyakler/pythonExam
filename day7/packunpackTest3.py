def myfunc1():
    return 1,10,100  # 튜플로 패킹하여 리턴함

result = myfunc1()
print(result)
print(type(result))


def myfunc2():
    return [1,10,100]  # list로 패킹하여 리턴함

result = myfunc2()
print(result)
print(type(result))


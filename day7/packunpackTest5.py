# 리스트도 패킹은 가능
data = [1,2,3,4]

print(data)
print(data[0], data[1], data[2], data[3])

print("*"*30)
a = [10,20,30,40]
print(a)

print("*"*30)
a,b,c,d = [10,20,30,40]
print(a)
print(b)
print(c)
print(d)

print("*"*30)
x,*y,z = [10,20,30,40]
print(x)
print(y)
print(z)

print("*"*30)
p = 100, 200, 300 # 나열된 값의 패킹은 기본적으로 튜플
print(p)

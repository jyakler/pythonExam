def myfunc(*str):
    for data in str:
        print(data,end=" ")
    print()
listv3=list("python")
v1,v2,v3,v4,v5,v6=listv3
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)
myfunc(*listv3)
print(*listv3)

print(listv3)
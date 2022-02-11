import random
listnum=[]
for _ in range(10):
    rand=random.randint(1,50)
    listnum.append(rand)
print(listnum)
print(listnum[0])
print(listnum[9])
print(listnum[1:6])
print(listnum[::-1])
print(listnum[:])
del listnum[4]
print(listnum[::1])
del listnum[1:3]
print(listnum[0:])
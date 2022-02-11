import random
set1=set()
set2=set()
while len(set1)<10:
    rand=random.randint(1,20)
    set1.add(rand)
while len(set2)<10:
    rand2=random.randint(1,20)
    set2.add(rand2)

print("집합 1:",set1)
print("집합 2:",set2)
print("두 집합에 모두 있는 데이터 :",set1.intersection(set2))
print("집합1 또는 집합2 에 있는 데이터 :",set1.union(set2))
print("집합1에는 있고 집합2에는 없는 데이터 :",set1-set2)
print("집합2에는 있고 집합1에는 없는 데이터 :",set2-set1)
print("집합1과 집합 2가 각자 가지고 있는 데이터",set1^set2)
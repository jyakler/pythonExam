import random

listv1=[random.randint(0,100) for _ in range(10)]
#dic={d:"pass" for d in listv1 if d>=60}
#dic={d:"nopass" for d in listv1 if d<60}
dic2={d:("pass" if d>=60 else "nopass") for d in listv1 }

print(dic2)


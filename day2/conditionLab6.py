import random
score = random.randint(0,100)

if score>=90:
    test="A"
elif score >= 80:
    test = "B"
elif score>=70:
    test = "C"
elif score>=60:
    test = "D"
else:
    test = "F"

print(score,"점은 ",test,"등급입니다.",sep="")
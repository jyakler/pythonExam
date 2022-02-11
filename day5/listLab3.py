listnum=[10,5,7,21,4,8,18]
max=0
min=999
for a in listnum:
    if a>max:
        max=a
    if a<min:
        min=a
print("최솟값 : %d,최댓값 : %d"%(min,max))
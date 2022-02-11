list1=[["B","C","A","A"]
       ,["C","C","B","B"]
       ,["D","A","A","D"]
       ]
list2=[]
for a in range(0,4):
    count = 0
    for x in range(0,3):
        for b in list1[x]:
          if b==chr(65+a):
                count+=1
    list2.append(count)

print(f"A는 {list2[0]}개 입니다.")
print(f"B는 {list2[1]}개 입니다.")
print(f"C는 {list2[2]}개 입니다.")
print(f"D는 {list2[3]}개 입니다.")
list1=[[10,20,30,40,50]
       ,[5,10,15]
       ,[11,22,33,44]
       ,[9,8,7,6,5,4,3,2,13]
       ]
for a in range(0,len(list1)):
    sum=0
    for b in list1[a]:
        sum+=b
    print(f"{a+1}행의 합은 {sum}입니다.")
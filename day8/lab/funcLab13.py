def myprint(*num,**data):
    if len(num)==0:
        print("Hello Python")
        return
    dic={}
    dic["deco"] = "**"
    dic["sep"] = ","
    for key,value in data.items():
        dic[key]=value

    print(dic["deco"],end="")
    print(*num,sep=dic["sep"],end='')
    ''' 
    for a in num:
         if a!=num[-1]:
             print(a,end=dic["sep"])
         else:
             print(a,end="")
     '''
    print(dic["deco"])

myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
myprint()
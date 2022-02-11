def mycompredict(**data):
    dic={}
    if len(data)==0:
        return dic
    dic={'my'+k:v for k,v in data.items()}
    return dic

print(mycompredict(begin=1,start=2,end=3))

print(mycompredict(begin=1,start=2,end=3,meme=132))
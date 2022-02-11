f1=None
count=0
try:
    f1=open("yesterday.txt","rt",encoding="UTF-8")
    for text in f1.readlines():
        words=text.split()
        for i in words:
            if i.find("yesterday")!=-1 or i.find("Yesterday")!=-1:
                count+=1

except(FileNotFoundError):
    print("파일을 읽을 수 없어요")
else:
    print("Number of a Word 'Yesterday'", count)
finally:
    print("수행완료!!")
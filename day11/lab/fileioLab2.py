f1=None
try:
    f1=open("sample.txt","rt",encoding="UTF-8")
    f2=open("sample_2022_02_06.txt","a",encoding="UTF-8")
    text=f1.read()
    f2.write(text)
    print("저장이 완료되었습니다.")
except:
    print("에러")

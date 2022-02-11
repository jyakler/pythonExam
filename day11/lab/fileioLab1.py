import time
import calendar
import os
try:
    if os.path.exists("c:/iotest"):
        #print("이미존재함")
        pass
    else:
        os.mkdir("c:/iotest")
        #print("생성함")
    f1=open("c:/iotest/today.txt","wt")
    now = time.localtime()

    f1.write("오늘은 %d년 %d월 %d일입니다.\n" % (now.tm_year, now.tm_mon, now.tm_mday))
    yoil = ['월', '화', '수', '목', '금', '토', '일']
    day = calendar.weekday(2022,8,15) # 숫자
    f1.write("오늘은 %s요일입니다.\n"%yoil[calendar.weekday(now.tm_year,now.tm_mon,now.tm_mday)])
    f1.write("나는 %s요일에 태어났습니다.\n"%yoil[calendar.weekday(1997,9,3)])
    print("저장이 완료되었습니다.")
except:
    print("에러")
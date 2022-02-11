weather={
    "월":(5,-3)
    ,"화":(2,-8)
    ,"수":(1,-10)
,"목":(4,-8)
,"금":(3,-8)
,"토":(3,-9)
,"일":(4,-9)
}
day= input("요일명을 한글로 입력하세요 :")
if day in weather:
    print(f'{day}요일의 최저온도는 {min(weather[day])} 이고 최고 온도는 {max(weather[day])}입니다')
else:
    print(f'{day}요일의 정보를 찾을 수 없습니다')

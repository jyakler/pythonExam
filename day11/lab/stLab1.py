import calendar
while(1):
    try:
        year=int(input("입력 년도: "))
        month=int(input("입력 월: "))
        print(calendar.month(year, month))
        break
    except(ValueError):
        print("value error 다시 입력")

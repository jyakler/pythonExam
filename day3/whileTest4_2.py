import random    # random 모듈을 가져옴

while True :
    dice_num = random.randint(1, 6)
    print("추출된 주사위 값 :", dice_num)
    if dice_num > 4 :
        print("ㅋㅋ")
    else :
        break

print("종료!!")
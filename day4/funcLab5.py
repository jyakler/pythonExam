def print_triangle(a):
    if a>10:
        return None
    for _ in range(a,0,-1):
            for b in range(_):
                print("@",end="")
            print()

num=int(input("숫자 입력: "))
print_triangle(num)
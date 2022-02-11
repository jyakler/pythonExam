def print_gugudan(num):
    if not( num>=1 and num<=9):
        return
    for _ in range(1,10):
        print("%d * %d= %d"%(num,_,num*_))
    print("-"*40)

print_gugudan(3)
print_gugudan(7)

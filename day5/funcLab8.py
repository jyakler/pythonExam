def print_triangle_withdeco(num,deco="%"):

    for a in range(1,num+1):
        print(" " * (num - a), sep="", end="")
        print(deco*a, end="")
        print()

print_triangle_withdeco(2)
print_triangle_withdeco(4,"*")
def sumeven(*num):
    if len(num)==0:
        return -1
    sum=0
    for data in num:
        if data%2==0:
            sum+=data


    return sum
print(sumeven(1, 2, 3, 4, 5))
print(sumeven(11, 22, 33, 44, 55))
print(sumeven(1, 3, 5))
print(sumeven())

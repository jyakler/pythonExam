def number_all_sum(*num):
    sum=0
    flag=0
    if len(num)==0:
        return None
    for data in num:
        if type(data)==int:
            flag=1
            sum+=data
    if flag:
        return sum
    else:
        return None

print(number_all_sum(1, 2, 3, 4, 5))
print(number_all_sum(1, 2, 'a', 3, 4, 'b', 5))
print(number_all_sum(10, 20, True))
print(number_all_sum())
print(number_all_sum('a', True, '가'))

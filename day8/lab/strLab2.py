#1
s1="pythonjavascript"
print(len(s1))
#2
s2="010-7777-9999"
print(s2.replace("-",""))
#3
s3="PYTHON"
print(s3[::-1])
#4
s4="Python"
print(s4.lower())
#5
s5="https://www.python.org/"
print(s5.replace("https://","").replace("/",""))
#6
s6="891022-2473837"
a=s6.split("-")
if a[1][0]=="1" or a[1][0]=="3":
    print("남성")
else:
    print("여성")
#7
s7="100"
print(int(s7))
print(float(s7))
#8
s8="The Zen of Python"
print(s8.count("n"))
#9
print(s8.find("Z"))
#10
list1=(s8.upper()).split(" ")
print(list1)
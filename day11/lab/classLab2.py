class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def getBookInfo(self)->str:
        return str(self.title)+','+str(self.author)+','+str(self.price)
    def __str__(self):
        return "Book 클래스로 생성된 객체"

book1=Book("파이썬정복","김상형",22000)
book2=Book("책2","작가2",1000)
book3=Book("책3","작가3",7777)
book4=Book("책4","작가4",10001)
book5=Book("책5","작가5",33210)

bookstore=[
Book("파이썬정복","김상형",22000),
Book("책2","작가2",1000),
Book("책3","작가3",7777),
Book("책4","작가4",10001),
Book("책5","작가5",33210)
]
for i,book in enumerate(bookstore,1):
    print("[객체",i,":", book1.__str__(), "]")
    a, b, c = book1.getBookInfo().split(",")
    print(a, b, c, sep="\n")
print("-" * 70)

print("[객체1:",book1.__str__(),"]")
a,b,c=book1.getBookInfo().split(",")
print(a,b,c,sep="\n")
print("-"*70)

print("[객체2:",book2.__str__(),"]")
a,b,c=book2.getBookInfo().split(",")
print(a,b,c,sep="\n")
print("-"*70)

print("[객체3:",book3.__str__(),"]")
a,b,c=book3.getBookInfo().split(",")
print(a,b,c,sep="\n")
print("-"*70)

print("[객체4:",book4.__str__(),"]")
a,b,c=book4.getBookInfo().split(",")
print(a,b,c,sep="\n")
print("-"*70)

print("[객체5:",book5.__str__(),"]")
a,b,c=book5.getBookInfo().split(",")
print(a,b,c,sep="\n")
print("-"*70)
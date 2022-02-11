class GoodStock:
    def __init__(self,code,amount):
        self.code=code
        self.amount=amount
    def addStock(self,amount):
        self.amount+=amount
        print("재고 수량 :",self.amount)

code=input("상품 코드를 입력하세요 :")
num=int(input("재고 수량을 입력하세요:"))
a1=GoodStock(code,num)
print("상품 코드: ",a1.code)
print("재고 수량: ",a1.amount)
num2=int(input("추가할 수량을 입력하세요: "))
a1.addStock(num2)
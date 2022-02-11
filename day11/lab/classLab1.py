class Member:
    def __init__(self,name,account,passwd,birthyear):
        self.name=name
        self.account=account
        self.passwd=passwd
        self.birth=birthyear


mem1=Member("1번","aa",12312,1992)
mem2=Member("2번","aa1",333,1993)
mem3=Member("3번","aa4","a32",1995)
print(f"회원1: {mem1.name} {mem1.account,mem1.passwd,mem1.birth}")
print(f"회원2: {mem2.name} {mem2.account,mem2.passwd,mem2.birth}")
print(f"회원3: {mem3.name} {mem3.account,mem3.passwd,mem3.birth}")

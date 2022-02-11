def isPYTHON(str):
    if "PYTHON" in str:
        return True
    else:
        return False

ok=isPYTHON("나는 PYTHON을 학습합니다.")
if ok==True:
    print("PYTHON이 존재합니다")
else:
    print("PYTHON이 존재하지 않습니다")

ok=isPYTHON("나는 python을 학습합니다")
if ok==True:
    print("PYTHON이 존재합니다")
else:
    print("PYTHON이 존재하지 않습니다")
ok=isPYTHON("PYTHON1234")
if ok==True:
    print("PYTHON이 존재합니다")
else:
    print("PYTHON이 존재하지 않습니다")
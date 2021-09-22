from atm1 import atm
atm = atm()
print("통장 또는 카드를 삽입하여주십시오.")
while True:

    a = input("1. 입금\n2. 출금\n3. 송금\n 선택>> ")
    if a == "1":
        amount = input("입금하실 금액을 투입하여주십시오")
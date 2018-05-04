# coding: cp949
print("공원 요금 계산 프로그램Ver2\n")

age = int(input('나이를 입력하세요.: '))

grade=""
fee=0

if age <0:
    print('다시 입력하세요.')
else:
    
    if age < 4:
        grade='유아'
        fee=0
    elif age < 14:
        grade='어린이'
        fee=2000
    elif age < 19:
        grade='청소년'
        fee=3000
    elif age < 66:
        grade='성인'
        fee=5000
    elif age > 65:
        grade='노인'
        fee=0

    money = int(input('돈을 입력하세요.: '))
    print('귀하는[%s]등급이며요금은[%d]원입니다.'%(grade,fee))
    if money - fee < 0:
        print("%d가 모자랍니다. 입력 하신 %d를 반환합니다."%(fee-money,money))
    elif money == fee:
        print("감사합니다. 티켓을 발행합니다.")
    elif money - fee > 0:
        print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환 합니다."%(money-fee))

# coding: cp949
print("공원 요금 계산 프로그램Ver4\n")

while 1 :
    age = -1
    while age < 0 :
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
        print('귀하는[%s]등급이며요금은[%d]원입니다.'%(grade,fee))

        form = int(input('요금유형을 선택하세요.(1:현금,2:공원 전용 신용카드):'))
        if form == 1:
            print('현금을선택하셨습니다.')
            money = int(input('금액을 입력하세요.: '))
            if money - fee < 0:
                print("%d가 모자랍니다. 입력 하신 %d를 반환합니다."%(fee-money,money))
            elif money == fee:
                print("감사합니다. 티켓을 발행합니다.")
            elif money - fee > 0:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환 합니다."%(money-fee))

        elif form ==2:
            fee = fee * 0.9
            if age >=60 and age <= 65:
                fee = fee * 0.95
            print('공원 전용 신용카드를 선택하셨습니다.')
            print('[%d]원 결제되었습니다. 티켓을 발행합니다.'%fee)
        print("")


        

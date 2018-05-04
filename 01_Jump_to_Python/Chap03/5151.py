# coding: cp949

price = [0,2000,3000,5000]

grade = 0
count = 0

freeDayTicket = 3
freeYearTicket = 5

while 1 :
    age = -1

    while age < 0 :
        age = int(input("나이를 입력하세요 : "))

        if age < 0 :
            print("다시 입력하세요")
            continue

        else :
            if age >= 0 and age <= 3 or age > 65 :
                print("감사합니다. 티켓을 발행합니다")
                continue
            elif age < 14 :
                grade = 1
            elif age < 19 :
                grade = 2
            elif age < 66 :
                grade = 3

            print("귀하는 %d등급이며 요금은 %d 원 입니다" % (grade, price[grade]))

            cost = price[grade]

            payType = int(input("요금 유형을 선택하세요. (1: 현금, 2: 공원전용 신용카드) : "))
        
            if payType == 1 :
                cash = int(input("요금을 입력하세요 : "))
                changeCoin = cash - cost

            elif payType == 2 :
                cost = cost * 0.9
                if age >= 60 and age <= 65 :
                    cost = cost * 0.95
                changeCoin = 0
            
            if changeCoin < 0 :
                print("%d 원이 모자랍니다. 입력하신 %d 원을 반환합니다" % (changeCoin * -1, cash))

            elif changeCoin >= 0 :
                count = count + 1

                if count % 7 == 0 and freeDayTicket > 0 :
                    freeDayTicket = freeDayTicket - 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다.")
                    print("여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d 장" % freeDayTicket)
                    cost = 0

                if count % 4 == 0 and freeYearTicket > 0 :
                    freeYearTicket = freeYearTicket - 1
                    print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다.")
                    print("연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d 장" % freeYearTicket)

                if payType == 2 :
                    print("%d 원 결제되었습니다. 티켓을 발행합니다" % cost)
                elif changeCoin == 0 :
                    print("감사합니다. 티켓을 발행합니다")
                elif changeCoin >= 0 :
                    print("감사합니다. 티켓을 발행하고 거스름돈 %d 원을 반환합니다" % changeCoin)

                print("")

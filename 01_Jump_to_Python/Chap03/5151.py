# coding: cp949

price = [0,2000,3000,5000]

grade = 0
count = 0

freeDayTicket = 3
freeYearTicket = 5

while 1 :
    age = -1

    while age < 0 :
        age = int(input("���̸� �Է��ϼ��� : "))

        if age < 0 :
            print("�ٽ� �Է��ϼ���")
            continue

        else :
            if age >= 0 and age <= 3 or age > 65 :
                print("�����մϴ�. Ƽ���� �����մϴ�")
                continue
            elif age < 14 :
                grade = 1
            elif age < 19 :
                grade = 2
            elif age < 66 :
                grade = 3

            print("���ϴ� %d����̸� ����� %d �� �Դϴ�" % (grade, price[grade]))

            cost = price[grade]

            payType = int(input("��� ������ �����ϼ���. (1: ����, 2: �������� �ſ�ī��) : "))
        
            if payType == 1 :
                cash = int(input("����� �Է��ϼ��� : "))
                changeCoin = cash - cost

            elif payType == 2 :
                cost = cost * 0.9
                if age >= 60 and age <= 65 :
                    cost = cost * 0.95
                changeCoin = 0
            
            if changeCoin < 0 :
                print("%d ���� ���ڶ��ϴ�. �Է��Ͻ� %d ���� ��ȯ�մϴ�" % (changeCoin * -1, cash))

            elif changeCoin >= 0 :
                count = count + 1

                if count % 7 == 0 and freeDayTicket > 0 :
                    freeDayTicket = freeDayTicket - 1
                    print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�.")
                    print("���� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d ��" % freeDayTicket)
                    cost = 0

                if count % 4 == 0 and freeYearTicket > 0 :
                    freeYearTicket = freeYearTicket - 1
                    print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�.")
                    print("���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d ��" % freeYearTicket)

                if payType == 2 :
                    print("%d �� �����Ǿ����ϴ�. Ƽ���� �����մϴ�" % cost)
                elif changeCoin == 0 :
                    print("�����մϴ�. Ƽ���� �����մϴ�")
                elif changeCoin >= 0 :
                    print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d ���� ��ȯ�մϴ�" % changeCoin)

                print("")

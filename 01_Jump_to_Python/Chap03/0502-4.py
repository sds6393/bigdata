# coding: cp949
print("���� ��� ��� ���α׷�Ver4\n")

while 1 :
    age = -1
    while age < 0 :
        age = int(input('���̸� �Է��ϼ���.: '))

        grade=""
        fee=0

    if age <0:
        print('�ٽ� �Է��ϼ���.')
    else:
    
        if age < 4:
            grade='����'
            fee=0
        elif age < 14:
            grade='���'
            fee=2000
        elif age < 19:
            grade='û�ҳ�'
            fee=3000
        elif age < 66:
            grade='����'
            fee=5000
        elif age > 65:
            grade='����'
            fee=0
        print('���ϴ�[%s]����̸�����[%d]���Դϴ�.'%(grade,fee))

        form = int(input('��������� �����ϼ���.(1:����,2:���� ���� �ſ�ī��):'))
        if form == 1:
            print('�����������ϼ̽��ϴ�.')
            money = int(input('�ݾ��� �Է��ϼ���.: '))
            if money - fee < 0:
                print("%d�� ���ڶ��ϴ�. �Է� �Ͻ� %d�� ��ȯ�մϴ�."%(fee-money,money))
            elif money == fee:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            elif money - fee > 0:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ �մϴ�."%(money-fee))

        elif form ==2:
            fee = fee * 0.9
            if age >=60 and age <= 65:
                fee = fee * 0.95
            print('���� ���� �ſ�ī�带 �����ϼ̽��ϴ�.')
            print('[%d]�� �����Ǿ����ϴ�. Ƽ���� �����մϴ�.'%fee)
        print("")


        

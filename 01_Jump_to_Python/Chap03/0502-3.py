# coding: cp949
print("���� ��� ��� ���α׷�Ver2\n")

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

    money = int(input('���� �Է��ϼ���.: '))
    print('���ϴ�[%s]����̸�����[%d]���Դϴ�.'%(grade,fee))
    if money - fee < 0:
        print("%d�� ���ڶ��ϴ�. �Է� �Ͻ� %d�� ��ȯ�մϴ�."%(fee-money,money))
    elif money == fee:
        print("�����մϴ�. Ƽ���� �����մϴ�.")
    elif money - fee > 0:
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ �մϴ�."%(money-fee))

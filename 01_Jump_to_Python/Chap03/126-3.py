#coding:cp949

coffee_number = 10

menu="""
    1.Ŀ�Ǳ���
    2.Ŀ���ܷ�Ȯ��
    3.���α׷�����
�޴��� �����ϼ���: """
Enter number:


while True:
    money = int(input("���� �־� �ּ���: "))
    if money == 300:
        print("Ŀ�Ǹ� �ݴϴ�.")
        coffee_number = coffee_number -1
    elif money > 300:
        coffee_number = coffee_number -1
        print("�Ž����� %d�� �ְ� Ŀ�Ǹ� �ݴϴ�." %(money-300))
    else:
        print("�ݾ��� %d�� ���ڶ��ϴ�."%(money-300))
        print("���� �ٽ� �����ְ� Ŀ�Ǹ� ���� �ʽ��ϴ�.")


    print("���� Ŀ���� ���� %d���Դϴ�." %coffee_number)
    if not coffee_number:
        print("Ŀ�ǰ� �� ���������ϴ�.�ǸŸ� �����մϴ�.")
        break

#coding:cp949


money=int(input("�󸶸� ������ �ֽ��ϱ�?"))
card = input("ī�带 ���� �ϰ� �ֽ��ϱ�? (y/n) : ")
if card == 'y':
                card = True
else:
                card = False

if money >= 3000:
    print("��Ű��ó �ý� �м� ������ �м��մϴ�.")
    print("�м��� �Ϸᰡ �Ǿ����ϴ�.")
    print("�ý�Ž")
elif card == True:
    print("�ý�Ž")
else:
    print("�ѹ���")
   
print("���α׷�����")

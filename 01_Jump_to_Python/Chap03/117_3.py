#coding:cp949

money=int(input("�󸶸� ������ �ֽ��ϱ�?"))
card = input("ī�带 ���� �ϰ� �ֽ��ϱ�? (y/n) : ")
if card == 'y':
                card = True
else:
                card = False

if money >= 3000:
    print("�ý�")
else:
    if card == True:
#        print("�ý�")# ������ �ڵ��� ��� �ߺ�
        print("ī�� �ý�")# �ߺ� �ڵ� �ƴ� ��� ���
    print("�ѹ���")
    
print("���α׷�����")

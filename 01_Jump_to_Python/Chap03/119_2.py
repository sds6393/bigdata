#coding:cp949

money=int(input("�󸶸� ������ �ֽ��ϱ�?"))
card = input("ī�带 ���� �ϰ� �ֽ��ϱ�? (y/n) : ")
partnership = input("��Ű��ó �ý� �����Դϱ�? (y/n) : ")
if card == 'y':     card = True
else:               card = False
if partnership == 'y':     partnership = True
else:               partnership = False
                

if money >= 3000:
    print("�ý�")
else:
#    if card == True:
#        if partnership == True: <- 11�� ������ �����ϰ� ó���ǹǷ� ��ø�� if�� ������ʿ䰡����
#            print("ī�� �ý�")
#        else:
#            print("�ɹ��� ī�尡 �ƴϹǷ� �ѹ���.")
if card == True and partnership ==True:
#    if and partnership == True: << ���������� �����ؾ��� ���x
                print("�ýø� Ÿ���Ǽ� �ֽ��ϴ�.")
    else:
        print("�ѹ���")
   
print("���α׷�����")

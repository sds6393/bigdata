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
         
    print('���ϴ�[%s]����̸�����[%d]���Դϴ�.'%(grade,fee))

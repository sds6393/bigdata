# coding: cp949
#�Է�:����(Argument,Parameter)
#���:return(print�� �ǹ��ϴ°��� �ƴ�)
def my_sum1(num1,num2):#�Է�,������� ��� �����ϴ� ���̽�
    result = num1*num2
    return result #����,�����Ͻ� �������� ����

def my_sum2(num1,num2):#�Է¸� ���� �ϴ� ���̽�
    result = num1*num2
    print("%d+%d=%d"(num1,num2,result))#����� �ʿ���ų� ��� ó���ϰ��� �Ҷ�

def my_sum3():#��¸� ���� �ϴ� ���̽�
    #�Է��� �Լ��ȿ��� ó��
    num1 = int(input("ù��° ���� �Է��ϼ���"))
    num2 = int(input("�ι�° ���� �Է��ϼ���"))
    result = num1*num2
    return result

def my_sum4():#�Է�/���(return)�� ���� �ϴ� ���̽�
    #�Լ��ȿ��� ��� ���� ó��
    num1 = int(input("ù��° ���� �Է��ϼ���"))
    num2 = int(input("�ι�° ���� �Է��ϼ���"))
    result = num1*num2
    return result

num1 = int(input("ù��° ���� �Է��ϼ���"))#my_snm1
num2 = int(input("�ι�° ���� �Է��ϼ���"))
result = my_sum1(num1,num2)
print("%d*%d=%d"%(num1,num2,result))

num1 = input("ù��° ���� �Է��ϼ���")#my_snm2
num2 = input("�ι�° ���� �Է��ϼ���")
my_sum2(num1,num2)

my_sum4()#my_snm4

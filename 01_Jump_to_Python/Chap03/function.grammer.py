# coding: cp949
#�Է�:����(Argument,Parameter)
#���:return(print�� �ǹ��ϴ°��� �ƴ�)
def my_sum1(num1,num2):#�Է�,������� ��� �����ϴ� ���̽�
    result = num1*num2
    return result #����,�����Ͻ� �������� ����

def my_sum2():
    result = num1+num2
    return result

def my_sum2_1():
    num1 = num1+100
    result = num1+num2
    return result

def my_sum2_2():
    global num1
    num1 = num1+100
    result = num1+num2
    return result

def my_sum2_3(num1):
    num1 = num1+100
    result = num1+2
    return result

def my_sum3(num1,num2):
    result = num1+num2

num1 = int(input("ù��° ���� �Է��ϼ���: "))
num2 = int(input("�ι�° ���� �Է��ϼ���: "))
#result = my_sum1(num1,num2)
#result = my_sum2()
#result = my_sum2_1()
#result = my_sum2_2()
#result = my_sum2_3(num1)
my_sun3(num1,num2)
print("%d+%d=%d"%(num1,num2,result))
#print("num1: %d"%num1)

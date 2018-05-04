# coding: cp949
print("공원 요금 계산 프로그램Ver2\n")

age = int(input('나이를 입력하세요.: '))
grade=""
fee=0

if age <0:
    print('다시 입력하세요.')
else:
    
    if age < 4:
        grade='유아'
        fee=0
    elif age < 14:
        grade='어린이'
        fee=2000
    elif age < 19:
        grade='청소년'
        fee=3000
    elif age < 66:
        grade='성인'
        fee=5000
    elif age > 65:
        grade='노인'
        fee=0
         
    print('귀하는[%s]등급이며요금은[%d]원입니다.'%(grade,fee))

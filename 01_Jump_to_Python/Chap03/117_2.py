#coding:cp949


money=int(input("얼마를 가지고 있습니까?"))
card = input("카드를 소유 하고 있습니까? (y/n) : ")
if card == 'y':
                card = True
else:
                card = False

if money >= 3000:
    print("아키텍처 택시 분석 조건을 분석합니다.")
    print("분석이 완료가 되었습니다.")
    print("택시탐")
elif card == True:
    print("택시탐")
else:
    print("뚜벅이")
   
print("프로그램종료")

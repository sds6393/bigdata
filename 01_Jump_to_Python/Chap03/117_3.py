#coding:cp949

money=int(input("얼마를 가지고 있습니까?"))
card = input("카드를 소유 하고 있습니까? (y/n) : ")
if card == 'y':
                card = True
else:
                card = False

if money >= 3000:
    print("택시")
else:
    if card == True:
#        print("택시")# 동일한 코드일 경우 중복
        print("카드 택시")# 중복 코드 아닌 경우 허용
    print("뚜벅이")
    
print("프로그램종료")

#coding:cp949

money=int(input("얼마를 가지고 있습니까?"))
card = input("카드를 소유 하고 있습니까? (y/n) : ")
partnership = input("아키텍처 택시 전용입니까? (y/n) : ")
if card == 'y':     card = True
else:               card = False
if partnership == 'y':     partnership = True
else:               partnership = False
                

if money >= 3000:
    print("택시")
else:
#    if card == True:
#        if partnership == True: <- 11번 라인이 동일하게 처리되므로 중첩된 if를 사용할필요가없음
#            print("카드 택시")
#        else:
#            print("맴버쉽 카드가 아니므로 뚜벅이.")
if card == True and partnership ==True:
#    if and partnership == True: << 개별조건을 지정해야함 사용x
                print("택시를 타고가실수 있습니다.")
    else:
        print("뚜벅이")
   
print("프로그램종료")

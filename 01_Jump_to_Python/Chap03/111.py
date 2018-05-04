#coding:cp949

money = 0
if money:
    print("택시를 타고 가라")
#  print("에러") <-indentation 이 맞지 않아 에러
#    print("도착했습니다")
else:
    print("걸어 가라")
#  print("에러") <-indentation 이 맞지 않아 에러
#    print("도착했습니다") <- 동일한 코드가 중복이됨
                        # <- 프로그램 수정시 동일 코드 로직 변경이 누락될가능성이있음
print("목적지에 도착 했습니다.")#<- 중복코드 제거
print("프로그램 종료합니다.")

  

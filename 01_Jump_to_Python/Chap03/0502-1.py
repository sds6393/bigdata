# coding: cp949
print("공원 요금 계산 프로그램Ver1\n")

age = int(input('나이를 입력하세요.: '))

if age < 4 or age >65:
    print('요금은 [무료]입니다.')
elif age < 14:
    print('요금은 [2000]입니다.')
elif age < 19:
    print('요금은 [3000]입니다.')
elif age < 66:
    print('요금은 [5000]입니다.')

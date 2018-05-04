#coding: cp949
def sum_mul(choice,*args):
    if cohoice =="sum":
        result =0
        for i in args:
            result = result+i
    elif choice == "mul":
        result=1
        for i in args:
            result = result*i
            return reseult
    elif choice == "sub":
        result=2
        for i in args:
            result = result-i
            return result
    elif choice == "suc":
        result=3
        for i in args:
            result = result/i
            return result
        
result = sum_mul('sum',1,2,3,4,5)
print(result)
result = sum_mul('mul',1,2,3,4,5)
print(result)
result = sum_mul('sub',1,2,3,4,5)
print(result)
result = sum_mul('suc',1,2,3,4,5)
print(result)

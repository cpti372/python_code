# 문자열 판별하기 
def pre(s):
    result=[]
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result)==10
print(pre("0123456789"))
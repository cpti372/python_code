def list_avg(numlist):
    total=0
    for i in numlist:
        total+=i
    avg=total/len(numlist)
    return avg
print(list_avg([10,20,30]))

def max_score(numlist):
    score=[10,20,30]
    max=0
    for i in numlist:
        if i>max:
            max=i

    return max
print(max_score([10,20,30]))

#def fun1():
 #   a=10#지역변수가 전역변수 보다 우선순위가 높다 
  #  print("fun1은 값은 %d 입니다"%a)
#def fun2():
 #   print("fun2의 값은 %d입니다"%a)

#def longest(str1,str2,str3):
 #   if len(str1)<len(str2) and len(str2)<len(str3):
  #      longest=str3
   # elif len(str2)> len(str1) and len(str2)>len(str3):
    #    longest=str2
    #elif len(str1)>len(str1) and len(str1)>len(str2):
    #    longest=str1

#def fun1(v1,v2):
 #   result=v1+v2
  #  return result

def fun2(v1,v2,v3):
    result=v1+v2+v3
    return result

def fun3(*para):
    result=0
    for i in para:
        result+=i
    return result
print(fun2(10,20,30))
print(fun3(10,20,30,40))

kor_score=int(input("국어점수"))
eng_score=int(input("영어점수"))
math_score=int(input("수학점수"))
if kor_score==90 and eng_score==90 and math_score==90:
    print("you got A")
else:
    print("you got F")

def calavg(numlist):
    sum=0
    for i in numlist:
        sum+=i
    avg=sum/len(numlist)
    return avg
def passfail(numlist):
    if avg>=60:
        message="pass"
    else:
        message="fail"
    return message
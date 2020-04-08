#143
num=int(input("Enter number:"))
if(num%2==0):
    print("EVEN")
else:
    print("ODD")

#144
num=input("Enter number:")
year=2018
result=[]
result=list(num)
num_2=result[0]+result[1]
num2=int(num_2)+1900
if(year-num2>=65):
    print("old")
else:
    print("young")

#148
year=int(input("Enter year:"))
if(year%400==0 or (year%4==0 and year%100!=0)):
   print("윤년")
else:
   print("평년")

#151
st=input()
if(st[0] in 'aeiouAEIOU'):
   print("good")
else:
    print("nos")

#150
x=int(input())
y=int(input())
if((x>=50 and x<=100) and (y>=40 and y<=80)):
   print("in")
else:
   print("out")

#152
colors=["red","pink","green","hot pinke","dark blue"]
co=input()
if (co in colors):
   print("Sorry")
else:
   colors.append(co)
   print(colors)

#153
a=int(input())
b=int(input())
print("Nice") if a+b>=0.5*a*b else print('bad')

#154
a=int(input())
b=int(input())
c=int(input())
print(c) if(c<a) else print(a) if a<b else print(c) if c<b else print(b)

#155
a=int(input())
print("minus")if(a<0) else print("plus")
print("odd")if(a%2!=0) else print("even")
print("right")if(a%3==0) else print("false")

#156
str=input()
str_list=str.split(' ')
if(str_list[1]=='*'):
   num=int(str_list[0])*int(str_list[-1])
   print(num)

#157
import random
list1=['a','b','c','d']
print(list1)
random.shuffle(list1)
ch1=random.choice(list1) #한 개 아무거나 출력됨
print(ch1)

#158
import random
n=random.randrange(1,100)
while True:
   num=int(input("ENTER:"))
   if(n==num):
      print("Correct")
      break
   elif(n!=num):
      if(n>num):
         print("you have to put big one")
      else:
         print("you have to put small one")

#160
import random
k=round(random.random()*10,1)
print(k)


#161
a,b=input("두 정수를 입력하세요").split()
a=int(a)
b=int(b)
import random
k=random.randrange(a,b)
if(k<a or k>b):
   print("no integer")
else:
   print(k)

#162
import random
sum=0
result=[]
for i in range(4):
   k=random.randrange(10,20)
   result.append(k)
print(result)
for i in result:
   sum+=i
avg=sum/4
print(avg)
if(avg>15):
   print("Big")
else:
   print("Small")

#163
import random
n=random.randrange(1,2)
ans1=int(input("Enter 1 level:"))
if(n==ans1):
   print("right")
   n2=random.randrange(1,4)
   ans2=int(input("Enter 2 level:"))
   if(n2==ans2):
      print("right")
      n3=random.randrange(1,8)
      ans3=int(input("Enter 3 level:"))
      if(n3==ans3):
         print("Lucky")
      else:
         print("Bye")
   else:
      print("Fail")

else:
   print("Fail")

#164
import random
cars=['hyndai','kia','bmw','porshe']
print(cars)
random.shuffle(cars)
if(cars[0]=='hyndai'):
   print(True)
else:
   print(False)

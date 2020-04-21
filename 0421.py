#220
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[1])
print(matrix[0:2])
print(matrix[0][2])
print(matrix[2][0:2])

#221
matrix1=[]
for i in range(3):
    matrix1.append([i]*4)
print(matrix)

matrix2=[[0]* 3 for i in range(3)]
print(matrix2)

matrix3=[[0 for col in range(3) for row in range(3)]]
print(matrix3)

matrix4=list(i for i in range(10) if i%2==0)
print(matrix4)

values=[0,1,2,3,4]
matrix5=[v**2 for v in values]
print(matrix5)

matrix6=[v**2 for v in values if v%2==0]
print(matrix6)

#224
a= list(2*(i+1) for i in range(10))
print(a)

#225
array=[[0]*4 for i in range(4)]
for i in range(16):
    array[i//4][i%4]=i
for i in range(4):
    print(array[i])

#226
array=[[0]*5 for i in range(3)]
array[0]=[5,8,10,6,4]
array[1]=[11,20,1,13,2]
array[2]=[7,9,14,22,3]

for i in range(3):
    for j in range(5):
        print('%2d' %array[i][j],end=' ')
    print()

#227
a=[[j for j in range(i+1,i+6)] for i in range(5)]
a=[list(range(i+1,i+6)) for i in range(5)]
print(a)

#228
import random
array=[[0]*5 for i in range(5)]
for i in range(0,25):
    array[i//5][i%5]=random.randrange(0,26)
sum=0
for i in range(5):
    for j in range(5):
        print('%2d' %array[i][j],end=' ')
        sum+=array[i][j]
    print()
if(sum/25>12.5):
    print('Big')
else:
    print('small')


#251
def printHello(n):
    print('Hello')
    printHello(n-1) if n>1 else None
printHello(5)

#252
def sum1(n):
    result=0
    for i in range(1,n+1):
        result+=i
    return result

def sum2(n):
    if(n==1):
        return 1
    else:
        return n+sum2(n-1)
print(sum1(50),sum2(50))

#253
def fun(n):
    if n==0:
        return 1
    elif n%2==1:
        return fun(n-1)*2-1
    else:
        return fun(n-2)+3
for i in range(10):
    print(fun(i),end='')

#254
print()
def countdown(n):
    if n==0:
        print("끝")
    else:
        print(n,'끝났어')
        countdown(n-1)
countdown(5)

#255
def factorial(n):
    if(n==1):
        return 1 
    else:
        return n*factorial(n-1)
print(factorial(5))

#256
def is_palindrome(word):
    if len(word) <2:
       return True
    if word[0]!=word[-1]:
        return False
    return is_palindrome(word[1:-1])
word=input()
print(is_palindrome(word))

#257
def fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(6))

#259
def exp(a,n):
    if n==1:
        return a
    else:
        return a*exp(a,n-1)
print(exp(3,2))
print(exp(4,7))

#258
def evennum(a,b):
    if a>b+2:
        evennum(b,a)
    elif(b-a)//2>0 and a%2==1:
        print(a+1,end='')
    elif(b-a)//2>0 and a%2==0:
        evennum(a+1,b)
        
evennum(10,15)
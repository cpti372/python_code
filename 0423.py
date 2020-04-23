#229
n=input()
def upper(str):
    upp=0
    for i in range(len(str)):
        if('A'<=str[i]<='Z'):
            upp+=1
    return upp

def lower(str):
    low=0
    for i in range(len(str)):
        if('a'<=str[i]<='z'):
            low+=1
    return low

print('upper:',upper(n),'lower:',lower(n))
#230
n=input()
def rev(str):
    mylist=list(str)
    for i in range(len(str)//2):
        a=mylist[len(str)-i-1]
        mylist[len(str)-i-1]=mylist[i]
        mylist[i]=a
    for i in range(len(str)):
        print(mylist[i],end='')
print(rev(n))

#231
alphabet='ABCDEFGHIJKLMNOPQRUSTUVWXYZ'
alphabet=list(alphabet)
mystr=list(input().upper())
for i in alphabet:
    if not (i in mystr):
        print(i,end='') 
#232
def arr(n):
    list=[]
    for i in range(1,2*n):
        if(i%2!=0):
            list.append(i)
    for i in range(2*n,1,-1):
        if(i%2==0):
            list.append(i)
    return list

n=int(input())
print(arr(n))

#232 배열로 푼다면 
n=int(input())
num=[0]*(2*n)
for i in range(0,n):
    num[i]=i*2+1
for j in range(0,n):
    num[2*n-1-j]=2+2*j
print(num)

#233
#한 줄에 두개씩 받으려고 함
num1=input().split(' ')
num2=input().split(' ')
num3=input().split(' ')
#배열 선언
array=[[0]*2 for i in range(3)]
array[0]=[int(num1[0]),int(num1[1])]
array[1]=[int(num2[0]),int(num2[1])]
array[2]=[int(num3[0]),int(num3[1])]
#가로 평균 
for i in range(3):
    print((array[i][0]+array[i][1])//2,end=' ')
print()
#세로 평균 
sum=0
#세로 읽어주기 
for i in range(3):
    sum2=0
    for j in range(2):
        sum2+=array[i][j]
    sum+=sum2
    print(sum2//3,end=' ')
print()

#234
def sct(str):
    for i in range(len(str)):
        if str[i]!=str[len(str)-1-i]:
            return False
    return True
str=input()
print(sct(str))

#265
def sum(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if(n%10==0):
        return 5*sum(n-1)-7*sum(n-5)
    elif(n%2==0):
        return sum(n-1)+2
    elif(n%2!=0):
        return 2*sum(n-1)-1
k=int(input())
print(sum(k))

#266
def fibo_simil(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n==3:
        return 1
    else:
        return fibo_simil(n-1)+fibo_simil(n-2)

k=int(input())
print(fibo_simil(k))
        

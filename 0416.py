#187
for i in range(1,10):
    print('\n')
    for j in range(1,10):
        print(i,'X',j,"=",i*j)

#189
for i in range(0,12):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")

#190
for i in range(0,11):
    print(" "*(11-i),"*"*(i+1))

#191
for i in range(0,11):
    if(i>=5):
        print("*"*9)
    if(i<5):
        print("*"*(2*i+1))  

#192
for i in range(0,11):
    print(" "* (10-i),end=' ')
    print("*"*(2*i+1),end=' ')
    print(" "*(10-i))

#194
num=int(input())
big_prime=1
for i in range(1,num):
    isTrue=True
    for j in range(2,i):
        if(i%j==0):
            isTrue=False
    if isTrue:
        big_prime=i
print(big_prime)

#195
for i in range(0,10):
    for j in range(0,10):
        if(3*i+2*j==10):
            print(i,j)
#198
myset=set()
for a in range(1,100):
    for b in range(1,100):
        for c in range(1,100):
            if(a+b+c==100):
                myset.update({a,b,c})
print(len(myset))

#s1 = set([1,2,3])
#{1, 2, 3}, 리스트나 튜플로 접근해야함 

#s2 = set("Hello") -> {'e', 'H', 'l', 'o'}

#200
num=[1,2,3,4,5]
list=[]
for i in num:
    for j in num:
        for k in num:
            for l in num:
                for m in num:
                    nstr=str(i)+str(j)+str(k)+str(l)+str(m)
                    if len({i,j,k,l,m})==5:
                        list.append(int(nstr))
list.sort()
print(list[49])

#201
def sum(a,b):
    return a+b

def dofun(n):
    return('This is',n)
print(dofun(10))
print(sum(2,3))

#204
def starprint(n):
    print('*'*n)
n=int(input('enter'))
starprint(n)

#205
def ope(a,b):
    list=[]
    list.append(int(a+b))
    list.append(int(a-b))
    list.append(int(a*b))
    return list
    #return [a+b,a-b,a*b]
print(ope(10,1))

#207
list=[5,1,7,2,6,3]
def swap(i,j):
    a=list[i]
    list[i]=list[j]
    list[j]=a
    return list
i,j=3,5
swap(i,j)
print(list)

#208
def wid(a):
    s=a*a*3.14
    print('the surface is',s)

a=int(input())
wid(a)

#209
def wordlist(string):
    result=string.upper()
    return result.split(' ')
string=input()
print(wordlist(string))

#210
def fun(n):
    sum=0
    for i in range(1,n):
        sum+=i%5
    return sum
n=int(input())
print(fun(8))

#214
def ismulTh(n):
    return n%3==0

def ismulFive(n):
    return n%5==0
sum=0
for i in range(1,100000):
    if(ismulTh(i) or ismulFive(i)):
        sum+=i
print(sum)

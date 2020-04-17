#211
def gcd(n,m):
    if m>n:
        for i in range(n,2,-1):
            if(m%i==0 and n%i==0):
                break
        return i
    else:
        for i in range(m,2,-1):
            if(m%i==0 and n%i==0):
                break
        return i

def lcm(n,m):
    if m>n:
        for i in range(n,2,-1):
            if(m%i==0 and n%i==0):
                break
        return i*(n//i)*(m//i)

    else:
        for i in range(m,2,-1):
            if(m%i==0 and n%i==0):
                break
        return i*(n//i)*(m//i)
            
n=int(input())
m=int(input())
print(gcd(n,m))
print(lcm(n,m))

#212
def fun(n):
    print(''.join(reversed(n)))

n=input()
fun(n)

#213
def add(n):
    sum=0
    while n!=0:
        sum += n%10
        print('+', n%10 , end=' ')
        n=(n-(n%10))//10
    print('=',sum)
    return sum

n=int(input())
while n//10!=0:
    n=add(n)

#215
def pro(n):
    for i in range(0,10):
        case=0
        num=n
        while num!=0:
            if num %10 ==i: 
                case+=1
            num=num//10
        if case !=1:
            return False
    return True
n=int(input())
print(pro(n))

#216
def pro2(n):
    case=0
    for i in range(1,n+1):
        num=i
        while num%10==1:
            if num %10 ==1:
                case+=1
            num=num//10
    return case
n=int(input())
print(pro2(n))

#217
def d(n):
    sum=n
    while n!=0:
        sum=sum+n%10
        n=n//10
    return sum

def isSelfNum(n):
    bool=False
    for i in range(n):
        if(n==d(i)):
            bool=True
    return bool
n=int(input())
print(isSelfNum(n))


#218
def double(n):
    list=[]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(n==i**2+j**2+k**2):
                    list.append(i)
                    list.append(j)
                    list.append(k)
                    return list
                else:
                    return 'Sorry'
n=int(input())
print(double(n))

#219
def pro3(n):
    nstr=str(1/n)[2:]
    if len(nstr)<=10:
        return 0
    else:
        rec=''
        for i in nstr:
            rec+=i
            if rec == nstr[len(rec):2*len(rec)]:
                return rec
n=int(input())
print(pro3(n))
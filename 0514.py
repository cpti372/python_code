#235
a,b=input('Enter the number').split()
a=int(a);b=int(b)
array=[a,b]
for i in range(2,10):
    array.append(array[i-2]*array[i-1]%10)
print(array)

#237
a=input('sentence:').split()

for i in range(len(a)):
    print(i+1,a[i])

#240
a=input('Enter number')
alist=a.split(" ")

for i in range(len(alist)):
    alist[i]=int(alist[i])

for i in range(1,11):
    num=0
    for j in range(len(alist)):
        if alist[j]==i:
            num+=1
    print(num)

#241
a=input()
b=input()
def isSame(a,b):
    list1=list(a)
    list2=list(b)
    list1.sort()
    list2.sort()
    for i in range(min(len(list1),len(list2))):
        if list1[i] !=list2[i]:
            return False
    return True
print(isSame(a,b))
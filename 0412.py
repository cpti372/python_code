#165
i=5
print("count")
while i>=0:
    print(i)
    i-=1
print("Boom")

#166
i=1
while True:
    i+=1
    if 3<=i<=5:
        continue
    print(i,'번째')
    if i==7:
        break

#167
num=10
while num<=18:
    print(num)
    num+=2
    
#168
num=1
while num <=100:
    print(num,end=' ')
    num*=2

#169
print('\n')
while True:
    a=input('Enter the alphabet:')
    if(a=='q'):
        break
print('finish')

#170
a=int(input('first num:'))
b=int(input('seconde num:'))
i=1
for i in range(a,b):
    if(i%5==0):
        print(i)

#171
mylist=[1,5,4,9,2]
for i in mylist:
    print(i,end=' ')
print()
myTuple=(1,3,'red',(2,5))
for i in myTuple:
    print(i, end=' ')


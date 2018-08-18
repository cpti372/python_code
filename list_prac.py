#튜플, 딕셔너리 연습 
#튜플은 값 수정이 안된다는 점 파악/딕셔너리에서도 함수 사용 가능 
#051 유클리디안 거리
p1=(0,0)
p2=(5,5)
import math
square_x = abs(p1[0] - p2[0]) ** 2
square_y = abs(p1[1] - p2[1]) ** 2
d1=math.sqrt(square_x + square_y)
print(d1)

#052
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

#053
tuple=('1','2','3','4','5')
print(tuple[1])
print(tuple[4])

#054
#t = ('a', 'b', 'c')
#t=tuple(t[0].upper())+t[1:]
#t=tuple("".join(t).capitalize())
#print(t)

#055
t = ['a', 'b', 'c']
n=[1,2,3]
print(list(zip(t, n)))

#056
a=10
b=20
a,b=b,a
print(a,b)

#057
t = ('a', 'b', 'c', 'd', 'e')
print(t[1:3])

#058  비어있는 딕셔너리
#059
store={'melona':1000,'pollapo':2000}
print(store)

#060 특정 딕셔너리 값 가져오기

print(store['pollapo'])


#061 딕셔너리 값수정 
store['melona']=1300
print(store)
#062 딕셔너리와 리스트 합성 
inventory = {'Melona':[1000, 10], 'Pollapo':[1200, 7], 'Ppangppare':[1800, 6], 'Tankboy':[1200, 5], 'Heathunting':[1200, 4], 'Worldcorn':[1500, 3]}
print(inventory)
#063 딕셔너리 keys값 가져오기
print(inventory.keys())
print(inventory.values())

#064응용
icecream = {'Tankboy': 1200, 'Ppangppare': 1800, 'Worldcorn': 1500, 'Melona': 1000}
for i in icecream:
    if price==min(icecream.values()):
print(name)

#065 update 메소드 사용       
contact1.update(contact2)
contact = contact1
for k, v in contact1.items() :
    d.update({k:v})
for k, v in contact2.items() :
    d.update({k:v})

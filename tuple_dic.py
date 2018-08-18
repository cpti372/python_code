#071 리스트 응축
nums=[1,2,3,4,5]
a=[x*x for x in nums]
print(a)

#072 리스트 응축 2
nums=[1,2,3,4,5,6,7,8,9,10]
even=[x for x in nums if x%2==0]
odd=[x for x in nums]
print(even)
print(odd)

#073 file_search
files = ['a.txt', 'b.txt', 'exer.avi', 'sing.mp3', 'ultra.avi']
a=[f for f in files if f.endswith('txt')]
print(a)

#074
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
end_price = [10500, 10300, 10100, 10800, 11000]
daeshin=dict(zip(date,end_price))


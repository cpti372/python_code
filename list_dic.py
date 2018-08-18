#041 리스트 연습
movie=["공작","너의 결혼식","어벤져스"]
print(movie)

#042 dictionary
movie_rank = [{'닥터 스트레인지': (36.6, 7.7)},
              {'스플릿': (18.8, 8.1)},
              {'럭키': (12.7, 7.6)}]

#043 list 
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2
print(langs)

#044 리스트에서만 사용가능한 함수들 
nums = [1, 2, 3, 4, 5, 6, 7]
print(min(nums))
print(max(nums))

#045 리스트에서만 가능
nums = [2, 3, 1, 7, 10, 4, 5, 8]
print(sorted(nums))

#046
tlist=['2016-09-05', '2016-09-06', '2016-09-07', '2016-09-08', '2016-09-09']
tlist.reverse()
print(tlist)


#047
close_price_daeshin = [10000, 10500, 10300, 10700, 11100]
tot=0
for i in close_price_daeshin:
    tot+=i
avg=tot/5
print(avg)

#048
data = ['a', 'b', 'c', 'd', 'e']
print(tuple(data))

#049
nums = [1, 2, 3, 4, 5]
nums.remove(3)
nums.remove(5)
print(nums)

#050
items = ['000600', '034560', '003540', '039490']
mystr=(';').join(items)
print(mystr)


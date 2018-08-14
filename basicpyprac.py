total=0
for i in range(1,1000):
    if i%3==0:
        total+=i
    if i%5==0:
        total+=i
    if i%3==0 and i%5==0:
        total-=i
print(total)
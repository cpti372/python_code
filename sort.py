def insert(x,ss):
    left = []
    if ss == []:
        return [x]
    else:
        while ss!=[]:
            smallest = min(ss)
            if x>smallest:
                ss.remove(smallest)
                left.append(smallest)
            else:
                left.append(x)
        return left+x

def isort0(s):
    if s != []:
        return insert(s[0],isort0(s[1:]))
    else:
        return []

print((insert(9,[6,7,8,10])))
print(isort0([10,5,6]))
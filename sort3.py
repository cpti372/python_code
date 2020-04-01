def insert0(x,ss):
    if ss!=[]:
        if x>ss[0]:
            return [ss[0]]+insert0(x,ss[1:])
        else:
            return [x]+ss
    else:
        return [x]

            
def isort0(s):
    if s != []:
        return insert0(s[0],isort0(s[1:]))
    else:
        return []

print(insort0([10,2,6,7,1,5]))

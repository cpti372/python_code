def insert1(x,ss):
    def loop(ss,left):
        if ss != []:
            if x <= ss[0]:
                return left + [x] + ss
            else:
                return loop(ss[1:],left+[ss[0]])
        else:
            return left + [x]
    return loop(ss,[])

def isort0(s):
    if s != []:
        return insert1(s[0],isort0(s[1:]))
    else:
        return []

print(insert1(10,[2,4,3,1,5,9,7]))
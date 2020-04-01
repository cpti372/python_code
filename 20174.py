def remove(x,xs):
    if xs!="":
        if x!=xs[0]:
            return xs[0]+remove(x,xs[1:])
        else:
            return remove(x,xs[1:])
    else:
        return ""


print(remove('a','abracadabra'))
print(remove('z','abracadabra'))
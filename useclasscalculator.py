class Cal():
    def setdata(self,a,b):
        self.a=a
        self.b=b

    def div(self):
        result=self.a/self.b
        return result

    def sub(self):
        result=self.a-self.b
        return result

    def sum(self):
        result=self.a+self.b
        return result

    def mul(self):
        result=self.a*self.b
        return result

a=Cal()
b=Cal()
a.setdata(4,2)
print(a.sum())
b.setdata(7,8)
print(b.mul())
#클래스 이해하기
class Park():
    lastname='park'
    def setName(self,name):
        self.fullname=self.lastname+name
    def travel(self,where):
        self.where=where
        return "%s,%s여행을 가다."%(self.fullname,self.where)

pey=Park()
print(pey.lastname)
pey.setName("연수")

print(pey.travel("부산"))
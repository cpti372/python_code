#계산기 서비스
class Service:
    secret="day6"
   # def setname(self,name):
    #    self.name=name
    #바로 아이디를 부여받을 때 실행될 수 있는 모
    def __init__(self,name):
        self.name=name
    def sum(self,a,b):
        result=a+b
        print("%s님%s+%s=%s입니다."%(self.name,a,b,result))
pey=Service()
pey.setname('jae')
pey.sum(1,4)

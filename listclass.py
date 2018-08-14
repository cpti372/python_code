class Cal():

    def __init__(self,num_list):
        self.num_list=num_list

    def sum(self):
        total=0
        for i in self.num_list:
            total+=i
        return total
    
    def avg(self):
        total=self.sum()
        result=total/len(self.num_list)
        return result

cal1=Cal([1,2,3])
print(cal1.sum())
print(cal1.avg())

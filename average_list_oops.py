#from chardet.test import result
class Average:
    def average_cal(self,list):
        results=sum(list)/len(list)
        print(results)
        
a=Average()
a.average_cal([1,2,3,4,5])
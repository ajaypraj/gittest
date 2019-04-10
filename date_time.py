import time
import datetime
initial=time.time()
k=0
while k<10:
    print("Hi,Friends")
    #time.sleep(1)
    k+=1
    
print("Remaining time",time.time()-initial)
initial2=time.time()

for i in range(10):
    print("Hi,Friends")
    #time.sleep(1)
print("Remaining time",time.time()-initial2)
today=datetime.datetime.now()
print(today)
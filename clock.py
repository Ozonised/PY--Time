import time

def clock():
    while 1:
        localTime = ((time.ctime()).split())[3]
        print(localTime, end='\r')
        time.sleep(1)

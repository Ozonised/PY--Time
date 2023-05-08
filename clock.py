import time

def clock():
    while 1:
        print(time.strftime("%X"), end='\r')
        time.sleep(1)
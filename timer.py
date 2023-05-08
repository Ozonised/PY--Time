import time
import datetime

def timer(mode):
    while 1:
        hours = int(input("Enter hours:"))
        minutes = int(input("Enter minutes:"))
        seconds = int(input("Enter seconds:"))
        
        timerDuration = hours * 3600 + minutes * 60 + seconds
        
        print("Timer duration:",datetime.timedelta(seconds=timerDuration))
        
        input("Press ENTER to start timer")
        
        while timerDuration:

            remainingTime = datetime.timedelta(seconds=timerDuration)
            
            print(remainingTime, end='\r')
            
            time.sleep(1)
            timerDuration -= 1
        
        print("Timer ended")
        
        option = input("Press e to exit or ENTER to continue: ")
        if (option == 'e' or option == 'E'):
            break
            
    mode = 0
    return mode
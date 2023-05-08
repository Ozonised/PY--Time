import time

def calender(mode):
    while 1:
        # print the abbreviated day name, full month name, day and full year
        print(time.strftime("%a %B %d %Y"))
        option = input("q to exit: ")
        
        if (option == 'q' or option == 'Q'):
            break
        else:
            continue
        
    mode = 0
    return mode


def menu(mode):
    print("1. Clock")
    print("2. Stopwatch")
    print("3. Timer")
    print("4. Calender")
    print("5. Exit")

    while mode == 0:       
        mode = int(input("Select a option:"))
       
        if mode < 1 or mode > 5:
            print("invalid input")
            mode = 0
            continue
        else: 
            break
        
    return mode
from menu import menu
from clock import clock
from stopwatch import stopwatch
from timer import timer

PROGRAM_TITLE = "PY CLOCK"
print(PROGRAM_TITLE.center(30, '-'))
mode = 0

while (1):
    mode = menu(mode)

    if mode == 1:
        clock(mode)
    elif mode == 2:
        mode = stopwatch(mode)
    elif mode == 3:
        mode = timer(mode)
    elif mode == 5:
        print("Exiting Program")
        break
    else:
        mode = 0


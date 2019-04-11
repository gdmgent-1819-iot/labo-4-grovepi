import time
from grovepi import *

# connect the led bar to D7
bar = 7

# set the used pins to their desired state,
# we're setting them to output because we're writing to them
pinMode(bar,"OUTPUT")

# initialize the led bar in the desired mode, 
# puttin 0 instead of 1 will change the direction
ledBar_init(bar, 1)

# wait 1 second
time.sleep(1)

# make a variable that holds the current count
i = 0
while True:
    try:
        if(i > 10):
            i = 0

        # check the counter to set the led bar status
        if(i == 0):
            ledBar_setLevel(bar, 0)
        if(i == 1):
            ledBar_setLevel(bar, 1)
        if(i == 2):
            ledBar_setLevel(bar, 2)
        if(i == 3):
            ledBar_setLevel(bar, 3)
        if(i == 4):
            ledBar_setLevel(bar, 4)
        if(i == 5):
            ledBar_setLevel(bar, 5)
        if(i == 6):
            ledBar_setLevel(bar, 6)
        if(i == 7):
            ledBar_setLevel(bar, 7)
        if(i == 8):
            ledBar_setLevel(bar, 8)
        if(i == 9):
            ledBar_setLevel(bar, 9)
        if(i == 10):
            ledBar_setLevel(bar, 10)

        i = i + 1
        time.sleep(1)

    # when the program ends, turn off led and led bar
    except KeyboardInterrupt:
        ledBar_setLevel(bar, 0)
        break
    # notify if error occurs
    except IOError:
        print ("Error")

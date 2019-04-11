import time
from grovepi import *

# connect the led to D3
led = 3
# connect the led bar to D7
bar = 7

# set the used pins to their desired state,
# we're setting them to output because we're writing to them
pinMode(led,"OUTPUT")
pinMode(bar,"OUTPUT")

# initialize the led bar in the desired mode, 
# puttin 0 instead of 1 will change the direction
ledBar_init(bar, 1)

# wait 1 second
time.sleep(1)

# make a variable that holds the current count/pwm value
i = 0
while True:
    try:
        # reset the variable if it passes 255(max pwm value)
        if i > 255:
            i = 0
        # if smaller than 255, increase by 2
        i = i + 2

        # current brightness
        print (i)

        # give pwm output to the led
        analogWrite(led,i)

        # check the pwm value to set the led bar status
        if(i<26):
            ledBar_setLevel(bar, 1)
        if(i>26 and i<52):
            ledBar_setLevel(bar, 2)
        if(i>52 and i<78):
            ledBar_setLevel(bar, 3)
        if(i>78 and i<104):
            ledBar_setLevel(bar, 4)
        if(i>104 and i<130):
            ledBar_setLevel(bar, 5)
        if(i>130 and i<156):
            ledBar_setLevel(bar, 6)
        if(i>156 and i<182):
            ledBar_setLevel(bar, 7)
        if(i>182 and i<208):
            ledBar_setLevel(bar, 8)
        if(i>208 and i<234):
            ledBar_setLevel(bar, 9)
        if(i>234 and i<256):
            ledBar_setLevel(bar, 10)

        time.sleep(.1)

    # when the program ends, turn off led and led bar
    except KeyboardInterrupt:
        digitalWrite(led,0)
        ledBar_setLevel(bar, 0)
        break
    # notify if error occurs
    except IOError:
        print ("Error")

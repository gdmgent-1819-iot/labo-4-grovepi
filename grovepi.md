
# GROVEPI

GrovePi+ is een board met 15 Grove 4-pin connectoren welke de Grove sensoren naar de Raspberry Pi brengen. Het is een eenvoudig aan te sluiten en te gebruiken modulair systeem voor hardware hacking met de Raspberry Pi. Solderen of breadboards zijn overbodig, plug je Grove sensoren simpelweg in de GrovePi+ en je kunt direct beginnen met programmeren.

## Wat is het? 

De GrovePi+ is een uitbreidingsboard voor de raspberryPi. Het board bevat 15(!) connectoren om sensoren en andere hardware aan te sluiten. De externe hardware is apart verkrijgbaar. 

## Poorten

Het board bestaat uit 7 digitale poorten, 3 analoge, 3 I2C poorten, 1 seriële poort voor de grovepi en 1 voor de rapsberryPi. Dan heb je ook nog 1 poort die 5V output geeft.

## Connecteren met pi

![Image of Yaktocat](https://seeeddoc.github.io/GrovePiPlus/img/GrovePi_Wiki_1.JPG)

We connecteren ze door de GrovePi op de raspberry te zetten. Pas op en plaats de connector met zorg op de pinnetjes.

## Hardware

Je kan sensoren en andere hardware apart verkrijgen of samen met de GrovePi bestellen. Deze connecteer je dan met de GrovePi via de 4-pin connectoren. Je mag de hardware niet zomaar connecteren want zoals boven vermeld zijn niet al de poorten hetzelfde. 

![Image of Yaktocat](https://github.com/gdmgent-1819-iot/labo-4-grovepi/blob/master/pictures/Hardware.png)

### Connecteren 

Wanneer we de hardware gaan connecteren moeten we opletten wat we waar aansluiten. Bij elke aansluiting staat wat voor poort het is. 
De A-poorten zijn analoog, D-poorten zijn digitaal, verder heb je nog de seriële poort en de I2C-poorten.

![Image of Yaktocat](https://github.com/gdmgent-1819-iot/labo-4-grovepi/blob/master/pictures/poorten.png)

## Software setup

Op je raspberry, navigeer naar een map waar je de GrovePi files wilt installeren.

![Image of Yaktocat](https://github.com/gdmgent-1819-iot/labo-4-grovepi/blob/master/pictures/code1.png)

In die map clone je de GrovePi github repo door volgend commando uit te voeren:
```
git clone https://github.com/DexterInd/GrovePi
```

Dan krijg je volgende response:

![Image of Yaktocat](https://github.com/gdmgent-1819-iot/labo-4-grovepi/blob/master/pictures/code2.png)

Er is nu een GrovePi map aangemaakt, navigeer naar deze map door volgende commando’s uit te voeren: 

```
cd GrovePi
```

![Image of Yaktocat](https://github.com/gdmgent-1819-iot/labo-4-grovepi/blob/master/pictures/code3.png)

Installeer de GrovePi library door volgend commando uit te voeren:

```
curl -kL dexterindustries.com/update_grovepi | bash
```

![Image of Yaktocat](https://github.com/gdmgent-1819-iot/labo-4-grovepi/blob/master/pictures/code4.png)

Navigeer naar de Python map en voer de grovepi.py applicatie uit:

```
cd Software/Python
python grovepi.py
```

![Image of Yaktocat](https://github.com/gdmgent-1819-iot/labo-4-grovepi/blob/master/pictures/code5.png)

Als alles goed is verlopen krijg je bovenstaande response.

## Writing python

Hieronder vind je een voorbeeld programma om het ledje aan te sturen, sluit de led aan op poort D4. 

```
import time
from grovepi import *

led = 4

pinMode(led,"OUTPUT")
time.sleep(1)

while True:
    try:
        digitalWrite(led,1)
        time.sleep(1)

        digitalWrite(led,0)
        time.sleep(1)

    except KeyboardInterrupt:
        digitalWrite(led,0)
        break
```

de bovenstaande code zet je in een file met .py als extentie. In je terminal navigeer je dan naar waar dit bestand staat en voer je het volgende commando uit om het programma te runnen. 

```
Python led_blink.py
```

Bij het volgende programma maken we gebruik van de ledbar, elke seconde vult de ledbar met 1 led en na 10 seconde wordt deze gereset. Sluit de ledbar aan op D7.

```
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
```

de bovenstaande code zet je in een file en sla je op als ledbar_time.py. In je terminal navigeer je dan naar waar dit bestand staat en voer je het volgende commando uit om het programma te runnen. 

```
Python ledbar_time.py
```

Onderstaand programma laat een led uitdoven en toont de vooruitgang op de ledbar. Sluit de led aan op D3 en de ledbar op D7.

```
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
```

de bovenstaande code zet je in een file en sla je op als led_fade_progress.py. In je terminal navigeer je dan naar waar dit bestand staat en voer je het volgende commando uit om het programma te runnen. 

````
Python led_fade_progress.py
```
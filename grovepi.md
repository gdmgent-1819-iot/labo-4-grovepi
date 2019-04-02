
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
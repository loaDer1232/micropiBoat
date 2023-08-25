# MicroPI Boat 
MicroPI Boat is a rewrite of my former project for the micropi pico libray to make running it easier 

## Classes:
### servo.py:
this class provides an easy way to interface the pins on the pico and coverts the pin vaule into a 360 Degree so that i can pass it angles

### angelDetector.py:
takes an input and coverts into a angel vaules alowing us to easily use them to set points of sail  

## Hardware:
### Pi PICO W:
I decided to use the raspberry pi pico w as it was a microcomtroler that was with in the projects budget and also had all of the nessacery features to run the boat and with it being powered by the RP2040 microprocesseser it has more then enough grunt to get the job done
![PinOut for PicoPi W](https://www.raspberrypi.com/documentation/microcontrollers/images/picow-pinout.svg)
<sub>pinout for the pi pico w</sub>

### Other Hardware:
For the servos I chose to use the SG-5010 which has caused several problems for example I didnt realise that the minamum voltage was 4.8V when the deafualt power output on the pi pico was 3V so it had to make a bodge soultion
![pinout for SG-5010](https://protosupplies.com/wp-content/uploads/2018/03/Servo-Connections.jpg)         
<sub>pinout for the SG-5010</sub>
interstingly the wires I used where taken from cat-6e ethernet cables because it was cheaper than buyimg soldcore copper cables
# MicroPI Boat

MicroPI Boat is a rewrite of my former project for the micropi pico libray to make running it easier

## Set up:

the set up process for the use of the boat is simple but does have some setps that you must follow for correct function  
instructions:

1. find the voltage of your potentiometer when it is set to zero degrees. this is your offset
2. find the voltage of the potentiometer at 2 other angles. useing the formula:  
   $v_2 - v_1 \over   θ_2 -  θ_1$  
   e.g.  
   ${0.8 - 0.4 \over 200 - 50} = 0.004$  
    this finds the scale of the potentiometer this works if the potentiometer being used is linaer and is simpley $y = mx+c$ where ${y = θ}$
3. take the scale and offset values obtanied in step 2 and use these for the corrspoding values in angelDetector.py as well as the ADC pin you want to use if no scale and offset are provided then deafault values will be used  
   e.g.

```
detector = AngelDetecor(pin, scale=, offset=)
```

4. set the pins to be used for the main and jib servos

```
mainServo = Servo(pin1)
jibServo = Servo(pin2)
```

5. the program is ready to run

## Classes:

### servo.py:

this class provides an easy way to interface the pins on the pico and coverts the pin vaule into a 360 Degree so that i can pass it angles

### angelDetector.py:

takes a voltage from a potentiometer as input and coverts into a angel vaules alowing us to easily use them to set points of sail

### pathFinder.py:

takes the start and ending coorids and uses this to find the horozotal and vertacal vectors as well as the angle need for travel 
it finds the vectors using:  
$x_1 - x_2$ and $y_1 - y_2$ 
and the angel using:   
$θ = cos^{-1}({adjcent \over hypotonys})$ where adjacent =  and oppo

## Hardware:

### Pi PICO W:

I decided to use the raspberry pi pico w as it was a microcomtroler that was with in the projects budget and also had all of the nessacery features to run the boat and with it being powered by the RP2040 microprocesseser it has more then enough grunt to get the job done
![PinOut for PicoPi W](https://www.raspberrypi.com/documentation/microcontrollers/images/picow-pinout.svg)
<sub>pinout for the pi pico w</sub>

### Other Hardware:

For the servos I chose to use the SG-5010 because they have are standed interface and more than enough tourque to pull int the sails as showen in the pinout the servo uses 4.8-6V which is easily supplable using the same power source as the pico pi itself
![pinout for SG-5010](https://protosupplies.com/wp-content/uploads/2018/03/Servo-Connections.jpg)  
<sub>pinout for the SG-5010</sub><br>
the potentiometer I used was a 10KΩ class A linear potentiometer as it was cost effective  
interstingly the wires I used where taken from cat-6e ethernet cables because it was cheaper than buying soldcore copper cables

## wire diagram:

![wire diagram for pico boat](/Media/Capture.PNG)  
<sub>wire diagram for pico boat</sub>

## style guide:

1. varibles should be in camelCase and have type hints
2. functions are camelCase with \_ between each word and have type hints
3. classes have capatilas ate the start and for each word and have descriptions and Attributes
4. identation should be done with tabs

Example

```
def example_Function(foo: int, bar: str)-> str:
    fooBar: str = str(foo) + bar
    return fooBar

class ExampleClass:
    ''' this is an example
    Attributes:
    this: this is fake
    '''
```

# MicroPI Boat

MicroPI Boat is a rewrite of my former project for the micropi pico libray to make running it easier

## Set up:

the set up process for the use of the boat is simple but does have some setps that you must follow for correct function  
instructions:

1. find the voltage of your potentiometer when it is set to zero degrees. this is your offset
2. find the voltage of the potentiometer at 2 other angles. useing the formula:  
   $v_2 - v_1 \over   \theta_2 -  \theta_1$  
   e.g.  
   ${0.8 - 0.4 \over 200 - 50} = 0.004$  
    this finds the scale of the potentiometer this works if the potentiometer being used is linaer and is simpley $y = mx+c$ where ${y = \theta}$
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

takes a voltage from a potentiometer as input and coverts into a angel vaules useing: 
$\theta  = scale \times x + offset$
alowing us to easily use them to set points of sail

### pathFinder.py:

takes the start and ending coorids and uses this to find the horozotal and vertacal vectors as well as the angle need for travel
it finds the vectors using:  
$\Delta x = x_2 - x_1$ and $\Delta y = y_2 - y_1$   
and the angel using:  
$\theta = cos^{-1}({adjacent \over hypotenuse})$

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

## project managment:

I decided to use a waterfall project management tool as this project mainly relied on parts that required other parts to be finished first and would also for me to meet certain deadlines i set up this waterfall using a spreadsheet this tool was also appropriate as this was a solo project so i didn't need to manage others only myself
![water fall chart](/Media/Capture1.PNG)
As you can see in my project management and in the screenshots I split my project into several functions and classes E.g. there is a class that interfaces with the servos and another that interfaces with the potentiometer and i have split the main function into several subroutines. This allowed me to more easily manage and test the individual components
![deconsturcted functions](/Media/Capture2.PNG)
I have obveslay chosen to use git and github for version control here is a screen shot of my git tree I found:
![git tree](/Media/Capture3.PNG)

## Trialling components:

### Componet testing rules:

1. all values passed must be of the correct type E.g. Int, str, etc.
2. all values returened must be of correct type
3. all values passed must be in acepatble bounds
4. all values returned must be in acepatble bounds
5. if any of the above rules are breached an error be returned and the program be stoped

### Componet testing system:

1. pass all values with in acpteble range and check returened values are correct
2. pass values just outside acceptlble bounds and make sure errors are returned or otherwise handled

## Testing outcome:

### write up for protype test 1:

start of test:  
the boat is placed in to the lake the the pi is powered the boat begains to sail forward after the servo test is finished the boat begains to move sails erraticly boat is then retrived and i find that the potentometer and rudder servo have been damaged  
end of test  
test outcome: failed

## Relevant Implications:

the relevent implactions that I am consdiering are usablity, funcatnality and my end user requierments.
|implactions|explanation|way I have addressed it|
|:-:|:-:|:-:|
|usablity|||
|functoinality|||
|end-user requirements|||

## Evaluate

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

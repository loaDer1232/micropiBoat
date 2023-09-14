# MicroPI Boat

MicroPI Boat is a rewrite of my former project for the micropi pico libray to make running it easier

## Set up:

The set up process for the use of the boat is simple but does have some steps that you must follow for correct function  
instructions:

1. Find the voltage of your potentiometer when it is set to zero degrees. this is your offset
2. Find the voltage of the potentiometer at 2 other s. useing the formula:  
   $v_2 - v_1 \over   \theta_2 -  \theta_1$  
   E.g.  
   ${0.8 - 0.4 \over 200 - 50} = 0.004$  
    this finds the scale of the potentiometer this works if the potentiometer being used is linaer and is simpley $y = mx+c$ where ${y = \theta}$
3. Take the scale and offset values obtanied in step 2 and use these for the corrspoding values in angelDetector.py as well as the ADC pin you want to use if no scale and offset are provided then deafault values will be used  
   E.g.

```
detector = AngelDetecor(pin, scale=, offset=)
```

4. Set the pins to be used for the main and jib servos

```
mainServo = Servo(pin1)
jibServo = Servo(pin2)
```

5. The program is ready to run

## Front End:

The decision to integrate a front-end component into the system, enabling users to modify settings through a graphical user interface (GUI), was driven by a strong commitment to enhancing the user experience and streamlining the operation of the boat. This strategic move represents a pivotal step towards making the boat's functionality more accessible and user-friendly, as it empowers individuals to interact with the vessel without requiring any knowledge of the underlying codebase.

Implementing this front-end GUI created a user-friendly bridge between the boat's core functionality and its end user. This interface serves as a portal through which users can effortlessly adjust settings, customize preferences, and make real-time modifications, all without delving into the details of the boat's code. This approach dramatically lowers the entry barrier for users of varying technical backgrounds, making the boat accessible to a wider audience and ensuring that everyone can harness its full potential.
![front end screenshot](/Media/Capture4.PNG)

## Classes:

### servo.py:

This class provides an easy way to interface the pins on the pico and coverts the pin value into a 360 degree range so that it can pass at angles.

### angelDetector.py:

Takes a voltage from a potentiometer as input and coverts into a angle vaules using:
$\theta  = scale \times x + offset$
alowing us to easily use them to set points of sails.

### pathFinder.py:

Takes the start and ending coordinates and uses this to find the horizontal and vertical vectors as well as the  need for travel.
It finds the vectors using:  
$\Delta x = x_2 - x_1$ and $\Delta y = y_2 - y_1$  
and the  using:  
$\theta = cos^{-1}({adjacent \over hypotenuse})$

### settings.py

Allows users to use a GUI to alter the settings and have it passed to the main file as a JSON

## Hardware:

### Pi PICO W:

The choice to employ the Raspberry Pi Pico W as the microcontroller for this project stemmed from a thoughtful evaluation of various factors, including budget constraints and the technical requirements of the boat's operation. This selection reflects a judicious blend of affordability and functionality, making it a well-rounded choice for driving the boat's essential systems.

First and foremost, the Raspberry Pi Pico W was a prudent selection due to its budget-friendly nature. Cost considerations are often paramount in project development, and by opting for this microcontroller, we ensured that the project remained financially feasible without compromising on performance or features. This cost-effectiveness allows us to allocate resources to other critical aspects of the project, such as sensors, actuators, and safety measures.

Equally crucial, the Raspberry Pi Pico W possesses all the necessary features to effectively control and manage the boat's operations. Its compatibility with the boat's specific requirements, including sensor integration, communication protocols, and control logic, ensures a seamless fit within the project's ecosystem. This compatibility minimises the need for extensive hardware adaptations, streamlining the development process and expediting time-to-market.

Additionally, the Raspberry Pi Pico W's utilisation of the RP2040 microprocessor grants the project a substantial computational advantage. The RP2040 microprocessor is renowned for its computational prowess, offering ample processing power to handle the boat's multifaceted tasks with ease. This extra computational "grunt" translates into enhanced responsiveness, faster data processing, and the ability to accommodate future feature enhancements without the risk of resource constraints.

In summary, the decision to utilise the Raspberry Pi Pico W as the project's microcontroller is a well-founded choice that balances budgetary considerations with the essential technical requirements. It not only ensures cost-efficiency but also guarantees compatibility and robust performance, thanks to the RP2040 microprocessor's ample processing power. This strategic selection underscores a commitment to both fiscal responsibility and technical excellence in delivering a boat that operates efficiently and reliably.
![PinOut for PicoPi W](https://www.raspberrypi.com/documentation/microcontrollers/images/picow-pinout.svg)
<sub>pinout for the pi pico w</sub>

### Other Hardware:

The choice of the SG-5010 servos for this project was made after careful consideration of several crucial factors that play a pivotal role in the boat's performance. These servos were selected primarily for their well-established interface standards and the abundant torque they provide, which makes them ideally suited for the task of controlling the boat's sails. The decision to use these servos aligns seamlessly with the boat's requirements and design goals.

One of the key advantages of the SG-5010 servos lies in their standardised interface. This conformity to industry standards simplifies the integration process, allowing for straightforward connectivity and communication with the boat's control system. Compatibility with established interfaces not only reduces development complexity but also ensures a wide range of resources and documentation are available, facilitating ease of use and troubleshooting.

Moreover, the SG-5010 servos boast an impressive torque output, which is of paramount importance when it comes to controlling the boat's sails effectively. Their ample torque ensures that the sails can be manipulated with precision, even under varying wind conditions. This attribute guarantees the boat's ability to respond promptly to changing environmental factors, contributing to enhanced maneuverability and overall performance.

Another practical advantage of the SG-5010 servos is their power requirements. These servos operate within the voltage range of 4.8-6V, which conveniently aligns with the power supply used for the Raspberry Pi Pico W itself. This simplifies the power management setup, allowing for a streamlined and cohesive electrical system within the boat. It also ensures efficiency and reliability by reducing the need for multiple power sources or complex voltage regulation.
![pinout for SG-5010](https://protosupplies.com/wp-content/uploads/2018/03/Servo-Connections.jpg)  
<sub>pinout for the SG-5010</sub><br>

The potentiometer I used was a 10KΩ class A linear potentiometer as it was cost effective.

## wire diagram:

![wire diagram for pico boat](/Media/Capture.PNG)  
<sub>wire diagram for pico boat</sub>

## project managment:

In this project management scenario, I opted to utilise a waterfall project management tool due to the specific characteristics of the project. The decision to use a waterfall approach was based on the project's nature, which primarily involved dependencies between various components, each of which had to be completed before moving on to the next phase. Additionally, there were predefined deadlines that I had established for myself.

The choice to create a waterfall project management system using a spreadsheet was made for several reasons. First and foremost, the waterfall methodology is known for its sequential and linear approach, where one phase must be completed before the next can begin. This aligns well with projects that have clear dependencies and where tasks are interrelated, as was the case here. By using a spreadsheet, I could create a structured timeline of tasks and milestones, breaking the project into distinct phases, and clearly defining the order in which they needed to be accomplished.
![water fall chart](/Media/Capture1.PNG)
As you can see in my project management and in the screenshots I split my project into several functions and classes for example there is a class that interfaces with the servos and another that interfaces with the potentiometer.  I have also split the main function into several subroutines. This allowed me to more easily manage and test the individual components.
![deconsturcted functions](/Media/Capture2.PNG)
As is evidenced by this document I have chosen to use git and github for version control. Here is a screen shot of my git tree at one stage of development:
![git tree](/Media/Capture3.PNG)

## Trialling components:

### Componet testing rules:

1. All values passed must be of the correct type E.g. Int, str, etc.
2. All values returened must be of correct type.
3. All values passed must be in acepatble bounds.
4. All values returned must be in acepatble bounds.
5. If any of the above rules are breached an error be returned and the program be stopped.

### Componet testing system:

1. Pass all values with in acceptable range and check returened values are correct.
2. Pass values just outside acceptable bounds and make sure errors are returned or otherwise handled.

## Testing outcome:

### write up for protype 1 test:

Start of test:  
The boat is placed in to the lake the the pi is powered the boat begains to sail forward after the servo test is finished the boat begins to move sails erraticly boat is then retrived and I find that the potentiometer and rudder servo have been damaged  
end of test  
test outcome: failed

Start of test: (1/9/23)
Changes:
I ran the potentometer in a waterprofed boax and got the physical input though a rubber gasket to stop it being damged i also peremptively waterproofed the servos to pervent damage and refactored the code 
test:
The repaired boat was put into the hutt river and begains to drift down because of the current the the sails seem to be setting them selves correctly but dew to the unfouanatlly testing enviroment
end of test
test outcome: failed

Start of test: (16/8/23)
Changes:
I increesed the senitivie of voltage to angel calculator to make it sail fater and more direct
Test:
the boat is placed into into the wellington harbour and the sails set them selves correctly and it begains to move in the correct direction 
end of test
test outcome: successes

## Relevant Implications:

The relevent implictions that I am consdiering are usablity, functionality and my end user requierments.
|implactions|explanation|way I have addressed it|
|:-:|:-:|:-:|
|usablity|The usability of a boat stands as a pivotal aspect to consider when evaluating its overall worth and functionality. In essence, a boat's usability hinges on how well it caters to the needs and preferences of its intended users, which could encompass a diverse range of individuals. The significance of usability is underscored by the fact that even the most technologically advanced and feature-packed vessels may fall short of their potential if the information associated with them is not presented in a manner that resonates with the comprehension and comfort levels of the end users.| Incorporating a front-end component into the project I've developed has proven to be a game-changer, as it significantly enhances the ease of formatting data without causing any disruption to the existing code base. This strategic addition bridges the gap between the back-end data processing logic and the end users, offering a user-friendly interface that simplifies the data formatting process. This modular approach facilitates future updates and modifications, ensuring that the project can evolve and accommodate changing requirements without undue challenges.|
|functoinality|The paramount criterion for any product's success lies in its consistent and flawless performance, ensuring that it functions as intended every time it is used. This reliability and adherence to functionality standards are non-negotiable aspects of product development and are indicative of a commitment to user satisfaction and trust. Regrettably, the current state of this product falls short of the functionality standards I have set for myself.| While the product undoubtedly exhibits promise and potential, it has not yet reached the pinnacle of performance and reliability that I aspire to achieve. As a conscientious developer, I am dedicated to upholding the highest standards of quality and functionality, and I firmly believe that this product has the capacity to meet those standards with continued refinement and dedication.|
|end-user requirements|The importance of meeting the requirements set forth by my end users cannot be overstated, as they represent the purpose for which this product is being developed. These requirements serve as a direct reflection of the needs, preferences, and expectations of the individuals who will ultimately utilise the product. As a responsible and user-centric developer, my primary duty is to ensure that every single requirement outlined by the end users is not only acknowledged but meticulously addressed in the development process. The significance of adhering to these requirements lies in the fact that they encapsulate the core functionalities and features that will make the product not only relevant, but invaluable to its intended audience. These requirements serve as a compass, guiding the development efforts and aligning them with the precise needs of the end users. By meticulously fulfilling these stipulated criteria, I am not merely creating a product; I am crafting an indispensable solution that caters to the unique demands and challenges faced by the end users.|At this juncture in the development process, I am delighted to report that the majority of the specifications outlined by my end users have been successfully met. This accomplishment signifies a significant milestone in the project's journey, and it is a testament to the diligent efforts and unwavering commitment to aligning the product with the precise needs and expectations of its intended audience. The fact that most of the specifications have been fulfilled carries profound implications. It indicates that the project has passed a crucial litmus test by effectively translating the end users' vision into a tangible, functional reality. This alignment between design and execution is instrumental in ensuring the product's relevance and usability in addressing the real-world challenges faced by its intended users.|

## Evaluate:

The project has demonstrated its potential by identifying areas for future growth and development. The recognition of shortcomings in the initial test outcome is useful as it shows how to continue futher development.
This evaluation highlights many issues with my project management methodologies. The identified issues illustrate the need for a more robust project management approach.
While the project currently is a faliuire, its shows promise and the valuable lessons gained from both its successes and failures present an opportunity for growth and improvement through addressing the issues identified.

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

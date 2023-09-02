from tkinter import *
from settings import Settings

setRead = Settings("settingsFile.json")
window = Tk()
settings: dict[str: int] = setRead.readSettings()

startPoint = StringVar(value=settings["startPoint"])
endPoint = StringVar(value=settings["endPoint"])
mainServo = StringVar(value=settings["mainServo"])
jibServo = StringVar(value=settings["jibServo"])
rudderServo = StringVar(value=settings["rudderServo"])
detector = StringVar(value=settings["detector"])

enterStartPoint = Entry(window, width=7, textvariable=startPoint)
enterEndPoint = Entry(window, width=7, textvariable=endPoint)
enterMainServoPin = Entry(window, width=7, textvariable=mainServo)
enterJibServoPin = Entry(window, width=7, textvariable=jibServo)
enterRudderPin = Entry(window, width=7, textvariable=rudderServo)
enterDetectorPin = Entry(window, width=7, textvariable=detector)


def main() -> None:
    Label(window, text="Select Function", font=(
        "bold", 13)).grid(row=1,  column=3)

    Label(window, text="Start Point", font=("bold", 13)).grid(row=2,  column=1)
    enterStartPoint.grid(row=3,  column=1)
    Label(window, text="End Point", font=("bold", 13)).grid(row=2,  column=2)
    enterEndPoint.grid(row=3,  column=2)
    Label(window, text="Main Servo Pin", font=(
        "bold", 13)).grid(row=2,  column=3)
    enterMainServoPin.grid(row=3,  column=3)
    Label(window, text="Jib Servo Pin", font=(
        "bold", 13)).grid(row=2,  column=4)
    enterJibServoPin.grid(row=3,  column=4)
    Label(window, text="Rudder Servo Pin", font=(
        "bold", 13)).grid(row=2,  column=5)
    enterRudderPin.grid(row=3,  column=5)
    Label(window, text="Detector Pin", font=(
        "bold", 13)).grid(row=2,  column=6)
    enterDetectorPin.grid(row=3,  column=6)

    Button(window, text="Submit", command=appened,
           width=10, height=1).grid(row=4,  column=3)
    Button(window, text="Quit", command=exit,
           width=10, height=1).grid(row=4,  column=4)


def writeFile():
    global settings
    setRead.writeSettings(settings=settings)


def appened():
    settings["startPoint"] = enterStartPoint.get()
    settings["endPoint"] = enterEndPoint.get()
    settings["mainServo"] = enterMainServoPin.get()
    settings["jibServo"] = enterJibServoPin.get()
    settings["rudderServo"] = enterRudderPin.get()
    settings["detector"] = enterDetectorPin.get()
    writeFile()


main()
window.mainloop()

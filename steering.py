import RPi.GPIO as GPIO
from time import sleep

servo = 37

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo, GPIO.OUT)

pwm=GPIO.PWM(servo,50)

pwm.start(0)


def SetAngle(angle):
    pwm.start(0)
    duty = angle / 18 + 2
    GPIO.output(servo, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servo,False)
    pwm.ChangeDutyCycle(0)

def turnLeft():
    SetAngle(90)
    
    

def turnRight():
    SetAngle(15)
    

def straight():
    SetAngle(50)
    
#type: ignore
#Zachary Siller E4 9/15/2023
# Turn a servo 180 degrees to simulate rocket takeoff
import time
import board
import digitalio
import pwmio
from adafruit_motor import servo

ledg=digitalio.DigitalInOut(board.GP15)
ledg.direction=digitalio.Direction.OUTPUT
ledr=digitalio.DigitalInOut(board.GP16)
ledr.direction=digitalio.Direction.OUTPUT
btn = digitalio.DigitalInOut(board.GP19)
btn.pull = digitalio.Pull.DOWN
btn.direction = digitalio.Direction.INPUT
pwm_servo = pwmio.PWMOut(board.GP3, duty_cycle=2 ** 15, frequency=50) #Setup servo
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

servo1.angle = 0



print("Ready for launch")


while btn.value == False:
    pass
    
for x in range (10,0,-1): # "-1" makes counter count down, excludes 0, so stops at 1
    print(x)
    ledr.value=True
    time.sleep(.5)
    ledr.value=False
    time.sleep(.5)
        
    if x <= 1:
        print("Liftoff")
        servo1.angle=180 #rotates servo
        ledg.value=True
        time.sleep(2)
        ledg.value=False
        
    
        

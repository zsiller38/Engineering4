#type: ignore
#Zachary Siller E4 9/22/2023
#Record and print acceleration from mpu6050. Blink a light whenever the board is rotated more than 90 degrees.
import time
import board
import digitalio
import adafruit_mpu6050 
import busio

ledr=digitalio.DigitalInOut(board.GP16) #Lines 10-16 led set up
ledr.direction=digitalio.Direction.OUTPUT

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
tiltT = .5 #tilt variable 
ledr.value=False

while True:
    Acceleration = mpu.acceleration
    Xa,Ya,Za=Acceleration
    print(f" Acceleration X:{Xa:.3f}, Y:{Ya:.3f}, Z:{Za:.3f}.")    
    time.sleep(.1)
    if (tiltT) > (Za): #checks if the angular acceleration around the z axis is less than the tilt variable.
        ledr.value=True #this works because when the board is turned more than 90 degrees the z acceleration is less than the tilt var.
        print("led on")
        time.sleep(.1)
    else:
        ledr.value=False
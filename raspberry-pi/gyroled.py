#type: ignore
import time
import board
import digitalio
import adafruit_mpu6050 
import busio

ledr=digitalio.DigitalInOut(board.GP0) #Lines 7-10 led set up
ledr.direction=digitalio.Direction.OUTPUT

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
tiltT = .5
ledr.value=False

while True:
    Acceleration = mpu.acceleration
    Xa,Ya,Za=Acceleration
    print(f" Acceleration X:{Xa:.3f}, Y:{Ya:.3f}, Z:{Za:.3f}.")    
    time.sleep(.1)
    if (tiltT) > (Za):
        ledr.value=True 
        print("led on")
        time.sleep(.1)
    else:
        ledr.value=False
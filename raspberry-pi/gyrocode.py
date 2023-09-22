#type: ignore
#Zachary Siller E4 9/20/2023
#Use a mpu6060 to track angular accelertaion of the x, y, and z axis. Use an f string to print the data in a readable manner.
import time
import board
import digitalio
import adafruit_mpu6050 
import busio


sda_pin = board.GP15 #11-14 pin setup and initialization.
scl_pin = board.GP14
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)



while True
    Acceleration = mpu.acceleration #Reads the acceleration and decomposes it into x, y, and z
    Xa,Ya,Za=Acceleration
    print(f" Acceleration X{Xa:.3f}, Y{Ya:.3f}, Z{Za:.3f}.")    # prints the acceleration values and rounds the # using :.3f
#type: ignore
import time
import board
import digitalio
import adafruit_mpu6050 
import busio


sda_pin = board.GP15
scl_pin = board.GP14
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)



while True
    Acceleration = mpu.acceleration
    Xa,Ya,Za=Acceleration
    print(f" Acceleration X{Xa:.3f}, Y{Ya:.3f}, Z{Za:.3f}.")    
#type: ignore
#Zachary Siller E4 9/22/2023
#Record and print acceleration from mpu6050. Blink a light whenever the board is rotated more than 90 degrees.
import time
import board
import digitalio
import adafruit_mpu6050 
import busio

timeelapsed=time.monotonic() #starts time
tiltR=0

ledr=digitalio.DigitalInOut(board.GP16) #Lines 10-16 led set up
ledr.direction=digitalio.Direction.OUTPUT

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
tiltT = .5 #tilt variable 
ledr.value=False

with open("/data.csv", "a") as datalog: #opens the csv file to record data in
#only starts loop once the file is opened
    while True:
        Acceleration = mpu.acceleration
        Xa,Ya,Za=Acceleration    
        if (tiltT) > (Za): #checks if the angular acceleration around the z axis is less than the tilt variable.
            ledr.value=True #this works because when the board is turned more than 90 degrees the z acceleration is less than the tilt var.
            tiltR=1
            print("led on")
        else:
            ledr.value=False
            tiltR=0
        datalog.write(f"{timeelapsed},{Xa:.3f},{Ya:.3f},{Za:.3f},{tiltR}\n") #writes to the datalog and formats it using an f-string
        led.value=True
        time.sleep(0.125)
        led.value=False      
        datalog.flush()#clears the data log so the same data does not get recorded twice
        time.sleep(0.125)

    
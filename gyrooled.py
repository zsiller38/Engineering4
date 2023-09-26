#type: ignore
import time
import board
import digitalio
import adafruit_mpu6050 
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays() 

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

ledr=digitalio.DigitalInOut(board.GP0) #Lines 7-10 led set up
ledr.direction=digitalio.Direction.OUTPUT

tiltT = .5
ledr.value=False

splash = displayio.Group()
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area) 
display.show(splash)   


while True:
    Acceleration = mpu.acceleration
    Xa,Ya,Za=Acceleration
    
    print(f" Acceleration X:{Xa:.3f}, Y:{Ya:.3f}, Z:{Za:.3f}.")    
    
    avtext = f" Acceleration \n X:{Xa:.3f} \n Y:{Ya:.3f} \n Z:{Za:.3f}"
    text_area.text = avtext
    time.sleep(.1)
    
    if (tiltT) > (Za):
        ledr.value=True 
        print("led on")
        time.sleep(.1)
    
    else:
        ledr.value=False
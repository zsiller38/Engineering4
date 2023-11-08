#type: ignore
# Zachary Siller
# Landing Area Part 1 10/20/2023

import board
import digitalio
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import adafruit_display_shapes
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

displayio.release_displays()

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

splash = displayio.Group()
title = "Landing Area"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=2, y=5)
splash.append(text_area) 
display.show(splash)   

xaxisx1=0
xaxisx2=128
xaxisy1=32
xaxisy2=32
yaxisx1=64
yaxisx2=64
yaxisy1=0
yaxisy2=64

circle = Circle(64, 32, 2, outline=0xFFFF00)
splash.append(circle)
xaxis = Line(xaxisx1,xaxisy1,xaxisx2,xaxisy2, color=0xFFFF00)
splash.append(xaxis)
yaxis = Line(yaxisx1,yaxisy1,yaxisx2,yaxisy2, color=0xFFFF00)
splash.append(yaxis)

def trianglearea (x1y1, x2y2, x3y3):
    try:
        x1y1=x1y1.split(',')
        x2y2=x2y2.split(',')
        x3y3=x3y3.split(',')
    
        x1=float(x1y1 [0])
        y1=float(x1y1 [1])
        x2=float(x2y2 [0])
        y2=float(x2y2 [1])
        x3=float(x3y3 [0])
        y3=float(x3y3 [1])
        area = abs((1/2)*(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))
        if area == 0:
            print("not a triangle") 
            avtext = f"Not a triangle"
            text_area.text = avtext
        else:
            avtext = f" Area {area} km^2"
            text_area.text = avtext
            Tx1=x1+64
            Ty1=-y1+32
            Tx2=x2+64
            Ty2=-y2+32
            Tx3=x3+64
            Ty3=-y3+32
            triangle = Triangle(int(Tx1), int(Ty1), int(Tx2), int(Ty2), int(Tx3), int(Ty3), outline=0xFFFF00)
            splash.append(triangle)
            return area

    except:
        print("invalid input")
        avtext = f"Invalid input"
        text_area.text = avtext
        area = 0
        return area

while True:
    
    coord1 = input('Coordinates for point 1:')
    coord2 = input('Coordinates for point 2:')
    coord3 = input('Coordinates for point 3:')

    area = trianglearea(coord1, coord2, coord3)
    if area==0:
        continue
    
    else:
        
        print(f"The triangle with vertices ({coord1}), ({coord2}), ({coord3}) has area:{area} km^2")


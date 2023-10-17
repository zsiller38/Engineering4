# Engineering_4_Notebook

## Table of Contents
* [Basic Countdown](#basic_countdown)
* [LED Countdown](#led_countdown)
* [Button Countdown](#button_countdown)
* [Servo Countdown](#servo_countdown)

## Basic Countdown

### Description
Create a basic countdown using a for loop to count down from 10 and print liftoff when it reaches zero.

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/CountdownE4.gif?raw=true" alt="wiring2" style="width:318px;"> |     No wiring    |

### Code
 [BasicCountdown](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/countdown.py)


### Reflection
This was a good project to work off the circuit python rust. The code was nothing special but learning the syntax of for loops was interesting. Undestanding which way the for loop and the last number the loop would count led to my first iterations either counting up or stopping at 2. Other than that there was nothing unique about this first assignment. Using Circuit Python with Picos is so much better than with metros. Uploading and running my code actually works now and my board isn't constantly disconnecting like it did with Metro.

## LED Countdown

### Description
Use the same countdown but blink a red LED each time it counts down and a green led to signal liftoff.

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/LEDcountdownGif.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/CountdownLEDwiringFix.png?raw=true" alt="wiring2" style="width:318px; "> |

### Code
 [CountdownLED](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/countdownwithLED.py)

### Reflection
The second part of the countdown project used two LEDs that blink during the countdown. Intergrating the LEDs was very simple one is put in the for loop right after the numbers are printed the second goes inside the if statement checking if the countdown has ended.
``` python
print(x)   #Prints the number the for loop is on
    ledr.value=True #Turns light on and off
    time.sleep(.5)
    ledr.value=False
    time.sleep(.5)
```
``` python
if x <= 1:
        print("Liftoff") 
        ledg.value=True
        time.sleep(2)
```
Both of these steps only require a few lines of code. The hardest part was remembering how to initialize the LEDs in the setup. My repositories from last year came in handy as I was able to copy the setup from a previous assignment and change the pin numbers to get the LEDs working.

## Button Countdown

### Description
Rather than start the countdown when the code program is executed, use a button to start the countdown, while keeping the LEDs to signal each count and liftoff.

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/LEDButtonWiringFix.png?raw=true" alt="wiring2" style="width:318px; "> |

### Code
 [CountdownButton](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/countdownbtn.py)

### Reflection

## Servo Countdown

### Description
When the countdown code from the previous assignments is completed rotate a servo 180 degrees to simulate a rocket launch.

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/CountdownServoWiringFix.png?raw=true" alt="wiring2" style="width:318px; "> |

### Code
 [CountdownServo](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/countdownservo.py)

### Reflection
There was not much to this assignment. Controlling a servo is something I have been doing since starting engineering. I used the info in the assignment and repository from last year to copy and paste the setup and control commands. The servo command was inserted in the same loop that the liftoff led was in. 
``` python
if x <= 1:
        print("Liftoff")
        servo1.angle=180 #rotates servo
        ledg.value=True
```
That was all there was to this section of the rocket launch system. In conclusion, I enjoyed the Launch Pad assignment. Breaking it up into several small sections made it manageable and also helped establish a line of thought that helped me logically add each component one after the other. 
## Accelerometer

### Description
An MPU is a type of inertial measurement unit that can record acceleration and angular velocity in the x, y, and z directions. The MPU communicates with the PICO using the SDA and SCL pins. After communication is setup the data from the MPU is printed on the serial monitor. 

| **Evidence** | **Wiring** |
| ------ | ------ |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/MyProjectGif.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/MPUPicowiring.jpg?raw=true" alt="wiring2" style="width:318px;"> |

### Code
[Accelerometer](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/gyrocode.py)

### Reflection

## Accelerometer LED

### Description
Using the same MPU setup we will turn on an LED when the PICO and MPU are rotated 90 degrees vertically. This is done by detecting the change in acceleration in the x, y, and z directions. 

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/CrashAvoidanceP2Gif.gif?raw=true" alt="wiring2" style="width:318px;"> |  |

### Code
[LED Accelerometer](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/gyroled.py)

### Reflection
Adding an LED was interesting because it provided a use for the acceleration data rather than collecting it for the sake of collecting it. To detect when the MPU is flipped vertically you first need to know what the acceleration of the MPU is at rest. At rest, it experiences downward acceleration in the z-direction roughly equal to 9.8 (the acceleration due to gravity). The actual value I received was closer to 7.8 m/s^2, but that could be fixed with calibration. When the MPU is say flipped, the acceleration due to gravity is acting on a different axis. The acceleration in the z direction becomes zero. With this information, an if statement can check when z acceleration dips below a certain value, which indicates that the MPU has been flipped. 
 
## Accelerometer OLED

### Description
Using the previous code and wiring, integrate an OLED screen to display the rotational velocity values of the MPU. The OLED has five pins that need to be wired. A 3V3, Ground, RST, Data, and Clk. The Data and Clk pins are equivalent to SDA and SCL pins and get plugged into the same SCL and SDA ports that the MPU uses because they are I2C devices. To do this a separate code was run to find the address for the OLED and MPU. 

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/Gyrooled.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/MPUOLEDwriring.jpg?raw=true" alt="wiring2" style="width:318px;"> |

### Code
[OLED Accelerometer](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/gyrooled.py)

### Reflection
The OLED display was much harder to learn how to use than an LCD, but the OLED display is far more versatile. To use the OLED and I2C protocol I had to find the address of both the OLED and MPU. With only one I2C device this step is not necessary. Using this [code](https://drive.google.com/file/d/1YEmYYJnxZW2rdZCV6Mmu-fHIeQoKGVfL/view) we can print the addresses of both devices and by unplugging one we can find the address of the other. 
After that, I used the following code to set up the font size and color. 
``` python
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area) 
display.show(splash)
```
On another note, I had some trouble ordering my setup and imports. Specifically with the I2C device setup. If they are ordered wrong sometimes VS code says they are undefined but as long as you always define your variable for pins and addresses first there should be no issues.     

## Beam Design

### Description
The first onshape design of the year was part of a contest; design a beam that could support the most weight hanging from one end. The beam used a prebuilt anchor. The beam had to be 180 mm long and have a 12mm hole at the end for the weight to hang from. The design could not use any support material when printing so no part of the design could have an overhang greater than 45 degrees. Our design utilized an I-Beam-like shape that tapered down towards the end of the beam. The I-Beam used 45 rather than 90-degree angles to prevent overhangs. Holes were also created to make sure the beam was under the 13-gram requirement. 

### Evidence

 ![png](images/Beam.png)

### Reflection

Chris and Zach looked at the winning design from the previous year as a basis of design. Tomas Slinglove and Nathanial had a disign that used a lot of chamfers and triangles but after looking at ideal beam theory we realized that a curve would be better. With the added research we put in we created a I beam design with a downward curve.  
here is the link: https://cvilleschools.onshape.com/documents/a0f454c861c2691786377fa6/w/1d6220f831f8dcc8ccb014d1/e/326089d5b23fb66986b4e29d
&nbsp;

## beam 2
### Assignment Description

this one we designed the beam with the use of FEA.
### Evidence

 ![png](images/beam2.png)

### Reflection

This beam we used what we had found in the perviuos beam and perfect beam theory to greatly odify our old beam. We made the curve of the beam far less and strengthened the mounting area. The FEA seemed to say that we would break at the mounting area first but in reality we broke in the middle. WE also failed by bending past 35mm first so the next one we need to made it more brittle.  
here is the link: [https://cvilleschools.onshape.com/documents/a0f454c861c2691786377fa6/w/1d6220f831f8dcc8ccb014d1/e/326089d5b23fb66986b4e29d](https://cvilleschools.onshape.com/documents/a0f454c861c2691786377fa6/w/1d6220f831f8dcc8ccb014d1/e/943aaf02dd4e55416d91be8d)
&nbsp;

## beam 2
### Assignment Description

this one we designed the beam with the use of FEA after testing our last one
### Evidence

 ![png](images/beam3.png)

### Reflection

This beam we used what we had found in the perviuos beam and perfect beam theory to greatly odify our old beam. We made the curve of the beam far less and strengthened the mounting area. The FEA seemed to say that we would break at the mounting area first but in reality we broke in the middle. WE also failed by bending past 35mm first so the next one we need to made it more brittle.  
here is the link: [https://cvilleschools.onshape.com/documents/a0f454c861c2691786377fa6/w/1d6220f831f8dcc8ccb014d1/e/326089d5b23fb66986b4e29d](https://cvilleschools.onshape.com/documents/a0f454c861c2691786377fa6/w/1d6220f831f8dcc8ccb014d1/e/943aaf02dd4e55416d91be8d)


## Media Test

### Test Link
[Testcode](raspberry-pi/test.py)

### Test Image
![Food](images/download.jpg)  


### Test GIF
![DinoGif](images/dinoprepgif.gif) 

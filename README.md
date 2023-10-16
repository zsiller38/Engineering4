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
This was a good project to work off the circuit python rust. The code was nothing special but learning the syntax of for loops was interesting. Undestanding which way the for loop and the last number the loop would count lead to my first iterations either counting up or stopping at 2. Other than that there was nothing unique about this first assignment. Using circuit python with picos is so much better than with metros. Uploading and running my code actually works now and my board isn't constantly disconnecting like it did with metro.

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
When the countdown code from the previous assignments is completed rotate a servo 180 degrees to simulate rocket launch

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/CountdownServoWiringFix.png?raw=true" alt="wiring2" style="width:318px; "> |

### Code
 [CountdownServo](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/countdownservo.py)

### Reflection

## Accelerometer

### Description

| **Evidence** | **Wiring** |
| ------ | ------ |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/MyProjectGif.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/MPUPicowiring.jpg?raw=true" alt="wiring2" style="width:318px;"> |

### Code
[Accelerometer](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/gyrocode.py)

### Reflection

## Accelerometer LED

### Description

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/CrashAvoidanceP2Gif.gif?raw=true" alt="wiring2" style="width:318px;"> |  |

### Code
[LED Accelerometer](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/gyroled.py)

### Reflection

## Accelerometer OLED

### Description
Using the previous code and wiring, integrate an OLED screen to display the rotational velocity values of the MPU.

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/Gyrooled.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/MPUOLEDwriring.jpg?raw=true" alt="wiring2" style="width:318px;"> |

### Code
[OLED Accelerometer](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/gyrooled.py)

### Reflection


## Beam Design

### Description
The first onshape design of the year was part of a contest; design a beam that could support the most weight hanging from one end. The beam used a prebuilt anchor. The beam had to be 180 mm long and have a 12mm hole at the end for the weight to hang from. The design could not use any support material when printing so no part of the design could have an overhang greater than 45 degrees. Our disign utalized an I-Beam like shape that tappered down towards the end of the beam. The I-Beam used 45 rather than 90 degree angles to prevent overhangs. Holes were also created to make sure the beam was under the 13 gram requirement. 

## Media Test

### Test Link
[Testcode](raspberry-pi/test.py)

### Test Image
![Food](images/download.jpg)  


### Test GIF
![DinoGif](images/dinoprepgif.gif) 

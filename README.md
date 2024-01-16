# Engineering_4_Notebook

## Table of Contents
* [Basic Countdown](#Basic-Countdown)
* [LED Countdown](#led-countdown)
* [Button Countdown](#button-countdown)
* [Servo Countdown](#servo-countdown)
* [Accelerometer](#accelerometer)
* [Accelerometer LED](#accelerometer-led)
* [Accelerometer OLED](#accelerometer-oled)
* [Beam Part 1](#beam-part-1-no-fea)
* [Beam Part 2](#beam-part-2-fea)
* [Landing Area 1](#landing-area-1)
* [Landing Area 2](#landing-area-2)
* [Morse Code 1](#morse-code-1)
* [Morse Code 2](#morse-code-2)
* [Data Storage](#data-storage)
* [Data Analysis](#data-analysis)
  
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
Use the same countdown but blink a red LED each time it counts down and a green LED to signal liftoff.

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
Both of these steps only require a few lines of code. The hardest part was remembering how to initialize the LEDs in the setup. My repositories from last year came in handy as I could copy the setup from a previous assignment and change the pin numbers to get the LEDs working.

## Button Countdown

### Description
Rather than start the countdown when the code program is executed, use a button to start the countdown, while keeping the LEDs to signal each count and liftoff.

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/ButtonCountdowngif.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/LEDButtonWiringFix.png?raw=true" alt="wiring2" style="width:318px; "> |

### Code
 [CountdownButton](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/countdownbtn.py)

### Reflection
This was one of the harder assignments for me to complete. I was initially having trouble with the button logic and pullup and pulldown. Then I accidentally put my countdown for loop in my loop checking the button state so it either always ran or never ran. Once I got the for loop out of the button checking loop I kept getting error codes because there was nothing in the button checking loop. This is when L learned about [pass](https://www.w3schools.com/python/ref_keyword_pass.asp). Pass allows you to run a loop without actually doing anything. Think of it like a placeholder. When a loop is entered with a pass in it it will exit the loop and return to the start of the code. It allowed me to run my button-checking loop and reset to the start of the code each time the button was not pressed rather than continuing on to the for loop. 
``` python
while btn.value == False: #Always checks if button has been pressed or not
    pass #Allows loop to function without something in it
```

## Servo Countdown

### Description
When the countdown code from the previous assignments is completed, rotate a servo 180 degrees to simulate a rocket launch.

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/servocoundowngif.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/CountdownServoWiringFix.png?raw=true" alt="wiring2" style="width:318px; "> |

### Code
 [CountdownServo](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/countdownservo.py)

### Reflection
There was not much to this assignment. Controlling a servo is something I have been doing since starting engineering. I used the info in the assignment and repository from last year to copy and paste the setup and control commands. The servo command was inserted in the same loop that the liftoff LED was in. 
``` python
if x <= 1:
        print("Liftoff")
        servo1.angle=180 #rotates servo
        ledg.value=True
```
That was all there was to this section of the rocket launch system. In conclusion, I enjoyed the Launch Pad assignment. Breaking it up into several small sections made it manageable and also helped establish a line of thought that helped me logically add each component one after the other. 

## Accelerometer

### Description
An MPU is a type of inertial measurement unit that can record acceleration and angular velocity in the x, y, and z directions. The MPU communicates with the PICO using the SDA and SCL pins. After communication is set up the data from the MPU is printed on the serial monitor. 

| **Evidence** | **Wiring** |
| ------ | ------ |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/MyProjectGif.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/MPUPicowiring.jpg?raw=true" alt="wiring2" style="width:318px;"> |

### Code
[Accelerometer](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/gyrocode.py)

### Reflection
The hardest part of using an MPU was the setup and libraries. After that getting data from it was easy. Figuring out how to format that data is where I used [f-strings](https://realpython.com/python-f-strings/). F-strings are a formatting syntax. They are very readable, unlike %-formating, and allow you to call functions which is useful while printing and changing numbers. This is how I used f-strings.
``` python
print(f" Acceleration X{Xa:.3f}, Y{Ya:.3f}, Z{Za:.3f}.")
```
The :.3f rounds the number to 3 decimal places. 

## Accelerometer LED

### Description
Using the same MPU setup we will turn on an LED when the PICO and MPU are rotated 90 degrees vertically. This is done by detecting the change in acceleration in the x, y, and z directions. 

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/CrashAvoidanceP2Gif.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/MPUledwiring.jpg?raw=true" alt="wiring2" style="width:318px;"> |

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

## Beam Part 1 (No FEA)

### Description
The first onshape design of the year was part of a contest; design a beam that could support the most weight hanging from one end. The beam used a prebuilt anchor. The beam had to be 180 mm long and have a 12mm hole at the end for the weight to hang from. The design could not use any support material when printing so no part of the design could have an overhang greater than 45 degrees. Our design utilized an I-Beam-like shape that tapered down towards the end of the beam. The I-Beam used 45 rather than 90-degree angles to prevent overhangs. Holes were also created to make sure the beam was under the 13-gram requirement. 

### Evidence
| [**CAD Model**](https://cvilleschools.onshape.com/documents/a0f454c861c2691786377fa6/w/1d6220f831f8dcc8ccb014d1/e/326089d5b23fb66986b4e29d) | **FEA Analysis** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/V1.png?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/V1FEA.png?raw=true" alt="wiring2" style="width:318px;"> |

### Reflection

We began by looking at the winning design from the previous year as a basis for our design. Tomas Slinglove and Nathaniel had a design that used a lot of chamfers and triangles but after looking at ideal beam theory we realized that a curve would be better. With a [cantilever beam](https://en.wikipedia.org/wiki/Euler%E2%80%93Bernoulli_beam_theory#Cantilever_beams)
, if a force is applied at the end, the stress of the beam increases as you get farther from the force point. So the beam must taper as it gets closer to the end to account for that. With the added research we put in we created an I-beam design with a downward curve. We also added holes throughout the beam to reduce weight. 

## Beam Part 2 (FEA)

### Assignment Description
After designing our first beam we used onshapes built-in simulation tools to improve our initial design. After redesigning our beam it was tested and then the process of redesign and testing was repeated an additional time. The FEA simulation was run using a force of 30 newtons for consistent results and the force was applied on the mounting face.

### Evidence
| [**CAD Model**](https://cvilleschools.onshape.com/documents/a0f454c861c2691786377fa6/w/1d6220f831f8dcc8ccb014d1/e/943aaf02dd4e55416d91be8d) | **FEA Analysis** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/V2.png?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/V2FEA.png?raw=true" alt="wiring2" style="width:318px;"> |

### Test Videos
| **Test 1** | **Test 2** |
| ----- | ----- | 
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/V1testG.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/V2testG.gif?raw=true" alt="wiring2" style="width:318px;"> |

### Reflection Test 1

After running FEA on our original design we found that our I-beam was thicker and stronger than necessary, but the tip of our beam was too weak and would snap off. For this beam, we used what we had found in the previous beam and perfect beam theory to greatly modify our old beam. We made the curve of the beam far less and strengthened the mounting area. The reasoning behind this was to prevent the beam from breaking where it mounts to the anchor block and prevent the tip from breaking off. The FEA seemed to say that we would break at the mounting area first but in reality, we broke in the middle. We also failed by bending past 35mm first so for the next one we need to decrease the displacement.  


### Reflection Test 2

While testing our first beam we found that it broke not only in the middle but also horizontally where the upper I meets the base of the beam. To fix this we added braces connecting the base and top of the beam. Throughout the second design, we struggled to find meaningful ways to decrease the displacement, and going into the test Zach was skeptical about how much our beam had actually improved. The beam ended up holding 4.8 kg before displacing an improvement of 1.3 kg. We think this was due to inaccuracies in the FEA and the fact that Chris loaded the weights faster. This reduced the time the beam was under stress and therefore prevented the beam from gradually growing weaker as small cracks and breaks formed. In conclusion, our beam was very well-designed and strong. We cannot overstate how helpful variables are in designs you are constantly iterating. Use them when you can. 

## Landing Area 1

### Description
This assignment did not require any physical components and was done entirely within VS code. The primary goal was to get experience using functions and to achieve that requirement the code uses a function to turn 3 coordinates inputted by the user into the area of a triangle. Three new functions `input()`, `split()`, and `try`/`except` allow the code to accept input, split the input into x and y coordinates, and check for syntax errors.

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/landingarea1.gif?raw=true" alt="wiring2" style="width:318px;"> | No Wiring |

### Code
[Landing Area](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/Landingarea.py)

### Reflection
Landing Area Part 1 was in my opinion one of the more challenging assignments of the year because of the number of new functions and components. The underlying purpose was to familiarize myself with functions and how they can be used. In this case, I used a function that took the three coordinates inputted by the user and calculated the area of the triangle using [this equation](https://www.cuemath.com/geometry/area-of-triangle-in-coordinate-geometry/). The function would then return that area to be displayed on the serial monitor. Within that function there were the split function, try function, and float function. The split function was used to split the input coordinate among the x and y components. The try function is used to check if the input is valid in relation to the input parameters; if not it exits the function with and error message. Finally, float converts values into floating decimals to be put into the equation for the triangle area. 

## Landing Area 2

### Description
Integrate a small OLED screen to display the plotted triangles and area. The previous assignment takes the input of three coordinates to calculate the area of the triangle created. The OLED is used to plot the points and display the created triangle and its area. The code also required the adafruit_display_shapes library to plot the triangle and x and y-axis.

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/LandingAreaOLEDF.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/LandingareaOLEDwiring.jpg?raw=true" alt="wiring2" style="width:318px;"> |

### Code
[Landing Area OLED](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/OLEDLanding.py)

### Reflection
Getting the OLED to display the triangles was more of a troubleshooting problem than code difficulty. I used my previous OLED assignments to retrieve the setup code and then simply inserted the plotting commands in the various code loops. One thing to note is the OLED does not use what one would traditionally think of as a coordinate grid with the origin in the center. Instead, the OLED origin is in the top left corner, so the center of the screen is (64,32). To plot the points correctly which are given in the form of a traditional coordinate grid, 64 was added to every x coordinate and 32 to every y. This accounts for the OLED origin in the top left corner. 

## Morse Code 1

### Description
This code will take any written input and translate it into Morse code. A Morse code directory is used to store the character translations. Each character is individually translated by passing it through `for element in string_name:`. In the output string, the characters are separated by spaces and the words by a slash. If the user types -q the code will exit the loop using `break`.

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/morsecode1.gif?raw=true" alt="wiring2" style="width:318px;"> | No Wriring |

### Code
[Morse Code Translation](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/morsecode.py)

### Reflection
The most interesting part of this assignment was using a Python dictionary. This was the first time I had used one but, its uses became quickly apparent. A dictionary allows you to call information in this case a translation when it is needed. This is what allowed us to translate the input text letter by letter. Here is more info on a [python dictionary](https://www.w3schools.com/python/python_dictionaries.asp). Another important command was `break`. When this command is used the current loop or function will be exited. In this situation it was used to exit the translating prompt when -q was entered. 

## Morse Code 2
This project is an extension of the previous one. Now an LED is blinked at varying intervals to transmit the message. Five variables are used for the timing. Two for how long the LED should turn on for a dot and a dash, two determine how long the code should pause for a gap between characters and words, and the final one for the time in between dots and dashes.

### Description

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/morsecodeLED.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/morsecodeLEDwiring.jpg?raw=true" alt="wiring2" style="width:318px;"> |

### Code
[Morse Code Transmission](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/morsecodeLED.py)

### Reflection
There is not much to say about this assignment as it only involved blinking a light to transmit a Morse code message. Blinking LEDs were one of the first things I learned to do so I got through it pretty quickly. Even though it was easy the end result of this project was one of my favorites this year apart from the landing area one. There was something very satisfying about watching the LED blink away. 

## Data Storage

### Description
A pico has MB of onboard storage. Using an MPU 6050 data acceleration data will be recorded and saved to the pico to be downloaded. The wiring and code are exactly the same as the original MPU 6050 project except for a small switch and lines that open a CSV file and insert our data into the file. The pico cannot download data and upload code at the same time so the switch is used to change between "data mode" and "code mode". A boot.py file is used to switch between data and code mode when the pico boots up. Data mode is shown by 10 fast blinks of the onboard LED and code mode is three long blinks. 

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/morsecode1.gif?raw=true" alt="wiring2" style="width:318px;"> | <img src="https://github.com/zsiller38/Engineering4/blob/main/images/20240116_153317.jpg?raw=true" alt="wiring" style="width:318px;"> |

### Code
[Data Storage](https://github.com/zsiller38/Engineering4/blob/main/raspberry-pi/datasaving.py)

### Reflection
For this assignment, the execution of switching between code and data mode was the hardest part. After a couple of years of coding, it has become intuitive to just run your code and see if it works. But with this project, after you upload your code you have to shut off your pico and change to data mode to actually record data. There were many times I uploaded and ran my code but no data file was created because I never switched the pico into data mode. The process for switching the mode was to unplug the pico flip the switch restart the pico and then replug the pico to download your data. this restarts the pico which is needed for it to start running in data mode. Other than that opening and downloading data to a CSV file. This assignment will be very useful once we begin our pi in the sky project because it is essentially the same procedure for recording data. 

## Data Analysis

### Description
Use the CSV data collected in the previous assignment to create two graphs to represent data. One graph will use a line graph to display the x, y, and z acceleration on the y-axis and time on the x-axis. The other will show whether the tilt factor is 0 or 1 denoting if the board has been tilted 90 degrees from the horizontal. 

| **Evidence** | **Wiring** |
| ----- | ----- |
| <img src="https://github.com/zsiller38/Engineering4/blob/main/images/Tilt%20Meter.png?raw=true" alt="wiring2" style="width:318px;" > <img src="https://github.com/zsiller38/Engineering4/blob/main/images/Zachary's%20MPU%20Data.png?raw=true" alt="wiring2" style="width:318px;" > | No Wriring |

### Code
No code, instead link to [data spreadsheet](https://docs.google.com/spreadsheets/d/1XrMvou4HHuxYgN3jNSytNLNSUDwSCTC8cPH6FZub-vQ/edit#gid=0)

### Reflection
This section was a good conclusion to the data collection analysis. When collecting data, you often need to create a way to display the data in tables or graphs. I have used google sheets many times so the process of making graphs was not challenging but it still allowed me to understand the data I collected in a clear manner. 

## Media Test

### Test Link
[Testcode](raspberry-pi/test.py)

### Test Image
![Food](images/download.jpg)  

### Test GIF
![DinoGif](images/dinoprepgif.gif) 

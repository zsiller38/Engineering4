#type: ignore
#Zachary Siller E4 9/14/2023
# Trigger the countdown using a button 

import time
import board
import digitalio
ledg=digitalio.DigitalInOut(board.GP15)
ledg.direction=digitalio.Direction.OUTPUT
ledr=digitalio.DigitalInOut(board.GP16)
ledr.direction=digitalio.Direction.OUTPUT
btn = digitalio.DigitalInOut(board.GP19)
btn.pull = digitalio.Pull.DOWN
btn.direction = digitalio.Direction.INPUT
print("Ready for launch")


while btn.value == False: #Always checks if button has been pressed or not
    pass #Allows loop to function without something in it
    
for x in range (10,0,-1): # 21-32 same as previous LED countdown
    print(x) # "-1" makes counter count down, excludes 0, so stops at 1
    ledr.value=True
    time.sleep(.5)
    ledr.value=False
    time.sleep(.5)
        
    if x <= 1:
        print("Liftoff")
        ledg.value=True
        time.sleep(2)
        ledg.value=False
    
        

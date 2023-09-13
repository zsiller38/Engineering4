#type: ignore
#Zachary Siller E4 9/12/2023
# Same as rocket countdown but now using a red light to signal each count and a green light when liftoff occurs
import time
import board
import digitalio
ledg=digitalio.DigitalInOut(board.GP15) #Lines 7-10 led set up
ledg.direction=digitalio.Direction.OUTPUT
ledr=digitalio.DigitalInOut(board.GP16)
ledr.direction=digitalio.Direction.OUTPUT

for x in range (10,0,-1): #For loop will start counting down from 10 and stop at 1
    print(x)   #Prints the number the for loop is on
    ledr.value=True #Turns light on and off
    time.sleep(.5)
    ledr.value=False
    time.sleep(.5)
    if x <= 1:
        print("Liftoff") 
        ledg.value=True
        time.sleep(2)
        

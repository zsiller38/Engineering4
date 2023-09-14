#type: ignore
import time
import board
import digitalio
ledg=digitalio.DigitalInOut(board.GP15)
ledg.direction=digitalio.Direction.OUTPUT
ledr=digitalio.DigitalInOut(board.GP16)
ledr.direction=digitalio.Direction.OUTPUT
btn = DigitalInOut(board.GP19)
btn.pull = digitalio.Pull.UP
btn.direction = Direction.INPUT
countdown=False

if btn.value == True
   
    for x in range (10,0,-1):
        print(x)
        ledr.value=True
        time.sleep(.5)
        ledr.value=False
        time.sleep(.5)
        if x <= 1:
            print("Liftoff")
            ledg.value=True
            time.sleep(2)
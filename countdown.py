#type: ignore
import time
import board
import digitalio
led=digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT
Icount=1 

for x in range (0,10):
    print(Icount)
    time.sleep(1)
    Ncount=Icount+1
    Icount=Ncount



print ("liftoff")
    
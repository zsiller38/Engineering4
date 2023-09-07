#type: ignore
import time

for x in range (10,0,-1):
    print(x)
    time.sleep(1)
    if x == 1:
        print("Liftoff")
#type: ignore
#Zachary Siller E4 9/6/2023
#Rocket countdown from 10 using the serial monitor
import time

for x in range (10,0,-1): #For loop will start counting down from 10 and stop at 1
    print(x) #Prints the number the for loop is on
    time.sleep(1)
    if x == 1: #Once the loop counts to 1 it will print liftoff
        print("Liftoff")
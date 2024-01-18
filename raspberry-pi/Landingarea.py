#type: ignore
# Zachary Siller
# Landing Area Part 1 10/20/2023

#import board
#import digitalio


def trianglearea (x1y1, x2y2, x3y3): #Function that calculates triangle area and uses a try loop to eliminate invalid inputs
    try:
        x1y1=x1y1.split(',')  #Splits user input into 6 components using commas
        x2y2=x2y2.split(',')
        x3y3=x3y3.split(',')
    
        x1=float(x1y1 [0]) #Turns the split input into floats
        y1=float(x1y1 [1])
        x2=float(x2y2 [0])
        y2=float(x2y2 [1])
        x3=float(x3y3 [0])
        y3=float(x3y3 [1])
        area = abs((1/2)*(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))) #Calculates are using a formula.
        if area == 0: #If the points given do not create a triangle this statement will be printed.
            print("not a triangle") 
        else: #If the inputs do create a valid triangle
            return area      
    except: #Runs if the try loop fails indicating there was an input error.
        print("invalid imput")
        area = 0
        return area


while True:
    
    coord1 = input('Coordinates for point 1:')  #Grabs user input and stores it
    coord2 = input('Coordinates for point 2:')
    coord3 = input('Coordinates for point 3:')

    area = trianglearea(coord1, coord2, coord3) #Calls the function.
    if area==0:
        continue
    
    else:
        print(f"The triangle with vertices ({coord1}), ({coord2}), ({coord3}) has area:{area} km^2")


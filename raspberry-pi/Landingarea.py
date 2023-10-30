#type: ignore
# Zachary Siller
# Landing Area Part 1 10/20/2023

#import board
#import digitalio


def trianglearea (x1y1, x2y2, x3y3):
    try:
        x1y1=x1y1.split(',')
        x2y2=x2y2.split(',')
        x3y3=x3y3.split(',')
    
        x1=float(x1y1 [0])
        y1=float(x1y1 [1])
        x2=float(x2y2 [0])
        y2=float(x2y2 [1])
        x3=float(x3y3 [0])
        y3=float(x3y3 [1])
        area = abs((1/2)*(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))
        if area == 0:
            print("not a triangle") 
        else:
            return area      
    except:
        print("invalid imput")
        area = 0
        return area


while True:
    
    coord1 = input('Coordinates for point 1:')
    coord2 = input('Coordinates for point 2:')
    coord3 = input('Coordinates for point 3:')

    area = trianglearea(coord1, coord2, coord3)
    if area==0:
        continue
    
    else:
        print(f"The triangle with vertices ({coord1}), ({coord2}), ({coord3}) has area:{area} km^2")


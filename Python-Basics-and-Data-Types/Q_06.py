# Calculate the area of:
# •	Circle 
# •	Rectangle 
# •	Triangle 
# (using user choice)

import math

def area_circle(radius):
    """
    calculating area of circle
    parameter: radius of circle
    return: area of circle
    """

    return round(math.pi*pow(radius,2),2)


def area_rectangle(length,breath):
    """
    calculating area of rectangle
    parameter: length and breath
    return: area of rectangle
    """

    return length*breath

def area_right_angle_triangle(base,height):
    """
    calculating area of right angle triangle
    parameter: base and height
    return: area of triangle
    """

    return 0.5*base*height

print("For area of circle Enter 1\nFor area of Rectangle Enter 2\nFor area of Triangle Enter 3")
area = int(input("Enter your choice: "))

match area:
    case 1:
        radius = int(input("Enter radius: "))
        print(area_circle(radius))
    case 2:
        length = int(input("Enter length: "))
        breath = int(input("Enter breath: "))
        print(area_rectangle(length,breath))
    case 3:
        base = int(input("Enter base: "))
        height = int(input("Enter height: "))
        print(area_right_angle_triangle(base,height))
    case _:
        print("Invalid input")



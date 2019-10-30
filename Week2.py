from math import pi

try:
    side_1 = int(input("Please enter a side length "))
    side_2 = int(input("Please enter a different side length "))

    area_rec = side_1 * side_2
    print("The area of the rectangle is", area_rec)

    radius = int(input("Please enter the radius of a circle "))

    area_circ = radius*pi
    print("The area of the circle is ", area_circ)

except ValueError:
    print ("Do one")
#Timothy Duong
#CTC 389 Midterm Question 2

def rectangle_area(base, height):
    area = base * height
    return area

input_base = int(input("Enter the base of the rectangle: "))
input_height = int(input("Enter the height of the rectangle: "))

calculated_area = rectangle_area(input_base, input_height)

print("The area of the rectangle is", calculated_area)

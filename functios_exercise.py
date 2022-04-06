# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# ```
# area = (1/2)*base*height
# ```

def calculate_area(base,height):
    area = (1/2)*base*height
    return area
a = calculate_area(10,5)
print("Area of triangle: ",a)

# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area = length*width

def area(dim1,dim2,shape):
    '''
    :param dimension1: In case of triangle it is "base". For rectangle it is "length".
    :param dimension2: In case of triangle it is "height". For rectangle it is "width".
    :param shape: Either "triangle" or "rectangle"
    :return: Area of a shape
    '''
    if shape=="triangle":
        area = 1/2*(dim1 * dim2)
    elif shape=="rectangle":
        area =  dim1 * dim2
    else:
        area = "None"
    return area

traingle_area = area(2,3,"triangle")
rectangle_area = area(2,3,"rectangle")

print(traingle_area)
print(rectangle_area)

        
# 3. Write a function called print_pattern that takes interger number as an argument and prints following pattern if input number is 3
'''
*
**
***
'''
# if input is 4 then it should print
'''
*
**
***
****
'''
def pattern(n):
    for i in range(n):
        s = ''
        for j in range(i+1):
            s = s+ '*'
        print(s)
pattern(3)

# 4. Write a Python function to find the Max of three numbers.

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))

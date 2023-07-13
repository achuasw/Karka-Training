"""def area_of_triangle(a,b,c):
    s=(a+b+c)/2
    area=(s*((s-a)*(s-b)*(s-c)))**0.5
    # print(area)
    return area
a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("ENter C: "))
area_tri=area_of_triangle(a,b,c)
print(area_tri)"""

def area_of_square(s):
    area=s*s
    return area
print("Find area of a square")
side1=float(input("Enter the side1:" ))
side2=float(input("Enter the side2: "))
area_sqr=area_of_square(side1)
print("Area of Square:",area_sqr)

def area_of_rectangle(area_sqr,b):
    area=area_sqr*b 
    return area
length=area_sqr

print("Area of rectangle\nlength=",length)
breadth=float(input("Enter the breadth: "))
print("\n")
area_rect=area_of_rectangle(length,breadth)
print("Area of rectangle:",area_rect)


def area_of_circle(r):
    area=3.14*(r*r)
    return area
radius=area_rect
print("\nRadius of circle= ",radius)
area_crcl=area_of_circle(radius)
print("Area of circle:",area_crcl)
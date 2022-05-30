from math import *

def cosFromThreeSides(a, b, c):
    A = (b**2) + (c**2) - (a**2)
    A = A / (2 * b * c)
    A = acos(A)
    return degrees(A)

def cosFromTwoSideAndAngleBetween(b, c, A):
    ARad = radians(A)
    a2 = (b**2) + (c**2) - (2 * b * c * cos(ARad))
    return sqrt(a2)

def sinForAngle(A, a, b):
    ARad = radians(A)
    sinAOvera = sin(ARad) / a
    BSin = sinAOvera * b
    BRad = asin(BSin)
    return degrees(BRad)

def remainingAngle(A, B):
    return 180 - A - B

def areaOfTriangle(a, b, C):
    CRad = radians(C)
    return 0.5 * a * b * sin(CRad)

def propertiesFromThreeSides(a, b, c):
    A = cosFromThreeSides(a, b, c)
    B = sinForAngle(A, a, b)
    C = remainingAngle(A, B)
    area = areaOfTriangle(a, b, C)
    return (a, b, c, A, B, C, area)

def propertiesFromTwoSidesAndAngleBetween(b, c, A):
    a = cosFromTwoSideAndAngleBetween(b, c, A)
    B = sinForAngle(A, a, b)
    C = remainingAngle(A, B)
    area = areaOfTriangle(a, b, C)
    return (a, b, c, A, B, C, area)

def showProperties(a, b, c, A, B, C, area):
    print(f"Sides: a = {a:.2f}cm, b = {b:.2f}cm, c = {c:.2f}cm")
    print(f"Angles: A = {A:.2f}°, B = {B:.2f}°, C = {C:.2f}°")
    print(f"Area = {area:.2f}cm²")

def drawTriangle(a, b, c, A, B, C):
    import turtle as t

    t.hideturtle()

    t.penup()
    t.goto(-20, -20)
    t.write("B", False, align="left", font=("Times New Roman", 16, "normal"))
    t.goto(0,0)
    t.pendown()

    t.fd(a/2)
    t.penup()
    t.goto(a/2, -25)
    t.write("a", False, align="left", font=("Times New Roman", 16, "normal"))
    t.goto(a/2, 0)
    t.pendown()
    t.fd(a/2)
    t.lt(180 - C)

    t.penup()
    t.goto(a+20, -20)
    t.write("C", False, align="left", font=("Times New Roman", 16, "normal"))
    t.goto(a,0)
    t.pendown()

    t.fd(b/2)
    t.penup()
    t.rt(90)
    t.fd(5)
    t.write("b", False, align="left", font=("Times New Roman", 16, "normal"))
    t.bk(5)
    t.lt(90)
    t.pendown()
    t.fd(b/2)
    t.lt(180 - A)
    t.write("A", False, align="left", font=("Times New Roman", 16, "normal"))

    t.fd(c/2)
    t.penup()
    t.rt(90)
    t.fd(15)
    t.write("c", False, align="left", font=("Times New Roman", 16, "normal"))
    t.bk(15)
    t.lt(90)
    t.pendown()
    t.fd(c/2)
    t.lt(180 - B)

    t.mainloop()

def main():
    t = propertiesFromTwoSidesAndAngleBetween(150, 400, 32)
    showProperties(*t)
    drawTriangle(*t[0:6])

if __name__ == "__main__": main()
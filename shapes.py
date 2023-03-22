#Circle: P = 2(pie)r | A = pie(r^2)
#Equrallirtal Triagle: P = 3 * a | A = sqarroot(3) / 4 * (a ^ 2)
#Square: P = 4*a | A = a ^ 2
#Retangle: P = 2 ( l + w ) | A = L * W

import math

def shape_cal():
    print("What SHAPE would you like to find the P & A of?")
    print("-----------------------------------------------")
    print("///Type 1,2,3, or 4 for a shape.///")
    print("1 = Circle")
    print("2 = Equilateral triangle ")
    print("3 = Square")
    print("4 = Rentangle")
    choice = input("")
    if choice == "1":
        print("What is the radius of your circle?")
        r = int(input())
        circle_cal(r)
    elif choice == "2":
        print("What is the length of the side of your trangle?")
        a = int(input())
        triangle_cal(a)
    elif choice == "3":
        print("What is the length of the side of your square?")
        a = int(input())
        square_cal(a)
    elif choice == "4":
        print("What is the length of your rentangle?")
        l = int(input())
        print("What is the width of your rentangle?")
        w = int(input())
        retangle_cal(l , w)
    else:
        print("///Please pick a number from 1 - 4")
        shape_cal()
    print("Would you like to do another shape? (yes/no)")
    ask = input("")
    if ask == "yes":
        shape_cal()
    else:
        quit()


def circle_cal(r):
    P = r * 2 * math.pi
    A = math.pi * (r ** 2)
    print("Your CIRCLE perimeter & area: P = " + str(P) + " | A = " + str(A))

def triangle_cal(a):
    P = 3 * a
    A = (math.sqrt(3) / 4) * (a ** 2)
    print("Your EQUILATERAL TRIANGLE perimeter & area: P = " + str(P) + " | A = " + str(A))

def square_cal(a):
    P = 4 * a
    A = a ** 2
    print("Your SQUARE perimeter & area: P = " + str(P) + " | A = " + str(A))

def retangle_cal(l , w):
    P = 2 * (l + w)
    A = l * w
    print("Your RETAGLE perimeter & area: P = " + str(P) + " | A = " + str(A))

shape_cal()

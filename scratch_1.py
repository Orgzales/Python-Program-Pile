import random


def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp%10
        sum += digit**3
        temp//=10
    if n == sum:
        print(str(n) + " is a armstrong number")
    else:
        print( str(n) + " is not a armstrong number")

armstrong(1634)







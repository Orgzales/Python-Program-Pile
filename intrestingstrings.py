import random

def splitray(arr, n):
    x = len(arr)
    for i in range(0, n):
        k = arr[0] #setting the k to the zero varable
        for j in range(0, x-1):
            arr[j] = arr[j+1] # shifting one over
        print(k)
        arr[x-1] = k

def rev_string(str):
    print(str[::-1]) ## reverse/rotates a string around

def pand_str(str):
    x = str
    y = str[::-1]
    if(x == y):
        print(str + " is a pandilooium")
    else:
        print(str + " is not a pandilooium")
    print(x)
    print(y)
str = input("what is your word? ")
pand_str(str)








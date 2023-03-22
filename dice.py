import random
import statistics #to import the function mode

dicearry1 = []
dicearry2 = []
dicesumarry = [] # arry for sum of each result

def rolldie1(n): ## function to roll the dice and make a arry
    for i in range(0 , n):
        dicearry1.append(random.randint(1,6))

def rolldie2(n): ## function to roll the dice and make a arry
    for i in range(0 , n):
        dicearry2.append(random.randint(1,6))

def dicesum():   ## function to create a arry of each sum of die 1 & 2
    for i in range(0, 100):
        dicesumarry.append(dicearry1[i] + dicearry2[i])
    finalsum = sum(dicesumarry) # The total value of all values
    print("The total results of all dice: " + str(finalsum))

# To call each function to create the arrays
rolldie1(100)
rolldie2(100)

# To print out each result
print("All rolls of die 1 : ")
print(dicearry1)
print("------------------------------------") # spcaer so it's easier to read
print("All rolls of die 2 : ")
print(dicearry2)
print("------------------------------------") # spcaer so it's easier to read
print("Every sum of each roll : ")
dicesum()
print(dicesumarry)


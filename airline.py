#Orion R. Gonzales
veganmeals = 5                  #Max meals for vegans
Airlineseats = {}
Maxseats = 0                    #also seat number
Mealletter = "S"                #extra varable to put into list/dictionary easier
Cancle = False                  #if we need to replace the seat

for s in range(1,11):
    Airlineseats['seat'+str(s)] = "Empty seat"                  #sets the dictionary for 10 seats


def mealplan():
    global veganmeals
    global Mealletter
    global Cancle
    print("would you like a vegan meal or a standard meal?: (v/s)")
    ask = input("")
    if ask == "v":
        if veganmeals > 0:                                              #if we have vegan meals left
            veganmeals -= 1
            print("Please enjoy your vegan meal")
            Mealletter = "V"
        else:                                                           #if there are no vegan meals left
            print("We are out of vegan meals")
            print("Would you like a standard meal? (yes/no)")
            ask2 = input("")
            if ask2 == "yes":                                           #if they want a standard
                print("enjoy your standard meal")
                Mealletter = "S"
            else:                                                       #if they want to reschedual
                print("Next flight with a vegetarian option leaves in 4 hours")
                print("Please reschedule.")
                Mealletter = "N/A"
                Cancle = True
    else:                                                               #if they want a standard meal
        print("Please enjoy your standard meal")
        Mealletter = "S"

def initiate():
    global Maxseats                         #for seat number
    global Airlineseats
    global Mealletter                       #for meal plan type
    global Cancle
    print("Welcome to our airline")
    if Maxseats < 10:                       #if there are avablibe seating
        Maxseats += 1
        firstname = input("what is your first name?: ")
        lastname = input("what is your last name?: ")
        mealplan()
        Airlineseats["seat" + str(Maxseats)] = "|| Name: " + firstname + " " + lastname + "| seat#: " + str(Maxseats) + "| meal plan: " + Mealletter
        if Cancle == True:                  #Clear out the seat for a new person
            Airlineseats["seat" + str(Maxseats)] = "canceled"
        print(Airlineseats["seat" + str(Maxseats)])
        if Cancle == True:                  #Clear out the seat after printing 'clear' and resetst the max seat number
            Maxseats -= 1
            Cancle = False
        print("Would you like to schdueal a flight?: (yes/no)")
        ask = input("")
        if ask == "yes":
            initiate()
        else:
            print("Have a good day!")
    else:                                   #if the plane is full
        print("No available seating.")
        print("Next flight leaves in 4 hours.")

initiate()
print(Airlineseats)













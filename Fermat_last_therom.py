# fermat's therom: A ** n + B ** n = C ** should be never true

def check_fermat(a, b , c , n ):
    check_rule = (a ** n) + (b ** n) == (c ** n)
    if check_rule == False:
        print("No, that doesn’t work.")
    else:
        print("Holy smokes, Fermat was wrong!")

def number_check_fermat():
    print("///Fermat's Last Theorem states that no three positive integers a, b, and c satisfy \n the equation aⁿ + bⁿ = cⁿ for any integer value of n greater than 2.///")
    print("\n What would you like to be your first value to be?")
    a = int(input())
    print("What would you like to be your second value to be?")
    b = int(input())
    print("What would you like to be your third value to be?")
    c = int(input())
    print("What would you like your 'n' value to be?")
    n = int(input())
    if a < 0:
        print("Your first value isn't valid please try again \n")
        number_check_fermat()
    if b < 0:
        print("Your second value isn't valid please try again \n")
        number_check_fermat()
    if c < 0:
        print("Your thrid value isn't valid please try again \n")
        number_check_fermat()
    if n <= 2:
        print("Your 'n' value isn't valid please try again \n")
        number_check_fermat()
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    print("n = " + str(n))
    print(str(a) + "^" + str(n) + " + " + str(b) + "^" + str(n) + " = " + str(c) + "^" + str(n))
    print("Are you happy with these values? (yes/no)")
    ask = input("")
    if ask == "yes":
        check_fermat(a , b , c , n)
        print("Would you like to try again? (yes/no)")
        choice = input("")
        if choice == "yes":
            number_check_fermat()
        else:
            quit()
    else:
        print("please retype your values.")
        number_check_fermat()

number_check_fermat()



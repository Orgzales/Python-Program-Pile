import random
import time

data_arry = []          #storage for unqiue numbers
cur_random_num = 0
retangles_names = {}
retangles_side_a = {}
retangles_side_b = {}
retangles_area = {}
retangles_p = {}

def random_num():               #so two rectangles don't have the same uqniue number
    global cur_random_num
    cur_random_num = random.randint(1000,9999)
    if cur_random_num in data_arry: #if there is already that number taken, rerun random_num()
        random_num()
    data_arry.append(cur_random_num)    #adding the num to storage

class Retangle:
    def __init__(self, name, side_a, side_b):
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.uqn = cur_random_num
        self.area = side_a * side_b
        self.p = (side_a * 2) + (side_b * 2)

        retangles_names[cur_random_num] = self.name
        retangles_side_a[cur_random_num] = self.side_a
        retangles_side_b[cur_random_num] = self.side_b
        retangles_area[cur_random_num] = self.area
        retangles_p[cur_random_num] = self.p


def build_rectangles():
    print("Would you like to create a new RECTANGLE or recall a old one?\n"
          "1 - New\n"
          "2 - Recall\n")
    ask = int(input())
    if ask == 1:
        print("What would you like your rectangle to be called?\n")
        ask_name = input("")
        print("What length would you like Side A to be?\n")
        try:
            ask_side_a = int(input())
        except ValueError:      #In case input is not a int
            print("Please restart and input a valid value\n")
            build_rectangles()
        if ask_side_a < 0:      #self guard against negitive numbers
            print("Please restart and input a valid value\n")
            build_rectangles()
        print("What length would you like Side B to be?\n")
        try:
            ask_side_b = float(input())
        except ValueError:
            print("Please restart and input a valid value\n")
            build_rectangles()
        if ask_side_b < 0:
            print("Please restart and input a valid value\n")
            build_rectangles()
        random_num()
        x = str(cur_random_num)
        x = Retangle(ask_name, ask_side_a, ask_side_b)
        print("--------------------")
        print("RECTANGLE " + x.name + ":")
        print("Side a : " + str(x.side_a))
        print("Side b : " + str(x.side_b))
        print("Rectangle # : " + str(x.uqn))
        print("Rectangle A = " + str(x.area))
        print("Rectangle P = "  + str(x.p) + "\n")
        time.sleep(0.5)
        print("Would you like to continue?\n"
              "1 - Yes\n"
              "2 - NO")
        ask_quit = int(input())
        if ask_quit == 1:
            build_rectangles()
        else:
            quit()

    elif ask == 2:
        print("What Rectangle would you like to see?")
        print(retangles_names)
        print("Please enter 4-digit number")
        try:
            ask_uqn = int(input())
        except ValueError:
            print("Please restart and input a valid value\n")
            build_rectangles()
        if ask_uqn not in retangles_names:
            print("That Rectangle does not exsist\n")
            build_rectangles()
        print("RECTANGLE " + retangles_names[ask_uqn])
        print("Side a : " + str(retangles_side_a[ask_uqn]))
        print("Side b : " + str(retangles_side_b[ask_uqn]))
        print("Rectangle # : " + str(ask_uqn))
        print("Rectangle A = " + str(retangles_area[ask_uqn]))
        print("Rectangle P = " + str(retangles_p[ask_uqn]))
        print("")
        time.sleep(0.5)
        print("Would you like to continue?\n"
              "1 - Yes\n"
              "2 - NO")
        ask_quit = int(input())
        if ask_quit == 1:
            build_rectangles()
        else:
            quit()
    else:
        build_rectangles()



build_rectangles()





















import random
import math

## Variables for making custom Account numbers
account_num_800 = 800
account_num_second = 1000
account_num_last = 00

##Memory place holders
ac_num_place = ""
data_arry_account_nums = []
ID = 0
data_arry_IDs = []

#DICTIONARY
# { ID | DATA }
ID_Name = {}
ID_Check_nums = {}  # { ID | CHECK account number }
ID_Check_bal = {}   # { CHECK account num | Bal }
ID_Save_nums = {}
ID_Save_bal = {}
ID_Busi_nums = {}
ID_Busi_bal = {}



def acccount_number():          #Function to make unqiue account numbers
    global account_num_second
    global account_num_last
    global ac_num_place

    account_num_second = random.randint(1000, 9999)
    account_num_last = random.randint(10,99)
    ac_num = str(account_num_800) + "-" + str(account_num_second) + "-" + str(account_num_last)
    if ac_num in data_arry_account_nums:
        acccount_number()
    data_arry_account_nums.append(ac_num)
    ac_num_place = ac_num

def ID_create():
    global ID
    ID = random.randint(100000, 999999)
    if ID in data_arry_IDs:
        ID_create()
    data_arry_IDs.append(ID)

class Bank_Account:
    def __init__( self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        acccount_number()
        self.Checking_ac_num = ac_num_place
        acccount_number()
        self.Saving_ac_num = ac_num_place
        acccount_number()
        self.Bussiness_ac_num = ac_num_place

        self.Check_balance = 0.0
        self.Saving_balance = 0.0
        self.Bussiness_balance = 0.0

        ID_create()
        self.ID = ID

        #adding to the memory

        ID_Name[ID] = self.first_name + " " + self.last_name

        ID_Check_nums[ID] = self.Checking_ac_num
        ID_Check_bal[ID_Check_nums[ID]] = self.Check_balance

        ID_Save_nums[ID] = self.Saving_ac_num
        ID_Save_bal[ ID_Save_nums[ID] ] = self.Saving_balance

        ID_Busi_nums[ID] = self.Bussiness_ac_num
        ID_Busi_bal[ ID_Busi_nums[ID] ] = self.Bussiness_balance

def Show_Checking_account(ID_num):
    print("~~CHECKING ACCOUNT~~")
    print("NAME: " + ID_Name[ID_num])
    print("AC-NUM: " + str( ID_Check_nums[ID_num] ) )
    print("BALANCE: $" + str( ID_Check_bal[ID_Check_nums[ID_num]]))

def Show_Saving_account(ID_num):
    print("~~SAVING ACCOUNT~~")
    print("NAME: " + ID_Name[ID_num])
    print("AC-NUM: " + str( ID_Save_nums[ID_num] ) )
    print("BALANCE: $" + str( ID_Save_bal[ID_Save_nums[ID_num]]))

def Show_Busi_account(ID_num):
    print("~~BUSSINESS ACCOUNT~~")
    print("NAME: " + ID_Name[ID_num])
    print("AC-NUM: " + str( ID_Busi_nums[ID_num] ) )
    print("BALANCE: $" + str( ID_Busi_bal[ID_Busi_nums[ID_num]]))

def ENTER():
    print("\nPRESS ENTER TO SIGH OUT\n")
    x = input("")

def Withdrawal(i):
    print("How much money would you like to WITHDRAWAL?\n")
    if i == "1":
        print("CHECKING BALANCE: $" + str(ID_Check_bal[ID_Check_nums[ID]]))
    elif i == "2":
        print("SAVING BALANCE: $" + str(ID_Save_bal[ID_Save_nums[ID]]))
    else:
        print("BUSSINESS BALANCE: $" + str(ID_Busi_bal[ID_Busi_nums[ID]]))
    money_W = float(input())
    if money_W < 0:
        print("Please enter a valid value")
        Withdrawal(i)
    try:
        if i == "1":
            ID_Check_bal[ID_Check_nums[ID]] = round(ID_Check_bal[ID_Check_nums[ID]] - money_W, 2)
            if ID_Check_bal[ID_Check_nums[ID]] < 0:
                print("!!!!YOUR ACCOUNT IS IN THE RED!!!!")
            print("WITHDRAWLING: $" + str(money_W))
            print("CHECKING BALANCE: $" + str(ID_Check_bal[ID_Check_nums[ID]]))
            ENTER()
        elif i == "2":
            ID_Save_bal[ID_Save_nums[ID]] = round(ID_Save_bal[ID_Save_nums[ID]] - money_W, 2)
            if ID_Save_bal[ID] < 0:
                print("!!!!YOUR ACCOUNT IS IN THE RED!!!!")
            print("WITHDRAWLING: $" + str(money_W))
            print("SAVING BALANCE: $" + str(ID_Save_bal[ID_Save_nums[ID]]))
            ENTER()
        else:
            ID_Busi_bal[ID_Busi_nums[ID]] = round(ID_Busi_bal[ID_Busi_nums[ID]] - money_W,2)
            if ID_Busi_bal[ID_Busi_nums[ID]] < 0:
                print("!!!!YOUR ACCOUNT IS IN THE RED!!!!")
            print("WITHDRAWLING: $" + str(money_W))
            print("BUSSINESS BALANCE: $" + str(ID_Busi_bal[ID_Busi_nums[ID]]))
            ENTER()
    except ValueError:
        print("Please enter a valid value")
        Withdrawal(i)

def Deposite(i):
    print("How much money would you like to DEPOSIT?\n")
    if i == "1":
        print("CHECKING BALANCE: $" + str(ID_Check_bal[ID_Check_nums[ID]]))
    elif i == "2":
        print("SAVING BALANCE: $" + str(ID_Save_bal[ID_Save_nums[ID]]))
    else:
        print("BUSSINESS BALANCE: $" + str(ID_Busi_bal[ID_Busi_nums[ID]]))
    money_W = float(input())
    if money_W < 0:
        print("Please enter a valid value")
        Deposite(i)
    try:
        if i == "1":
            ID_Check_bal[ID_Check_nums[ID]] = round(ID_Check_bal[ID_Check_nums[ID]] + money_W, 2)
            print("Deposit: $" + str(money_W))
            print("CHECKING BALANCE: $" + str(ID_Check_bal[ID_Check_nums[ID]]))
            ENTER()
        elif i == "2":
            ID_Save_bal[ID_Save_nums[ID]] = round(ID_Save_bal[ID_Save_nums[ID]] + money_W, 2)
            print("Deposit: $" + str(money_W))
            print("SAVING BALANCE: $" + str(ID_Save_bal[ID_Save_nums[ID]]))
            ENTER()
        else:
            ID_Busi_bal[ID_Busi_nums[ID]] = round(ID_Busi_bal[ID_Busi_nums[ID]] + money_W, 2)
            print("Deposit: $" + str(money_W))
            print("BUSSINESS BALANCE: $" + str(ID_Busi_bal[ID_Busi_nums[ID]]))
            ENTER()
    except ValueError:
        print("Please enter a valid value")
        Deposite(i)



def Main_program():
    global ID
    print("~WELCOME TO BANK OF ACM~")
    print("1 - SIGNING IN\n"
          "2 - NEW ACCOUNT")
    ask = input("")
    if ask == "1":
        print("Please enter your ID:")
        try:
            ID_x = int(input())
            ID = ID_x
            print("Welcome back " + ID_Name[ID_x])
        except KeyError:
            print("KEY ERROR, ID does not exsits")
            Main_program()
        print("1 - Access account\n"
              "2 - Withdrawal \n"
              "3 - Deposit \n"
              "Other - Logout")
        ask2 = input("")
        if ask2 == "1":
            print("Which account would you wish to see?")
            print("1 - " + ID_Check_nums[ID_x] + " (Checking)")
            print("2 - " + ID_Save_nums[ID_x] + " (Saving)")
            print("3 - " + ID_Busi_nums[ID_x] + " (Bussiness)")
            print("4 - VIEW ALL")
            print("Other - EXIT")
            ask_V = input("")
            if ask_V == "1":
                Show_Checking_account(ID_x)
                ENTER()
                Main_program()
            elif ask_V == "2":
                Show_Saving_account(ID_x)
                ENTER()
                Main_program()
            elif ask_V == "3":
                Show_Busi_account(ID_x)
                ENTER()
                Main_program()
            elif ask_V == "4":
                Show_Checking_account(ID_x)
                print("---------------------------------")
                Show_Saving_account(ID_x)
                print("---------------------------------")
                Show_Busi_account(ID_x)
                ENTER()
                Main_program()
            else:
                print("SIGNING OUT...")
                Main_program()
        elif ask2 == "2":
            print("Which account would you like to withdrawl from?")
            print("1 - " + ID_Check_nums[ID_x] + " (Checking)")
            print("2 - " + ID_Save_nums[ID_x] + " (Saving)")
            print("3 - " + ID_Busi_nums[ID_x] + " (Bussiness)")
            print("Other - EXIT")
            ask_W = input("")
            if ask_W == "1":
                Withdrawal(ask_W)
                Main_program()
            elif ask_W == "2":
                Withdrawal(ask_W)
                Main_program()
            elif ask_W == "3":
                Withdrawal(ask_W)
                Main_program()
            else:
                print("SIGNING OUT...")
                Main_program()
        elif ask2 == "3":
            print("Which account would you like to Deposit from?")
            print("1 - " + ID_Check_nums[ID_x] + " (Checking)")
            print("2 - " + ID_Save_nums[ID_x] + " (Saving)")
            print("3 - " + ID_Busi_nums[ID_x] + " (Bussiness)")
            print("Other - EXIT")
            ask_D = input("")
            if ask_D == "1":
                Deposite(ask_D)
                Main_program()
            elif ask_D == "2":
                Deposite(ask_D)
                Main_program()
            elif ask_D == "3":
                Deposite(ask_D)
                Main_program()
            else:
                print("SIGNING OUT...")
                Main_program()
        else:
            Main_program()

    elif ask == "2":
        print("What is your first name?:")
        ask_first_name = input("")
        print("What is your last name?:")
        ask_last_name = input("")
        Account =Bank_Account(ask_first_name, ask_last_name)
        print("NAME: " + ID_Name[ID])
        print("ID NUMBER: " + str(ID))
        print("CHECKING ACCOUNT ###: " + str(ID_Check_nums[ID]))
        print("SAVING ACCOUNT ###: " + str(ID_Save_nums[ID]))
        print("BUSSINESS ACCOUNT ###: " + str(ID_Busi_nums[ID]))
        ENTER()
        Main_program()
    else:
        Main_program()

Main_program()
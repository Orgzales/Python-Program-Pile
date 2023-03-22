import random
import statistics
import math
import time
import sys
zero = 0
SCORE = 0

#Basic Stats
Player_Name = ""
Player_Gender = ""
Player_Class = ""
Player_level = 1
Player_xp = 0

#Weapon stats
Weapon_min_value = 1
Weapon_max_value = 6
Weapon_s_value = 0

class Player_Weapon_create:
    def __init__(self, name):
        self.name = name
    def weapon_dmg_set(self, a, b, c):
        self.dmg = random.randint(a, b) + c

Player_Weapon = Player_Weapon_create("empty")

#Setting all the levels
Playerxplimits = {}
lvcue = 1
xplimit = 1000
for i in range(1,101):
    Playerxplimits[i] = round(xplimit)
    xplimit = xplimit + (100 * lvcue)
    lvcue = lvcue + 1

#Game stats
Player_HP = 20
Player_STR = 10
Player_DEX = 10

#Player Fighting
Strfightingbonus = random.randint(round(Player_STR/2), Player_STR)
Dexfightingbonus = random.randint(round(Player_DEX/2), Player_DEX)
Player_dmg = 0
Player_speed = 0
Player_health = Player_HP

#Item varables
Potions_num = 0
Potions_heal = .25
Itemspot1_name = "empty"
Itemspot2_name = "empty"
Itemspot3_name = "empty"
Itemspot4_name = "empty"
Itemnum1 = 0
Itemnum2 = 0
Itemnum3 = 0
Itemnum4 = 0
Item1_type = ""         # D = dmg item | H = Healing item
Item2_type = ""
Item3_type = ""
Item4_type = ""
Which_item = 0          #1,2,3, or 4

#Enemy Fighting
Enemy_name = ""
Enemyhp = 0
Enemystr = 0
Enemydex = 0
Enemystrboost = 0
Enemydexboost = 0
Enemydmg = 0
Enemydodge = 0
Enemyxp = 0
EnemyLv = 1

Enemy_notes = "None"

Whos_turn = "P"
Enemycount = 0
Boss_enemy = False

#attacks chances
Quick_atk = .75         #50% dmg
Normal_atk = .5         #100% dmg
Heavy_atk = .2          #150% dmg
Quickatk_adapter = .35
Normalatk_adapter = 1.0
Heavyatk_adapter = 1.25

#Dodge cjances
Negate = .75       #25% reduce
Block = .5       #50% reduce
Dodge = .2        #100% reduce
Negate_adapator = .25
Block_adaptor = .50
Dodge_adaptor = 1.0

dmg_avoided = 0.0

#Priority of Stats
High_Prinum = 5
Med_Prinum = 3
Low_Prinum = 1

#Level up priority
HighP = ""
MedP = ""
LowP = ""
classarry = ["1","2","3"]

#Materials
#Materials = {1: "Rusty", 2: "Copper", 3: "Iron", 4: "Steel", 5: "Carbon", 6: "Silver", 7: "Titanium", 8: "Tungsten", 9: "Demon's Skin"}

def Player_Create():
    global Player_Name
    global Player_Gender
    global Player_Class
    global Player_Weapon_name
    global HighP
    global MedP
    global LowP
    global Materials
    global Player_level

    classes = { 1 : "Warrior", 2 : "Archer", 3:  "Spartan"} #For the else statement in picking class to be randomly assigned one

    Player_Name = input("What would you like your name to be: \n\n\n")        #Name
    Spacer()
    Player_Gender = input("What Gender are you: \n\n\n")                      #Gender
    Spacer()
    print("///Type number to choose decision. Any number that you pick that isn't a option your choice will be randomized.///\n\n\n")
    print("What type of Class would you like to take?")
    print("1 - Warrior (You follow the way of the Blade)")
    print("2 - Archer  (Distance and Accruacry are safer)")
    print("3 - Spartan (SMASH EVERYTHING)\n\n\n\n")
    Spacer()
    classpick = input("")                                            #Class
    if classpick == "1":
        Player_Class = "Warrior"
        print("Class: Warrior")
    elif classpick == "2":
        Player_Class = "Archer"
        print("Class: Archer")
    elif classpick == "3":
        Player_Class = "Spartan"
        print("Class: Spartan")
    else:
        Player_Class = classes[random.randint(1,3)]
        if Player_Class == "Warrior":
            print("Class: Warrior")
        if Player_Class == "Archer":
            print("Class: Archer")
        if Player_Class == "Spartan":
            print("Class: Spartan")
    Spacer()
    Stat_setup()
    weaponsetter()
    print("Your Main weapon will be: " + Player_Weapon.name)
    Spacer()
    playerinfo()
    Spacer()
    print("Are you satisfied with your charater?: (1 - yes/ 2 - no)")
    finalask = input("")
    if finalask == "1":
        print("Let's begin the game!")
    else:
        print("Are you sure you want to remake your CHARATER?: (1 - yes/ 2 - no)")
        finalask2 = input("")
        if finalask2 == "1":
            Player_Create()
        else:
            print("Let's begin the game!")
            print("please wait...")
            time.sleep(3)

def Enemyspawn():
    global Enemyhp
    global Enemystr
    global Enemydex
    global Enemydexboost
    global Enemystrboost
    global Enemyxp
    global EnemyLv
    global Enemy_name
    Enemyhp = random.randint(round((Player_HP / 4)), round((Player_HP/2)))
    Enemystr = random.randint(round((Player_STR / 4)), round((Player_STR/2)))
    Enemydex = random.randint(round((Player_DEX / 4)), round((Player_DEX/2)))
    #Enemystrboost = Enemystr/2
    #Enemydexboost = Enemydex/2
    EnemyLv = random.randint((Player_level - 1) , (Player_level + 1))
    if EnemyLv <= 0:            #So a Enemy doesn't have a Lv.0 or less
        EnemyLv = 1
    Enemny_type_spawn()

def Enemny_type_spawn():
    global Enemy_name
    global Enemyxp
    #Higher levels creatures are obvisouly stronger
    if EnemyLv <= 3:
        weakest_creatures = ["Wolf", "Goblin", "Giant Bat", "Flumph", "Stirge"]
        Enemy_name = weakest_creatures[random.randint(0,4)]
        Enemyxp = random.randint(100, 150) * EnemyLv
    elif EnemyLv <= 7:
        weak_creatures = ["Giant Beetles" , "Homunculus", "Small Demon", "Ghoul", "Crawling Claw", "Skeleton", "Banshee", "Lamia"]
        Enemy_name = weak_creatures[random.randint(0,7)]
        Enemyxp = random.randint(100, 150) * round(EnemyLv/2)
    elif EnemyLv <= 13:
        normal_creatures = ["Awakened Shrub", "Lemure", "Myconid Sprout", "IMP", "Zombie", "Giant Serpant", "Kobold", "Maniac", "Fire Elemental"]
        Enemy_name = normal_creatures = [random.randint(0,8)]
        Enemyxp = random.randint(100, 150) * round(EnemyLv/3)
    elif EnemyLv <= 25:
        strong_creatures = ["Red Demon", "Demon prince", "Prideful Demon", "Small Dragon", "Unknown Spirit Force", "Fake Mimic"]
        Enemy_name = strong_creatures = [random.randint(0,5)]
        Enemyxp = random.randint(100, 150) * round(EnemyLv/4)
    else:
        strongest_creatures = ["Large Dragon", "Large Demon", "Hell Hound", "Syntax Error", "A Devil", "DEBUGGER", "(&#Q *)^#^@)"]
        Enemy_name = strongest_creatures[random.randint(0,6)]
        Enemyxp = random.randint(100, 150) * round(EnemyLv/5)

def fight_Enemy_dmg():
    global Enemydmg
    Enemydmg = random.randint(round(Enemystr / 2) , Enemystr)
def fight_Enemy_dodge():
    global Enemydodge
    Enemydodge = random.randint(round(Enemydex / 2) , Enemydex)
def fight_Playerdmg():
    global Player_dmg
    global Strfightingbonus
    Player_Weapon_create.weapon_dmg_set(Player_Weapon, Weapon_min_value, Weapon_max_value, Weapon_s_value)
    Strfightingbonus = random.randint(1, round(Player_STR/2))
    Player_dmg = Strfightingbonus + Player_Weapon.dmg
def fight_Playerspeed():
    global Player_speed
    global Dexfightingbonus
    Dexfightingbonus = random.randint(1, round(Player_DEX/2))
    Player_speed = Dexfightingbonus + round(Dexfightingbonus/2)


#Fighting menus
def taskbar_print():
    print("------------------------------------------------------------------------------------------------------")
    print("| 1 - ATTACK |    | 2 - ANALYSIS |    | 3 - ITEMS |   | 4 - SELF CHECK |   | 5 - FLEE |   | 6 - HELP |")
    print("------------------------------------------------------------------------------------------------------")
def attack_print():
    print("---------------------------------------------------------------------------------------")
    print("1 - QUICK ATK " + "[HIT CHANCE: " + str(Quick_atk*100) + "%]")
    print("2 - NORMAL ATK " + "[HIT CHANCE: " + str(Normal_atk*100) + "%]")
    print("3 - HEAVY ATK " + "[HIT CHANCE: " + str(Heavy_atk*100) + "%]")
    print("0 - CANCEL")
    print("---------------------------------------------------------------------------------------")
def items_print():
    print("---------------------------------------------------------------------------------------------------")
    print("0 - USE: [HP potion {" + str(Potions_num) + " LEFT} ]")
    print("1 - USE: [" + Itemspot1_name + "]")
    print("2 - USE: [" + Itemspot2_name + "]")
    print("3 - USE: [" + Itemspot3_name + "]")
    print("4 - USE: [" + Itemspot4_name + "]")
    print("5 - CHECK INVENTORY")
    print("9 - CANCEL")
    print("---------------------------------------------------------------------------------------------------")
def selfcheck_print():
    print("-------------------------------------------")
    print(Player_Name + " Lv." + str(Player_level))
    print("Weapon: " + Player_Weapon_name)
    print("Health: " + str(Player_HP) + " (Current HP: " + str(Player_health) + ")")
    print("QUICK ATK CHANCE: " + str(Quick_atk * 100) + "% to deal [" + str(Quickatk_adapter * 100) + "% dmg]")
    print("NORMAL ATK CHANCE: " + str(Normal_atk * 100) + "% to deal [" + str(Normalatk_adapter * 100) + "% dmg]")
    print("HEAVY ATK CHANCE: " + str(Heavy_atk * 100) + "% to deal [" + str(Heavyatk_adapter * 100) + "% dmg]")
    print("-------------------------------------------")
def flee_print():
    print("--------------------------------------------------")
    print("You sure you wanna run away? (1 - yes / 2 - no)")
    print("--------------------------------------------------")
#Defense Menus
def dodgechoice_print():
    print("-----------------------------------------------------------------------")
    print("| 1 - NEGATE |    | 2 - BLOCK |    | 3 - DODGE |     | 4 - STATISTICS |")
    print("-----------------------------------------------------------------------")
def help_menu_print():
    Spacer()
    print("//As you are fighting the amount of dmg you deal is based on three factors.\n"
          "How strong is your weapon, How high is your strenght, and If you deal a \n"
          "critical strike or not. Weapons Dmg is based on the type of material it's \n"
          "made out of. There are different and unknown materials in this world now \n"
          "that has been brought by or made out of the monsters. Your strength will \n"
          " naturally grow but some quests can help increase your overall skill.\n"
          "Critical strikes will be based on both your stats and the weapon.//\n"
          "\n"
          "//Once your HP drops to 0 you die, you only get one life, no do-overs.//\n"
          "\n"
          "//during fights you'll have choices to atttack, heal, anaylsis, or retreat\n"
          "Everything has a certain chance of happening.// \n"
          "\n"
          "//1 - ATTACK:\n"
          "-Heavy attacks have a 25% chance to land a strike and deal a extra 125% dmg\n"
          "-Normal attacks have a 50% chance to hit and deal monderate dmg\n"
          "-Quick attacks have a 75% chance to hit but ony deal 35% of all dmg//\n"
          "\n"
          "//2 - ANALYSIS:\n"
          "Take a turn to analysis your ENEMY's Stats such as HP, Dmg chance, or \n"
          "any special effects such as burning, healing or poison. Recommend only\n"
          "using this on stronger unknown enemyies.//\n"
          "\n"
          "//3 - ITEMS:\n"
          "Spend a turn to use any ITEMS such as POTIONS, speical healing items\n"
          "or any dmg boosters or magic spells. Once you use an item weither if\n"
          "it fails or succeeds, it is only a one time use... most of the time.//\n"
          "\n"
          "//4 - SELF CHECK:\n"
          "Quickly check yourself for any effects or if you just want to overall\n"
          "see how yourself is doing and what your stats are. This won't take up\n"
          "a turn no matter how many times you look at yourself.//\n"
          "\n"
          "//5 - FLEE:\n"
          "If you think you have no chance in fighting an enemy or know you are \n"
          "going to die, take a chance to run if it's the last enemy based on how\n"
          "high your DEX Skill. If it's a boss then you can not flee.\n"
          "\n"
          "//6 - HELP:\n"
          "Need a reminder back to what everything means then you can type 6 for\n"
          "help. Disclaimer, in the future the stats will remain deault in help\n"
          "but to check actual stats use SELF CHECK//\n"
          "\n"
          "//7 - DEFENSE:\n"
          "As you are getting attack, you have choices too,\n"
          "Negate- 75% chance to avoide 25% of dmg\n"
          "Block- 50% chance to avoide 50% of dmg\n"
          "Dodge - 25% chance to take no dmg at all\n")
    input("///PRESS ENTER TO CONTINUE///")

def leveling_up_player():
    global Player_level
    global Player_xp
    global Player_health
    if Player_xp >= Playerxplimits[Player_level]:
        Player_xp = Player_xp - Playerxplimits[Player_level]
        Player_level = Player_level + 1
        Spacer()
        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        print("CONGRATULATIONS! YOU ARE NOW LEVEL - " + str(Player_level))        #HP STR DEX
        levelup_highskill()
        levelup_medskill()
        levelup_lowskill()
        Player_health = Player_HP
        playerinfo()
        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
        input("\n ///PRESS ENTER TO CONTINUE///")

def levelup_highskill():
    global Player_HP
    global Player_STR
    global Player_DEX
    if HighP == "STR":
        Player_STR = Player_STR + High_Prinum
    elif HighP == "DEX":
        Player_DEX = Player_DEX + High_Prinum
    elif HighP == "HP":
        Player_HP = Player_HP + High_Prinum

def levelup_medskill():
    global Player_HP
    global Player_STR
    global Player_DEX
    if MedP == "STR":
        Player_STR = Player_STR + Med_Prinum
    elif MedP == "DEX":
        Player_DEX = Player_DEX + Med_Prinum
    elif MedP == "HP":
        Player_HP = Player_HP + Med_Prinum

def levelup_lowskill():
    global Player_HP
    global Player_STR
    global Player_DEX
    if LowP == "STR":
        Player_STR = Player_STR + Low_Prinum
    elif LowP == "DEX":
        Player_DEX = Player_DEX + Low_Prinum
    elif LowP == "HP":
        Player_HP = Player_HP + Low_Prinum

def fighting_intiate():
    global Player_xp
    global Player_level
    global Enemycount
    global SCORE
    if Enemycount == 0:                #So there is no 0 enemys on the feild
        Enemycount = 1
    while Enemycount > 0:
        Enemyspawn()
        print("There are : " + str(Enemycount) + " Enemy's left")
        print("A " + Enemy_name + " Spots you!")
        fighting_dur()
        Enemycount = Enemycount - 1
        print("XP GAINED: " + str(Enemyxp))
        Player_xp = Player_xp + Enemyxp
        SCORE = SCORE + Enemyxp
        SCORE = SCORE + round(EnemyLv * 100)
        leveling_up_player()
        Spacer()
        ENTER()
    print("There are no more ENEMYS in the area.")
    input("\n PRESS ENTER TO CONTINUE")

def dodgetactic():
    global dmg_avoided

    dodgechoice_print()
    player_choiced = input("")
    if player_choiced == "1":
        Negate_chance = random.randint(1,100)
        Negate_miss = 100 * Negate
        if Negate_chance - Player_speed <= Negate_miss:
            dmg_avoided = Negate_adapator
            print("You Negate some of the attack")
        else:
            dmg_avoided = 0.0
            print("you failed to Negate some of the attack")
    elif player_choiced == "2":
        Block_chance = random.randint(1,100)
        Block_miss = 100 * Block
        if Block_chance - Player_speed <= Block_miss:
            dmg_avoided = Block_adaptor
            print("You Block some of the attack")
        else:
            dmg_avoided = 0.0
            print("You failed to block some of the attack.")
    elif player_choiced == "3":
        Dodge_chance = random.randint(1,100)
        Dodge_miss = 100 * Dodge
        if Dodge_chance - Player_speed <= Dodge_miss:
            dmg_avoided = Dodge_adaptor
            print("You dodged the attack")
        else:
            dmg_avoided = 0.0
            print("failed to dodge")
    elif player_choiced == "4":
        print("NEGATE CHANCE: " + str(Negate * 100) + "% to avoid [" + str(Negate_adapator * 100) + "% dmg]")
        print("BLOCK CHANCE: " + str(Block * 100) + "% to avoid [" + str(Block_adaptor * 100) + "% dmg]")
        print("DODGE CHACNE: " + str(Dodge * 100) + "% to avoid [" + str(Dodge_adaptor * 100) + "% dmg]")
        input("PRESS ENTER TO RETURN")
        dodgetactic()
    else:
        print("PICK A CHOICE")
        dodgetactic()



def fighting_dur():
    global Enemyhp
    global Player_health
    global Whos_turn
    global Potions_num
    global Which_item
    global Enemyxp
    global SCORE

    if Player_health <= 0:
        print("死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死")
        print("YOU ARE DEAD")
        print("GAME OVER")
        print("死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死")
        quit()


    if Whos_turn == "P":
        Whos_turn = "E"
        fight_Playerdmg()
        fight_Enemy_dodge()
        if Enemyhp >= 0:
            taskbar_print()
            print("YOUR TURN...")
            choice = input("")
            if choice == "1":
                attack_print()
                choice_A = input("")
                if choice_A == "1":
                    #quick attack
                    Q_chance = random.randint(1,100)
                    Q_hit = 100 * Quick_atk
                    if Q_chance - Player_speed <= Q_hit:
                        Enemyhp = Enemyhp - round((Player_dmg * Quickatk_adapter))
                        Whos_turn = "E"
                        print("DMG DEALT TO " +  Enemy_name + ": " + str(round(Player_dmg * Quickatk_adapter)))
                        Spacer()
                        print(Enemy_name + " HP: " + str(Enemyhp))
                        print(Player_Name + " HP: " + str(Player_health))
                        SCORE = SCORE + round(Player_dmg * Quickatk_adapter)
                        input("\n ///PRESS ENTER TO CONTINUE///")
                        Spacer()
                        fighting_dur()
                    else:
                        print("YOU MISSED")
                        Spacer()
                        print(Enemy_name + " HP: " + str(Enemyhp))
                        print(Player_Name + " HP: " + str(Player_health))
                        input("\n ///PRESS ENTER TO CONTINUE///")
                        Spacer()
                        Whos_turn = "E"
                        fighting_dur()
                elif choice_A == "2":
                    N_chance = random.randint(1,100)
                    N_hit = 100 * Normal_atk
                    if N_chance - Player_speed <= N_hit:
                        Enemyhp = Enemyhp - round((Player_dmg * Normalatk_adapter))
                        Whos_turn = "E"
                        print("DMG DEALT TO " + Enemy_name + ": " + str(round(Player_dmg * Normalatk_adapter)))
                        Spacer()
                        print(Enemy_name + " HP: " + str(Enemyhp))
                        print(Player_Name + " HP: " + str(Player_health))
                        SCORE = SCORE + round(Player_dmg * Normalatk_adapter)
                        input("\n ///PRESS ENTER TO CONTINUE///")
                        Spacer()
                        fighting_dur()
                    else:
                        print("YOU MISSED")
                        Spacer()
                        print(Enemy_name + " HP: " + str(Enemyhp))
                        print(Player_Name + " HP: " + str(Player_health))
                        input("\n ///PRESS ENTER TO CONTINUE///")
                        Spacer()
                        Whos_turn = "E"
                        fighting_dur()
                elif choice_A == "3":
                    H_chance = random.randint(1,100)
                    H_hit = 100 * Heavy_atk
                    if H_chance - Player_speed <= H_hit:
                        Enemyhp = Enemyhp - round((Player_dmg * Heavyatk_adapter))
                        Whos_turn = "E"
                        print("DMG DEALT TO " + Enemy_name + ": " + str(round(Player_dmg * Heavyatk_adapter)))
                        Spacer()
                        print(Enemy_name + " HP: " + str(Enemyhp))
                        print(Player_Name + " HP: " + str(Player_health))
                        SCORE = SCORE + round(Player_dmg * Heavyatk_adapter)
                        input("\n ///PRESS ENTER TO CONTINUE///")
                        Spacer()
                        fighting_dur()
                    else:
                        print("YOU MISSED")
                        Spacer()
                        print(Enemy_name + " HP: " + str(Enemyhp))
                        print(Player_Name + " HP: " + str(Player_health))
                        input("\n ///PRESS ENTER TO CONTINUE///")
                        Spacer()
                        Whos_turn = "E"
                        fighting_dur()
                else:
                    Whos_turn = "P"
                    fighting_dur()

            elif choice == "2":
                Spacer()
                print( Enemy_name + " | LV." + str(EnemyLv)) #enemy str & dex
                print("STR: " + str(Enemystr))
                print("DEX: " + str(Enemydex))
                print("HP: " + str(Enemyhp))
                print("DMG CHANCE: " + str(round(Enemystr/2)) + " - " + str(Enemystr))
                print("XP: " + str(Enemyxp))
                print("NOTES: " + Enemy_notes)
                Spacer()
                input("\n ///PRESS ENTER TO CONTINUE///")
                Whos_turn = "P"
                fighting_dur()

            elif choice == "3":     #ITEMS
                items_print()
                choice_C = input("")
                if choice_C == "0":
                    if Potions_num > 0: #potions
                        Healing = round(Player_health * Potions_heal)
                        print("YOU HEAl: " + str(Player_health) + " +" + str(Healing))
                        Player_health = Player_health + Healing
                        print("HP: " + str(Player_health))
                        input("///PRESS ENTER TO CONTINUE")
                        Potions_num = Potions_num - 1
                        Whos_turn = "E"
                        if Player_health > Player_HP:
                            Player_health = Player_HP
                        fighting_dur()
                    else:
                        Spacer()
                        print("You are out of HP-POTIONS...")
                        input("///PRESS ENTER TO CONTINUE///")
                        Whos_turn = "P"
                        fighting_dur()
                elif choice_C == "1":
                    if Itemspot1_name == "empty":
                        Spacer()
                        print("YOU DO NOT HAVE AN ITEM IN THAT SLOT")
                        input("///PRESS ENTER TO CONTINUE///")
                        Whos_turn = "P"
                        fighting_dur()
                    else:
                        Spacer()
                        print("USE " + Itemspot1_name + "? (1 - yes / 2 - no)")
                        confirm_1 = input("")
                        if confirm_1 == "1":
                            USEITEM()
                            Whos_turn = "E"
                            fighting_dur()
                        else:
                            Whos_turn = "P"
                            fighting_dur()
                elif choice_C == "2":
                    if Itemspot2_name == "empty":
                        Spacer()
                        print("YOU DO NOT HAVE AN ITEM IN THAT SLOT")
                        input("///PRESS ENTER TO CONTINUE///")
                        Whos_turn = "P"
                        fighting_dur()
                    else:
                        Spacer()
                        print("USE " + Itemspot2_name + "? (1 - yes / 2 - no)")
                        confirm_2 = input("")
                        if confirm_2 == "1":
                            USEITEM()
                            Whos_turn = "E"
                            fighting_dur()
                        else:
                            Whos_turn = "P"
                            fighting_dur()
                elif choice_C == "3":
                    if Itemspot3_name == "empty":
                        Spacer()
                        print("YOU DO NOT HAVE AN ITEM IN THAT SLOT")
                        input("///PRESS ENTER TO CONTINUE///")
                        Whos_turn = "P"
                        fighting_dur()
                    else:
                        Spacer()
                        print("USE " + Itemspot3_name + "? (1 - yes / 2 - no)")
                        confirm_3 = input("")
                        if confirm_3 == "1":
                            USEITEM()
                            Whos_turn = "E"
                            fighting_dur()
                        else:
                            Whos_turn = "P"
                            fighting_dur()
                elif choice_C == "4":
                    if Itemspot4_name == "empty":
                        Spacer()
                        print("YOU DO NOT HAVE AN ITEM IN THAT SLOT")
                        input("///PRESS ENTER TO CONTINUE///")
                        Whos_turn = "P"
                        fighting_dur()
                    else:
                        Spacer()
                        print("USE " + Itemspot4_name + "? (1 - yes / 2 - no)")
                        confirm_4 = input("")
                        if confirm_4 == "1":
                            USEITEM()
                            Whos_turn = "E"
                            fighting_dur()
                        else:
                            Whos_turn = "P"
                            fighting_dur()
                elif choice_C == "5":
                    Spacer()
                    print("POTIONS: " + str(Potions_num)) #shows inventory
                    print("ITEM 1: " + Itemspot1_name)
                    print("ITEM 2: " + Itemspot2_name)
                    print("ITEM 3: " + Itemspot3_name)
                    print("ITEM 4: " + Itemspot4_name)
                    input("///PRESS ENTER TO CONTINUE///")
                    Whos_turn = "P"
                    fighting_dur()
                else:
                    Whos_turn = "P"
                    fighting_dur()

            elif choice == "4":
                selfcheck_print()
                input("\n ///PRESS ENTER TO CONTINUE///")
                Spacer()
                Whos_turn = "P"
                fighting_dur()

            elif choice == "5":
                flee_print()
                choice_D = input("")
                if choice_D == "1":
                    if Boss_enemy == True:
                        print("Can't flee from a boss")
                        Whos_turn = "P"
                        fighting_dur()
                    else:
                        print("YOU TRY TO RUN?...")
                        run_away_chance = Enemydex
                        player_run_away = random.randint(0, Player_DEX)
                        if player_run_away > run_away_chance:
                            Spacer()
                            print("You have successfully fled away from " + Enemy_name)
                            Enemyxp = 50 #so you don't get full xp for running away
                            ENTER()
                            Whos_turn = "P"
                        else:
                            Spacer()
                            print("You failed to run away...")
                            ENTER()
                            Whos_turn = "E"
                            fighting_dur()
                else:
                    Whos_turn = "P"
                    fighting_dur()
            elif choice == "6":
                help_menu_print()
                Whos_turn = "P"
                fighting_dur()
            else:
                Whos_turn = "P"
                fighting_dur()
        else:
            print("The " + Enemy_name +" is dead.")

    elif Whos_turn == "E":      #ENEMY'S TURN
        Whos_turn = "P"
        fight_Enemy_dmg()
        fight_Playerspeed()
        if Enemyhp > 0:              #note here to put in dodge mechanics
            print(Enemy_name + " is attacking...")
            Enemyatkchoice = random.randint(1,3)
            if Enemyatkchoice == 1:
                QE_chance = random.randint(1,100)
                if QE_chance <= 90:
                    Spacer()
                    print("QUICK attack incomming...")
                    dodgetactic()
                    print("DMG AVOIDED: " + str(round(Enemydmg * dmg_avoided)))
                    dmg_given_quick = round((Enemydmg * .75)) - round(Enemydmg * dmg_avoided)
                    print_Q_dmg = round((Enemydmg * .75))
                    if dmg_given_quick <= -1:                                   # so a negivtive dmg doesn't heal player
                        dmg_given_quick = 0
                    Player_health = Player_health - dmg_given_quick
                    Whos_turn = "P"
                    print("DMG DEALT TO YOU: " + str(print_Q_dmg) + " (-" + str(round(Enemydmg * dmg_avoided)) + ")")
                    Spacer()
                    print(Enemy_name + " HP: " + str(Enemyhp))
                    print(Player_Name + " HP: " + str(Player_health))
                    SCORE = SCORE + round(Enemydmg + dmg_given_quick)
                    input("\n ///PRESS ENTER TO CONTINUE///")
                    Spacer()
                    fighting_dur()
                else:
                    Spacer()
                    print(Enemy_name+ " MISSED")
                    Whos_turn = "P"
                    ENTER()
                    Spacer()
                    print(Enemy_name + " HP: " + str(Enemyhp))
                    print(Player_Name + " HP: " + str(Player_health))
                    input("\n ///PRESS ENTER TO CONTINUE///")
                    Spacer()
                    fighting_dur()
            elif Enemyatkchoice == 2:
                NE_chance = random.randint(1,100)
                if NE_chance <= 75:
                    print("NORMAL attack incomming...")
                    Spacer()
                    dodgetactic()
                    print("DMG AVOIDED: " + str(round(Enemydmg * dmg_avoided)))
                    dmg_given_normal = round((Enemydmg)) - round(Enemydmg * dmg_avoided)
                    print_N_dmg = round((Enemydmg))
                    if dmg_given_normal <= -1:                  #so negitvae dmg doesn't heal
                        dmg_given_normal = 0
                    Player_health = Player_health - dmg_given_normal
                    Whos_turn = "P"
                    print("DMG DEALT TO YOU: " + str(print_N_dmg) + " (-" + str(round(Enemydmg * dmg_avoided)) + ")")
                    Spacer()
                    print(Enemy_name + " HP: " + str(Enemyhp))
                    print(Player_Name + " HP: " + str(Player_health))
                    SCORE = SCORE + round(Enemydmg + dmg_given_normal)
                    input("\n ///PRESS ENTER TO CONTINUE///")
                    Spacer()
                    fighting_dur()
                else:
                    Spacer()
                    print(Enemy_name + " MISSED")
                    ENTER()
                    Whos_turn = "P"
                    Spacer()
                    print(Enemy_name + " HP: " + str(Enemyhp))
                    print(Player_Name + " HP: " + str(Player_health))
                    input("\n ///PRESS ENTER TO CONTINUE///")
                    Spacer()
                    fighting_dur()
            else:
                HE_chance = random.randint(1,100)
                if HE_chance <= 50:
                    Spacer()
                    print("HEAVY attack incomming...")
                    dodgetactic()
                    print("DMG AVOIDED: " + str(round(Enemydmg * dmg_avoided)))
                    dmg_given_heavy = round((Enemydmg * 1.5)) - round(Enemydmg * dmg_avoided)
                    print_H_dmg = round((Enemydmg * 1.5))
                    if dmg_given_heavy <= -1:
                        dmg_given_heavy = 0
                    Player_health = Player_health - dmg_given_heavy
                    Whos_turn = "P"
                    print("DMG DEALT TO YOU: " + str(print_H_dmg) + " (-" + str(round(Enemydmg * dmg_avoided)) + ")")
                    Spacer()
                    print(Enemy_name + " HP: " + str(Enemyhp))
                    print(Player_Name + " HP: " + str(Player_health))
                    SCORE = SCORE + round(Enemydmg + dmg_given_heavy)
                    input("\n ///PRESS ENTER TO CONTINUE///")
                    Spacer()
                    fighting_dur()
                else:
                    Spacer()
                    print(Enemy_name + " MISSED")
                    ENTER()
                    Spacer()
                    print(Enemy_name + " HP: " + str(Enemyhp))
                    print(Player_Name + " HP: " + str(Player_health))
                    input("\n ///PRESS ENTER TO CONTINUE///")
                    Spacer()
                    Whos_turn = "P"
                    fighting_dur()
        else:
            print("The " + Enemy_name + " is dead.")

def USEITEM():
    global Player_health
    global Enemyhp
    global Itemspot1_name
    global Itemspot2_name
    global Itemspot3_name
    global Itemspot4_name

    if Which_item == 1:         ############USE item 1
        Spacer()
        print("USING: " + Itemspot1_name)
        if Item1_type == "D":
            Spacer()
            print(Itemspot1_name + " DEALS: " + str(Itemnum1) + " DMG to " + Enemy_name)
            Itemspot1_name = "empty"
            input("///PRESS ENTER TO CONTINUE///")
            fighting_dur()
        else:
            Spacer()
            print(Itemspot1_name + " HEALS YOU FOR: +" + str(Itemnum1))
            Itemspot1_name = "empty"
            input("///PRESS ENTER TO CONTINUE")
    elif Which_item == 2:         ############USE item 2
        Spacer()
        print("USING: " + Itemspot2_name)
        if Item2_type == "D":
            Spacer()
            print(Itemspot2_name + " DEALS: " + str(Itemnum2) + " DMG to " + Enemy_name)
            Itemspot2_name = "empty"
            input("///PRESS ENTER TO CONTINUE///")
            fighting_dur()
        else:
            Spacer()
            print(Itemspot2_name + " HEALS YOU FOR: +" + str(Itemnum2))
            Itemspot2_name = "empty"
            input("///PRESS ENTER TO CONTINUE")
    elif Which_item == 3:         ############USE item 3
        Spacer()
        print("USING: " + Itemspot3_name)
        if Item3_type == "D":
            Spacer()
            print(Itemspot3_name + " DEALS: " + str(Itemnum3) + " DMG to " + Enemy_name)
            Itemspot3_name = "empty"
            input("///PRESS ENTER TO CONTINUE///")
            fighting_dur()
        else:
            Spacer()
            print(Itemspot3_name + " HEALS YOU FOR: +" + str(Itemnum3))
            Itemspot3_name = "empty"
            input("///PRESS ENTER TO CONTINUE")
    elif Which_item == 4:         ############USE item 4
        Spacer()
        print("USING: " + Itemspot4_name)
        if Item4_type == "D":
            Spacer()
            print(Itemspot4_name + " DEALS: " + str(Itemnum4) + " DMG to " + Enemy_name)
            Itemspot4_name = "empty"
            input("///PRESS ENTER TO CONTINUE///")
            fighting_dur()
        else:
            Spacer()
            print(Itemspot4_name + " HEALS YOU FOR: +" + str(Itemnum4))
            Itemspot4_name = "empty"
            input("///PRESS ENTER TO CONTINUE")

def playerinfo():
    print(Player_Name + " Lv." + str(Player_level))
    print("Gender: " + Player_Gender)
    print("Class: " + Player_Class)
    printstr()
    printdex()
    printhp()
    print("Weapon: " + Player_Weapon.name)
    print("XP: " + str(Player_xp))
    print("XP TILL NEXT LEVEL: " + str(Playerxplimits[Player_level]))

def printstr():
    if HighP == "STR":
        print("STR: " + str(Player_STR) + " (+" + str(High_Prinum) + ")")
    if MedP == "STR":
        print("STR: " + str(Player_STR) + " (+" + str(Med_Prinum) + ")")
    if LowP == "STR":
        print("STR: " + str(Player_STR) + " (+" + str(Low_Prinum) + ")")
def printdex():
    if HighP == "DEX":
        print("DEX: " + str(Player_DEX) + " (+" + str(High_Prinum) + ")")
    if MedP == "DEX":
        print("DEX: " + str(Player_DEX) + " (+" + str(Med_Prinum) + ")")
    if LowP == "DEX":
        print("DEX: " + str(Player_DEX) + " (+" + str(Low_Prinum) + ")")
def printhp():
    if HighP == "HP":
        print("HP: " + str(Player_HP) + " (+" + str(High_Prinum) + ")")
    if MedP == "HP":
        print("HP: " + str(Player_HP) + " (+" + str(Med_Prinum) + ")")
    if LowP == "HP":
        print("HP: " + str(Player_HP) + " (+" + str(Low_Prinum) + ")")

def Stat_setup():
    global HighP
    global MedP
    global LowP
    global classarry              # To make sure that you can only choose one for each choice

    print("What priority would you like your skills?\n")
    print("///When leveling up you're skills will go up based on priority///\n\n")
    print("1 - Strength (How strong you're attack are and dmg you deal.)")
    print("2 - Dexterity   (How fast and quick you are to do things like dodging or running.)")
    print("3 - HP (Your health points is how much life you have and dmg you can take.)\n\n\n")
    Spacer()
    highskillset()
    Spacer()
    medskillset()
    Spacer()
    lowskillset()
    classarry = ["1","2","3"]
    Spacer()
    print("Are you satisfy with your skills and stats? (1 - yes/ 2 - no)\n")
    print("Strongest Skill: " + HighP)
    print("Balanced Skill: " + MedP)
    print("Weakest Skill: " + LowP)
    redochoice = input("")
    if redochoice == "2":
        print("\nAre you sure you wanna redo your skills? (1 - yes/ 2 - no)\n")
        redo2 = input("")
        if redo2 == "1":
            Stat_setup()
        else:
            Spacer()
    else:
        Spacer()

def highskillset():
    global HighP
    global classarry
    print("What skill would you like to be HIGH PRIORITY?: ")
    first_skillchoice = input("")
    if first_skillchoice == "1":
        HighP = "STR"
        classarry.remove(first_skillchoice)
    elif first_skillchoice == "2":
        HighP = "DEX"
        classarry.remove(first_skillchoice)
    elif first_skillchoice == "3":
        HighP = "HP"
        classarry.remove(first_skillchoice)
    else:
        print("Please pick 1, 2, or 3 to set a skill. (No spaces)")
        Spacer()
        highskillset()
def medskillset():
    global MedP
    global classarry
    print("What skill would you like to be MEDIUM PRIORITY?: ")
    second_skillchoice = input("")
    if second_skillchoice == "1":
        if "1" in classarry:
            MedP = "STR"
            classarry.remove(second_skillchoice)
        else:
            print("You already set your STR skill")
            medskillset()
    elif second_skillchoice == "2":
        if "2" in classarry:
            MedP = "DEX"
            classarry.remove(second_skillchoice)
        else:
            print("You already set your DEX skill")
            medskillset()
    elif second_skillchoice == "3":
        if "3" in classarry:
            MedP = "HP"
            classarry.remove(second_skillchoice)
        else:
            print("You already set your HP skill")
            Spacer()
            medskillset()
    else:
        print("Please pick 1,2, or 3 to set a skill. (No spaces)")
        medskillset()
def lowskillset():
    global LowP
    global classarry
    print("What skill would you like to be LOW PRIORITY?: ")
    third_skillchoice = input("")
    if third_skillchoice == "1":
        if "1" in classarry:
            LowP = "STR"
            classarry.remove(third_skillchoice)
        else:
            print("You already set your STR skill")
            lowskillset()
    elif third_skillchoice == "2":
        if "2" in classarry:
            LowP = "DEX"
            classarry.remove(third_skillchoice)
        else:
            print("You already set your DEX skill")
            lowskillset()
    elif third_skillchoice == "3":
        if "3" in classarry:
            LowP = "HP"
            classarry.remove(third_skillchoice)
        else:
            print("You already set your HP skill")
            lowskillset()
    else:
        print("Please pick 1,2, or 3 to set a skill. (No spaces)")
        Spacer()
        lowskillset()

def weaponsetter():
    global Player_Class
    global Player_Weapon
    if Player_Class == "Warrior":
        Player_Weapon = Player_Weapon_create("Copper Sword [1d6]")
        Player_Weapon_create.weapon_dmg_set(Player_Weapon, Weapon_min_value, Weapon_max_value, Weapon_s_value)
    if Player_Class == "Archer":
        Player_Weapon = Player_Weapon_create("Wooden Bow [1d6]")
        Player_Weapon_create.weapon_dmg_set(Player_Weapon, Weapon_min_value, Weapon_max_value, Weapon_s_value)
    if Player_Class == "Spartan":
        Player_Weapon = Player_Weapon_create("Copper Axe [1d6]")
        Player_Weapon_create.weapon_dmg_set(Player_Weapon, Weapon_min_value, Weapon_max_value, Weapon_s_value)




def Spacer():
    print("-------------------------------------------------------------------------------------------")

def Title_screen():
    # title screen
    print("===========================================================================================")
    time.sleep(0.25)
    print("+                     _ _                _   _______   ____   _     []    _ _             +")
    time.sleep(0.25)
    print("+      /\    /\     /     \   |\   |   /  \     |     |      |  \   []   |   /    \   /   +")
    time.sleep(0.25)
    print("+     /  \  /  \   |       |  | \  |   \        |     |__    |  /   []   |__/      \ /    +")
    time.sleep(0.25)
    print("+    /    \/    \  |       |  |  \ |     \      |     |      | \    []   |          |     +")
    time.sleep(0.25)
    print("+   /            \  \ _ _ /   |   \|   \__/     |     |____  |  \   [] . |          |     +")
    time.sleep(0.25)
    print("===========================================================================================")
    time.sleep(0.25)
    print("")

# intro menu
def Intro_scene():
    print("!!!Welcome to Monster.PY!!!")
    time.sleep(0.5)
    print("Your goal is to slay the monsters that have taken over the world and came from the depths of the underworld..." )
    time.sleep(0.5)
    print("Your final objective will be to slay the worst demon of them all...")
    time.sleep(0.5)
    print("!!!THE SYNTAX PYTHON!!!")
    time.sleep(0.5)
    print("But first you must create you....\n")
    time.sleep(1)
    ENTER()

def Menu():
    Title_screen()
    print("Start - to begin")
    Spacer()
    print("Exit - to Leave")
    Spacer()
    print("1 = Start")
    print("2 = Exit")
    now = int(input())
    if now == 1:
        print("The game is begining...")
    else:
        print("Goodbye")
        quit()

def ENTER():
    input("\n///PRESS ENTER TO CONTINUE///\n")

def Diaprint(s):
    for c in s:
        sys.stdout.write(c)
        time.sleep(0.05)
    time.sleep(0.25)

def Storyprint(s):
    print(s)
    time.sleep(0.75)

def Gameover_screen():
    Spacer()
    Spacer()
    Spacer()
    Spacer()
    Spacer()
    print("\n.......####......###......##...##....######.............#####...#.......#...######...#####...")
    time.sleep(0.5)
    print("......#.........#...#....#..#.#..#...#.................#.....#...#.....#....#........#...#...")
    time.sleep(0.5)
    print(".....#...###...#######...#...#...#...####..............#.....#....#...#.....####.....####....")
    time.sleep(0.5)
    print(".....#....#....#.....#...#.......#...#.................#.....#.....#.#......#........#..#....")
    time.sleep(0.5)
    print("......####.....#.....#...#.......#...######.............#####.......#.......######...#...#...")
    time.sleep(1)
    print("=============================================================================================")
    print("===== " + Player_Name + "  -  SCORE: " + SCORE + " =====")
    print("=============================================================================================\n")
    Spacer()
    Spacer()
    Spacer()
    Spacer()
    Spacer()
    quit()


######################MENU###########################
#Menu()
#Intro_scene()
#Player_Create()
#Enemycount = 3
#fighting_intiate()

#####################MENU############################
def Prolouge_title():
    Spacer()
    print("........#######....#....#...............###.......")
    time.sleep(0.25)
    print("........#.....#....#....#............##..##.......")
    time.sleep(0.25)
    print("........#..........######................##.......")
    time.sleep(0.25)
    print("........#.... #    #....#.......##.......##.......")
    time.sleep(0.25)
    print("........#######....#....#.......##....#######.....")
    time.sleep(0.25)
    print("==================================================")
    print("==CHAPTER 1 - GETTING OUT OF THIS PLACE FINALLY!==")
    print("==================================================")
    time.sleep(0.5)
    Spacer()
    ENTER()


def Prolouge_scene():
    Storyprint("Prolouge...")
    Storyprint("Your world has been taken over...")
    Storyprint("One day the depth of the underworld has crested open...")
    Storyprint("Monsters come out one by one slautering, kidnapping, and killing everyone they see...")
    Storyprint("They've taken over the major towns...")
    Storyprint("You and a small group of survivors retreat into a fallout bunker a month ago when the world began to end...")
    Storyprint("All of you can defend and protect each other, however... food is running low...")
    Storyprint("Everyone has their fair share, but all you have is your " + Player_Weapon.name + " and a few scraps left...")
    Storyprint("You throw away your moldy bread, You are tired of rotting away, you tell yourself it's our turn to fight back!")
    Spacer()
    ENTER()
    ENTER()
    Spacer()
    Diaprint("|" + Player_Name + ": That's it! I'm Done!\n")
    Diaprint("|Another Skinny Survivor: What do you mean " + Player_Name + " ?\n")
    Diaprint("|" + Player_Name + ": I am done with all this bullshit!\n")
    Spacer()
    ENTER()
    ENTER()
    Spacer()
    Storyprint("You hype yourself up and start a scene\n")
    Diaprint("|" + Player_Name + ": I want to fight! I want to take back what is ours!\n")
    Storyprint("everyone stares as you stand.\n")
    Diaprint("|" + Player_Name + ": So who is with me!\n")
    Storyprint("No one responds")
    Storyprint("You get ready to leave which was always a option in the first place.")
    Storyprint("You grab your " + Player_Weapon.name + " and walk near the exit of the bunker. ")
    Spacer()
    ENTER()
    Spacer()
    Diaprint("|Leader: *He hesitates to let you out.* are you sure you want to leave, " + Player_Name + "?")
    print("1 - Yes! I AM LEAVING!\n"
          "2 - Actually, I think I'll stay, it's not safe out there...\n")
    ask1 = int(input())
    time.sleep(1)
    if ask1 == 2:
        Diaprint("|" + Player_Name + ": Actually, I think I'll stay it's not safe out there...\n")
        Diaprint("|Leader: Alright then, I thought you were suicidal for a minute. I know it's hard\n"
                 "         but we will survive though. Don't give up.")
        Storyprint("You decided to stay and live the rest of your life inside the buncker...")
        Storyprint("Eventually, everyone runs out of food but is too weak and hungry to deal with anything...")
        Storyprint("You close your eyes... and next thing you know...")
        Storyprint("You don't wake up... you STARVE TO DEATH...")
        Gameover_screen()
    else:
        Diaprint("|" + Player_Name + ": Yes! I AM LEAVING! LET ME OUT! I WOULD RATHER FIGHT THAN\n"
                                      "STAY IN HERE ANOTHER DAY!")
    




######################CH.1###########################
Prolouge_title()
Prolouge_scene()

######################CH.1###########################

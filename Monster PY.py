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

class Boss_create:
    def __init__(self, name):
        self.name = name

    def assign_stats(self, str, dex, hp, lv):
        self.str = str
        self.dex = dex
        self.hp = hp
        self.lv = lv

    def assign_notes(self, string):
        self.notes = string

class Item_create:
    def __init__(self, name):
        self.name = name

    def assign_stats(self, num, type):
        self.num = num
        self.type = type

Player_Weapon = Player_Weapon_create("empty")
Chapter_Boss = Boss_create("empty")
Item_adding = Item_create("empty")

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
Potions_heal = .60
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

#Dodge chances
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
    print("2 - Archer  (Speed and use of any weapon)")
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
            print("Please wait...")
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
    Enemy_notes = ""
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
    print("Weapon: " + Player_Weapon.name)
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
          "How strong is your weapon, How high is your strength, and if you deal a \n"
          "critical strike or not. Weapons Dmg is based on the type of material it's \n"
          "made out of. There are different and unknown materials in this world \n"
          "that have been brought by (or made out of) the monsters. Your strength will \n"
          "naturally grow, but some quests can help quickly increase your overall skill.\n"
          "Critical strikes will be based on both your stats and the weapon.//\n"
          "\n"
          "//Once your HP drops to 0 you die, you only get one life, no do-overs.//\n"
          "\n"
          "//During fights, you'll have choices to attack, heal, analysis, or retreat\n"
          "Everything has a certain chance of happening.// \n"
          "\n"
          "//1 - ATTACK:\n"
          "-Heavy attacks have a 25% chance to land a strike and deal a extra 125% dmg.\n"
          "-Normal attacks have a 50% chance to hit and deal monderate dmg.\n"
          "-Quick attacks have a 75% chance to hit but ony deal 35% of all dmg.//\n"
          "\n"
          "//2 - ANALYSIS:\n"
          "Take a turn to analysis your ENEMY's Stats such as HP, Dmg chance, or \n"
          "any special effects such as burning, healing or poison. Recommend only\n"
          "using this on stronger unknown enemyies.//\n"
          "\n"
          "//3 - ITEMS:\n"
          "Spend a turn to use any ITEMS such as POTIONS, speical healing items,\n"
          "or any dmg boosters or magic spells. Once you use an item whether if\n"
          "it fails or succeeds, it is only an one time use... most of the time.//\n"
          "\n"
          "//4 - SELF CHECK:\n"
          "Quickly check yourself for any effects or if you just want to overall\n"
          "see how you are doing and what your stats are. This won't take up\n"
          "a turn no matter how many times you look at yourself.//\n"
          "\n"
          "//5 - FLEE:\n"
          "If you think you have no chance in fighting an enemy or know you are \n"
          "going to die, take a chance to run if it's the last enemy based on how\n"
          "high your DEX Skill is. If it's a boss then you cannot flee.\n"
          "\n"
          "//6 - HELP:\n"
          "Need a reminder back to what everything means? Then you can type 6 for\n"
          "help. Disclaimer: in the future the stats will remain default in help,\n"
          "but to check actual stats use SELF CHECK.//\n"
          "\n"
          "//7 - DEFENSE:\n"
          "As you are getting attacked, you have choices too,\n"
          "Negate- 75% chance to avoid 25% of dmg.\n"
          "Block- 50% chance to avoid 50% of dmg.\n"
          "Dodge - 25% chance to take no dmg at all.\n")
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
        print("There are : " + str(Enemycount) + " enemies left")
        print("A " + Enemy_name + " spots you!")
        fighting_dur()
        Enemycount = Enemycount - 1
        print("XP GAINED: " + str(Enemyxp))
        Player_xp = Player_xp + Enemyxp
        SCORE = SCORE + Enemyxp
        SCORE = SCORE + round(EnemyLv * 100)
        leveling_up_player()
        Spacer()
        ENTER()
    print("There are no more ENEMIES in the area.")
    ENTER()
    Spacer()

def Boss_fighting_intiate():
    global Player_xp
    global Player_level
    global SCORE
    fighting_dur()
    print("XP GAINED: " + str(Enemyxp))
    Player_xp = Player_xp + Enemyxp
    SCORE = SCORE + Enemyxp
    SCORE = SCORE + round(EnemyLv * 1000)
    leveling_up_player()
    ENTER()
    Spacer()

def dodgetactic():
    global dmg_avoided

    dodgechoice_print()
    player_choiced = input("")
    if player_choiced == "1":
        Negate_chance = random.randint(1,100)
        Negate_miss = 100 * Negate
        if Negate_chance - Player_speed <= Negate_miss:
            dmg_avoided = Negate_adapator
            print("You Negate some of the damage.")
        else:
            dmg_avoided = 0.0
            print("You failed to Negate some of the damabge.")
    elif player_choiced == "2":
        Block_chance = random.randint(1,100)
        Block_miss = 100 * Block
        if Block_chance - Player_speed <= Block_miss:
            dmg_avoided = Block_adaptor
            print("You Block some of the damage.")
        else:
            dmg_avoided = 0.0
            print("You failed to block some of the damage.")
    elif player_choiced == "3":
        Dodge_chance = random.randint(1,100)
        Dodge_miss = 100 * Dodge
        if Dodge_chance - Player_speed <= Dodge_miss:
            dmg_avoided = Dodge_adaptor
            print("You dodged the attack.")
        else:
            dmg_avoided = 0.0
            print("You failed to dodge.")
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
        print("YOU ARE DEAD, Killed by " + Enemy_name)
        print("死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死死")
        Gameover_screen()


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
                        Healing = round(Player_HP * Potions_heal)
                        print("YOU HEAl: " + str(Player_health) + " +" + str(Healing))
                        Player_health = Player_health + Healing
                        input("///PRESS ENTER TO CONTINUE")
                        Potions_num = Potions_num - 1
                        Whos_turn = "E"
                        if Player_health > Player_HP:
                            Player_health = Player_HP
                        print("HP: " + str(Player_health))
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
                        print("YOU DO NOT HAVE AN ITEM IN THAT SLOT.\n")
                        input("///PRESS ENTER TO CONTINUE///")
                        Whos_turn = "P"
                        fighting_dur()
                    else:
                        Spacer()
                        print("USE " + Itemspot1_name + "? (1 - yes / 2 - no)")
                        confirm_1 = input("")
                        if confirm_1 == "1":
                            Which_item = 1
                            USEITEM()
                            Whos_turn = "E"
                            fighting_dur()
                        else:
                            Whos_turn = "P"
                            fighting_dur()
                elif choice_C == "2":
                    if Itemspot2_name == "empty":
                        Spacer()
                        print("YOU DO NOT HAVE AN ITEM IN THAT SLOT.\n")
                        input("///PRESS ENTER TO CONTINUE///")
                        Whos_turn = "P"
                        fighting_dur()
                    else:
                        Spacer()
                        print("USE " + Itemspot2_name + "? (1 - yes / 2 - no)")
                        confirm_2 = input("")
                        if confirm_2 == "1":
                            Which_item = 2
                            USEITEM()
                            Whos_turn = "E"
                            fighting_dur()
                        else:
                            Whos_turn = "P"
                            fighting_dur()
                elif choice_C == "3":
                    if Itemspot3_name == "empty":
                        Spacer()
                        print("YOU DO NOT HAVE AN ITEM IN THAT SLOT.\n")
                        input("///PRESS ENTER TO CONTINUE///")
                        Whos_turn = "P"
                        fighting_dur()
                    else:
                        Spacer()
                        print("USE " + Itemspot3_name + "? (1 - yes / 2 - no)")
                        confirm_3 = input("")
                        if confirm_3 == "1":
                            Which_item = 3
                            USEITEM()
                            Whos_turn = "E"
                            fighting_dur()
                        else:
                            Whos_turn = "P"
                            fighting_dur()
                elif choice_C == "4":
                    if Itemspot4_name == "empty":
                        Spacer()
                        print("YOU DO NOT HAVE AN ITEM IN THAT SLOT.\n")
                        input("///PRESS ENTER TO CONTINUE///")
                        Whos_turn = "P"
                        fighting_dur()
                    else:
                        Spacer()
                        print("USE " + Itemspot4_name + "? (1 - yes / 2 - no)")
                        confirm_4 = input("")
                        if confirm_4 == "1":
                            Which_item = 4
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
                        print("Did you... really think you can run from a boss... a BOSS?!??! I think not. \n"
                              "GO BACK AND FIGHT THEM COWARD! Tch.\n")
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
            Enemyhp = Enemyhp - Itemnum1
            Itemspot1_name = "empty"
            input("///PRESS ENTER TO CONTINUE///")
            fighting_dur()
        else:
            Spacer()
            print(Itemspot1_name + " HEALS YOU FOR: +" + str(Itemnum1))
            Player_health = Player_health + Itemnum1
            if Player_health > Player_HP:
                Player_health = Player_HP
            print("HP: " + str(Player_health))
            Itemspot1_name = "empty"
            input("///PRESS ENTER TO CONTINUE")
    elif Which_item == 2:         ############USE item 2
        Spacer()
        print("USING: " + Itemspot2_name)
        if Item2_type == "D":
            Spacer()
            print(Itemspot2_name + " DEALS: " + str(Itemnum2) + " DMG to " + Enemy_name)
            Enemyhp = Enemyhp - Itemnum2
            Itemspot2_name = "empty"
            input("///PRESS ENTER TO CONTINUE///")
            fighting_dur()
        else:
            Spacer()
            print(Itemspot2_name + " HEALS YOU FOR: +" + str(Itemnum2))
            Player_health = Player_health + Itemnum2
            if Player_health > Player_HP:
                Player_health = Player_HP
            print("HP: " + str(Player_health))
            Itemspot2_name = "empty"
            input("///PRESS ENTER TO CONTINUE")
    elif Which_item == 3:         ############USE item 3
        Spacer()
        print("USING: " + Itemspot3_name)
        if Item3_type == "D":
            Spacer()
            print(Itemspot3_name + " DEALS: " + str(Itemnum3) + " DMG to " + Enemy_name)
            Enemyhp = Enemyhp - Itemnum3
            Itemspot3_name = "empty"
            input("///PRESS ENTER TO CONTINUE///")
            fighting_dur()
        else:
            Spacer()
            print(Itemspot3_name + " HEALS YOU FOR: +" + str(Itemnum3))
            Player_health = Player_health + Itemnum3
            if Player_health > Player_HP:
                Player_health = Player_HP
            print("HP: " + str(Player_health))
            Itemspot3_name = "empty"
            input("///PRESS ENTER TO CONTINUE")
    elif Which_item == 4:         ############USE item 4
        Spacer()
        print("USING: " + Itemspot4_name)
        if Item4_type == "D":
            Spacer()
            print(Itemspot4_name + " DEALS: " + str(Itemnum4) + " DMG to " + Enemy_name)
            Enemyhp = Enemyhp - Itemnum4
            Itemspot4_name = "empty"
            input("///PRESS ENTER TO CONTINUE///")
            fighting_dur()
        else:
            Spacer()
            print(Itemspot4_name + " HEALS YOU FOR: +" + str(Itemnum4))
            Player_health = Player_health + Itemnum4
            if Player_health > Player_HP:
                Player_health = Player_HP
            print("HP: " + str(Player_health))
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
            print("You've already set your STR skill.")
            lowskillset()
    elif third_skillchoice == "2":
        if "2" in classarry:
            LowP = "DEX"
            classarry.remove(third_skillchoice)
        else:
            print("You've already set your DEX skill.")
            lowskillset()
    elif third_skillchoice == "3":
        if "3" in classarry:
            LowP = "HP"
            classarry.remove(third_skillchoice)
        else:
            print("You've already set your HP skill.")
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
    print("But first you must create... YOU....\n")
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
    print("===== " + Player_Name + "  -  SCORE: " + str(SCORE) + " =====")
    print("=============================================================================================\n")
    quit()

def add_item():
    global Itemspot1_name
    global Itemspot2_name
    global Itemspot3_name
    global Itemspot4_name
    global Itemnum1
    global Itemnum2
    global Itemnum3
    global Itemnum4
    global Item1_type  # D = dmg item | H = Healing item
    global Item2_type
    global Item3_type
    global Item4_type

    if Itemspot1_name == "empty":
        Itemspot1_name = Item_adding.name
        Itemnum1 = Item_adding.num
        Item1_type = Item_adding.type
        print("///" + Item_adding.name + " has been added to ITEM SLOT 1///")
        ENTER()
    elif Itemspot2_name == "empty":
        Itemspot2_name = Item_adding.name
        Itemnum2 = Item_adding.num
        Item2_type = Item_adding.type
        print("///" + Item_adding.name + " has been added to ITEM SLOT 2///")
        ENTER()
    elif Itemspot3_name == "empty":
        Itemspot3_name = Item_adding.name
        Itemnum3 = Item_adding.num
        Item3_type = Item_adding.type
        print("///" + Item_adding.name + " has been added to ITEM SLOT 3///")
        ENTER()
    elif Itemspot4_name == "empty":
        Itemspot4_name = Item_adding.name
        Itemnum4 = Item_adding.num
        Item4_type = Item_adding.type
        print("///" + Item_adding.name + " has been added to ITEM SLOT 4///")
        ENTER()
    else:
        Spacer()
        print("You have too many items, please get rid of one of them.\n\n")
        print("Please choose one item to get rid of...\n")
        print("\n1 - " + Itemspot1_name)
        print("\n2 - " + Itemspot2_name)
        print("\n3 - " + Itemspot3_name)
        print("\n4 - " + Itemspot4_name)
        print("\n0 - " + Item_adding.name)
        ask = input("")
        Spacer()
        if ask == "1":
            print("You left " + Itemspot1_name + " behind...")
            Itemspot1_name = "empty"
            ENTER()
            add_item()
        elif ask == "2":
            print("You left " + Itemspot2_name + " behind...")
            Itemspot2_name = "empty"
            ENTER()
            add_item()
        elif ask == "3":
            print("You left " + Itemspot3_name + " behind...")
            Itemspot3_name = "empty"
            ENTER()
            add_item()
        elif ask == "4":
            print("You left " + Itemspot4_name + " behind...")
            Itemspot4_name = "empty"
            ENTER()
            add_item()
        else:
            print("You decided to not take " + Item_adding.name)
            ENTER()



######################MENU###########################
Menu()
Intro_scene()
Player_Create()

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
    print("===================================================")
    print("==CHAPTER 1 - GETTING OUT OF THIS PLACE, FINALLY!==")
    print("===================================================")
    time.sleep(0.5)
    Spacer()
    ENTER()

def Prolouge_scene():
    global Enemycount
    Storyprint("Prolouge...")
    Storyprint("Your World has been taken over...")
    Storyprint("One day the depth of the Underworld has crested open...")
    Storyprint("Monsters come out one by one.. slautering.. kidnapping.. killing everyone they see...")
    Storyprint("They've even taken over the major towns and cities...")
    Storyprint("You and a small group of survivors retreated into a fallout bunker a month ago when the world began to end...")
    Storyprint("All of you can defend and protect each other, however... food is running dangerously low...")
    Storyprint("Everyone has their fair share, but all you have is your " + Player_Weapon.name + " and a few scraps left...")
    Storyprint("Tired of rotting away, you throw away your moldy bread, you tell yourself it's our turn to fight back!")
    Spacer()
    ENTER()
    ENTER()
    Spacer()
    Diaprint("|" + Player_Name + ": That's it! I'm Done!\n")
    Diaprint("|Another Skinny Survivor: What do you mean " + Player_Name + "?\n")
    Diaprint("|" + Player_Name + ": I am done with all this bullshit!\n")
    Spacer()
    ENTER()
    ENTER()
    Spacer()
    Storyprint("You hype yourself up as you start a scene.\n")
    Diaprint("|" + Player_Name + ": I want to fight! I want to take back what is ours!\n")
    Storyprint("Everyone stares as you stand.\n")
    Diaprint("|" + Player_Name + ": So who is with me?!\n")
    Storyprint("No one responds.")
    Storyprint("You get ready to leave which was always a option in the first place.")
    Storyprint("You grab your " + Player_Weapon.name + " and start to walk near the exit of the bunker. ")
    Spacer()
    ENTER()
    Spacer()
    Diaprint("|Leader: *He hesitates to let you out.* Are you sure you want to leave, " + Player_Name + "?\n")
    Spacer()
    print("\n1 - Yes! I AM LEAVING!\n"
          "2 - Actually, I think I'll stay, it's not safe out there...\n")
    ask1 = int(input())
    time.sleep(1)
    if ask1 == 2:
        Diaprint("|" + Player_Name + ": Actually, I think I'll stay it's not safe out there...\n")
        Diaprint("|Leader: Alright then, I thought you were suicidal for a minute. I know it's hard,\n"
                 "but we will survive this. Don't give up on us.")
        ENTER()
        Storyprint("You decided to stay and live the rest of your life inside the buncker...")
        Storyprint("Eventually, everyone runs out of food but they are too weak and hungry to deal with anything...")
        Storyprint("You close your eyes... and next thing you know...")
        Storyprint("You don't wake up... you STARVE TO DEATH...")
        ENTER()
        Spacer()
        Gameover_screen()
    else:
        Spacer()
        Diaprint("|" + Player_Name + ": Yes! I AM LEAVING! LET ME OUT! I WOULD RATHER FIGHT AND DIE THAN\n"
                                      "STAY IN HERE ANOTHER DAY!\n")
    Diaprint("|Leader: Don't say I didn't warn you... once you leave you can't come back...\n")
    ENTER()
    ENTER()
    Spacer()
    Storyprint("The giant bunker door slowly opens up to allow you to walk through.")
    Storyprint("You walk outside and are blinded by the sunset. You hear the door close behind you, locking you out...")
    Storyprint("You start to regret your choice as you hear the screechs of the monsters echo through the forest...")
    Storyprint("You think to yourself- (What the hell am I doing?!?) Your hands begin to shake...")
    Spacer()
    ENTER()
    ENTER()
    Spacer()
    Diaprint("Should I just end myself...? By my own hands instead getting ripped apart in agony?")
    print("\n1 - Yes, I should just end myself\n"
          "2 - No, that's stupid.")
    ask2 = int(input())
    if ask2 == 1:
        Storyprint("YOU COMMIT SUICIDE... YOU DIE")
        ENTER()
        Spacer()
        Gameover_screen()
    Storyprint("You suck it up and tighten your hand(s) around your " + Player_Weapon.name + ".")
    Spacer()
    ENTER()
    ENTER()
    Spacer()
    Storyprint("After a half hour of walking, you are deep inside a forest.")
    Storyprint("You wander into the woods as the sun begins to set....")
    Storyprint("Growls begin to form around you, you know you are going to have to fight...")
    Storyprint("And learn how to fight very quickly!")
    Enemycount = 3
    help_menu_print()
    fighting_intiate()#grammer check down VVV
    Storyprint("You fall down to the ground and the sun is setting, the only safe place to sleep is up in a tree...")
    Storyprint("You think to yourself... (what are you thinking of right now?)")
    thought_1 = input("")
    if thought_1 == "":
        thought_1 = "Nothing"
    Storyprint('"' + thought_1 + '... just ' + thought_1 + '..."')
    Storyprint("But besides that thought... you know there is no turning back now.")
    Storyprint("*YOU FALL ASLEEP KNOWING IT'S YOUR CALLING TO END ALL OF THIS*")
    ENTER()


######################CH.1###########################
Prolouge_title()
Prolouge_scene()
ENTER()

######################CH.1###########################

def Chapter2_title():
    Spacer()
    print("........#######....#....#.............#######.....")
    time.sleep(0.25)
    print("........#.....#....#....#..................##.....")
    time.sleep(0.25)
    print("........#..........######.............#######.....")
    time.sleep(0.25)
    print("........#.... #    #....#.......##....##..........")
    time.sleep(0.25)
    print("........#######....#....#.......##....#######.....")
    time.sleep(0.25)
    print("==================================================")
    print("=========CHAPTER 2 - SCAVENGING ENCOUNTERS========")
    print("==================================================")
    time.sleep(0.5)
    Spacer()
    ENTER()

def Chapter2_neighborfight():
    global Enemycount
    global Potions_num
    loot_times = 3
    while loot_times > 0:
        Enemycount = 3
        fighting_intiate()
        if loot_times == 3:
            Storyprint("You cleared the area to search two houses, you were able to snag some food, but not enough...")
            Storyprint("However you did find some nicer clothing so you aren't just wearing rags...")
            Storyprint("You only found one thing, but there may be more if you search more, but you need to fight again...\n\n")
            print("LOOT:\n"
                  "1x HP - POTION")
            Potions_num = Potions_num + 1
        elif loot_times == 2:
            Storyprint("You search the next two houses for more goodies and you aren't too disappointed.")
            Storyprint("Enough food to satisfy your hunger, nicer cloathing, and more goodies!\n\n")
            print("LOOT:\n"
                  "2x HP - POTIONS")
            Potions_num = Potions_num + 2
        else:
            Storyprint("The last house you search had some extra food for you to keep and something special...")
            Storyprint("A new weapon!\n\n")
            Spacer()
            print("NEW WEAPON: Copper Long-sword [1d8]")
            print("OLD WEAPON: " + Player_Weapon.name + "\n")
            print("Would you like to swap weapons?\n\n"
                  "1 - YES\n"
                  "2 - NO")
            ask2 = input("")
            if ask2 == "1":
                Player_Weapon.name = "Copper Long-sword [1d8]"
                Weapon_min_value = 1
                Weapon_max_value = 8
                Weapon_s_value = 0
                Player_Weapon_create.weapon_dmg_set(Player_Weapon, Weapon_min_value, Weapon_max_value, Weapon_s_value)
            else:
                Spacer()
                print("\nYou keep your " + Player_Weapon.name)
        ENTER()
        ENTER()
        if loot_times > 1:
            Spacer()
            print("///WANT TO LEAVE OR CONTINUE TO FIGHT AND LOOT?///\n\n"
              "1 - LEAVE W/ WHAT YOU HAVE\n"
              "2 - FIGHT & LOOT AGAIN")
            ask = input("")
            if ask == "1":
                loot_times = 0
            else:
                loot_times = loot_times - 1
        else:
            print("No more houses to loot...")
            loot_times = loot_times - 1

def Chapter2skelly():
    global Enemyhp
    global Enemystr
    global Enemydex
    global Enemyxp
    global EnemyLv
    global Enemy_name
    global Enemy_notes
    global Boss_enemy
    Chapter_Boss.name = "!!!ＴＨΞ░ＴＲΛＳＨ░ＳＫΞＬＬＹ!!!"
    Boss_create.assign_stats(Chapter_Boss, 8, 8, 60, Player_level - 1)
    Boss_create.assign_notes(Chapter_Boss, "\n- Nothing too special, heavy armor and weak attacks, still watch out though\n"
                             "- This skeleton smells like shit... ")
    Enemy_name = Chapter_Boss.name
    Enemyhp = Chapter_Boss.hp
    Enemystr = Chapter_Boss.str
    Enemydex = Chapter_Boss.dex
    EnemyLv = Chapter_Boss.lv
    Enemy_notes = Chapter_Boss.notes
    Enemyxp = 500 + EnemyLv * 100
    Boss_enemy = True
    Boss_fighting_intiate()
    Boss_enemy = False


def Chapter2_scene():
    global Enemycount
    global Player_health
    Player_health = Player_HP
    Storyprint("CHAPTER 2...")
    Storyprint("You are far gone from the bunker and out of the forest, although it's been 2 days. You are hungry, tired, and just")
    Storyprint("want a shower... both for cleaning and drinking. You stumble across a small neighbor hood with at least some houses")
    Storyprint("still intact... for the most part atleast. You know it's either you have to go in there knowing of the thought of ")
    Storyprint("the possiblity of finding some food. You do see some enemies in sight, but you'll fight if you have to. You know ")
    Storyprint("the basics of fighting with your " + Player_Weapon.name + ", just attack and avoid any lethals.")
    ENTER()
    ENTER()
    Storyprint("*YOU CHARGE INTO THE STREETS TO FIGHT*")
    Chapter2_neighborfight()
    Storyprint("\nYou walk out the house and in front of you, you don't see anymore monsters except for one...")
    Storyprint("A giant 7ft skeleton holding a bunch of debri and trash with a giant wooden pillar for a weapon...")
    Storyprint("You just yell at it...")
    yell1 = input(str(Player_Name) + ":")
    Diaprint("|" + Player_Name + ": " + yell1 + "!\n")
    Storyprint("The skeleton pauses...")
    time.sleep(0.2)
    Diaprint("|???: ...\n")
    time.sleep(0.2)
    Diaprint("|???: ...\n")
    time.sleep(0.2)
    Diaprint("|???: ...\n")
    Storyprint("It screeches at you ready to battle, it seems very angry at what you said.")
    ENTER()
    ENTER()
    Spacer()
    Diaprint("!!!ＴＨΞ░ＴＲΛＳＨ░ＳＫΞＬＬＹ!!!\n")
    time.sleep(0.5)
    Chapter2skelly()
    Storyprint("You defected the giant creature, he didn't have much to work with besides a small backpack you've found...")
    Storyprint("You loot the only intact backpack...")
    print("LOOT:\n"
          "Throwing Knife (10 - 20 dmg)\n")
    Item_adding.name = "Throwing Knife (10 - 20 dmg)"
    Item_adding.assign_stats(random.randint(10,20), "D")
    add_item()
    Storyprint("After Defeating the gross ass skeleton... it quietly whispers a few words...")
    Diaprint("|The Trash Skelly: You killed me...\n")
    Diaprint("|The Trash Skelly: They will take over...\n")
    Diaprint("|The Trash Skelly: This is war...\n")
    Diaprint("|The Trash Skelly: ...\n")
    Storyprint("You weren't sure what this means or what's going on...")
    Storyprint("You just want to get the hell out of this neighborhood...")
    Diaprint("|" + Player_Name + ": Next stop, city of Krimiy!\n")
    Storyprint("*You sprint your ass out of that town*")

######################CH.2###########################
Chapter2_title()
Chapter2_scene()
ENTER()

######################CH.2###########################

def Chapter3_title():
    Spacer()
    print("........#######....#....#.............#######.....")
    time.sleep(0.25)
    print("........#.....#....#....#..................##.....")
    time.sleep(0.25)
    print("........#..........######.............#######.....")
    time.sleep(0.25)
    print("........#.... #    #....#.......##.........##.....")
    time.sleep(0.25)
    print("........#######....#....#.......##....#######.....")
    time.sleep(0.25)
    print("==================================================")
    print("=======CHAPTER 3 - A KIDNAPPER OR A MURDERER======")
    print("==================================================")
    time.sleep(0.5)
    Spacer()
    ENTER()

def Chapter3_location():
    global Enemycount
    local_enemy_count = 0
    local_name = "empty"
    print("\n1 - Half of Skyscraper (HARD)\n"
          "2 - Underground Subway Station (NORMAL)\n"
          "3 - Local Streets & Restaraunts (EASY)\n")
    ask = input("")
    if ask == "1":
        Storyprint("You decided to risk it by going into the half torn-down office building")
        local_enemy_count = 10
        local_name = "Skyscraper"
    elif ask == "2":
        Storyprint("You decided to travel down to the abandoned subway")
        local_enemy_count = 8
        local_name = "Subway Station"
    elif ask == "3":
        Storyprint("You keep it somewhat safe and stay on ground level to loot")
        local_name = "Streets & Restaurants"
        local_enemy_count = 4
    else:
        print("\n///Please choose 1,2, or 3///\n")
        ENTER()
        Chapter3_location()
    Storyprint("\nYou head to the " + local_name + " and when you arrive you see a small mob of creatures you are going to have to fight...")
    Enemycount = local_enemy_count
    number_p = local_enemy_count
    fighting_intiate()

    global Potions_num

    global Quick_atk  # 75% dmg
    global Normal_atk   # 50% dmg
    global Heavy_atk   # 20%
    Storyprint("You have cleared the area to make it safe enough to loot")
    Storyprint("You found...")
    print("\nLoot: \n")
    print("" + str(round(number_p/2)) + "x HP - POTIONS\n")
    print("1x Book - Fighting Basics 101")
    print("1x Rusty Throwing Axe (" + str(round(number_p)) + " dmg)\n")
    Item_adding.name = "Rusty Throwing Axe (" + str(round(number_p)) + " dmg)"
    Item_adding.assign_stats(number_p, "D")
    add_item()
    ENTER()
    print("You read through the Book and you are understanding the basics of swinging a weapon around.")
    print("///YOU LEARN HOW TO ATTACK BETTER///")
    qx = Quick_atk
    Nx = Normal_atk
    Hx = Heavy_atk
    #book = +10% attack
    Quick_atk = Quick_atk + .10
    Normal_atk = Normal_atk + .10
    Heavy_atk = Heavy_atk + .10

    print("\nQUICK ATTACK CHANCE: " + str(qx * 100) + "% ---> " + str(Quick_atk * 100) + "%")
    print("\nNORMAL ATTACK CHANCE: " + str(Nx * 100) + "% ---> " + str(Normal_atk * 100) + "%")
    print("\nHEAVY ATTACK CHANCE: " + str(Hx * 100) + "% ---> " + str(Heavy_atk * 100) + "%")
    ENTER()

def Chapter3gang():
    global Enemyhp
    global Enemystr
    global Enemydex
    global Enemyxp
    global EnemyLv
    global Enemy_name
    global Enemy_notes
    global Boss_enemy
    Chapter_Boss.name = "T̶H̶E̶ T̶H̶R̶E̶E̶ U̶N̶K̶N̶O̶W̶N̶ B̶A̶N̶D̶I̶T̶S̶"
    Boss_create.assign_stats(Chapter_Boss, 15, 15, 90, Player_level - 1)
    Boss_create.assign_notes(Chapter_Boss, "\n- The three of them are expereice survivors\n"
                                           "- the thrid guy was more of an asshole\n"
                                           "- they all attack at the same time\n")
    Enemy_name = Chapter_Boss.name
    Enemyhp = Chapter_Boss.hp
    Enemystr = Chapter_Boss.str
    Enemydex = Chapter_Boss.dex
    EnemyLv = Chapter_Boss.lv
    Enemy_notes = Chapter_Boss.notes
    Enemyxp = 500 + EnemyLv * 100
    Boss_enemy = True
    Boss_fighting_intiate()
    Boss_enemy = False

def Chapter3_scene():
    global Enemycount
    global Player_health
    global Potions_num
    Player_health = Player_HP
    Storyprint("You were tired of wasting your time on looting the near by neighborhoods...")
    Storyprint("9 times out of 10 there is almost near to nothing left in any houses, let alone the house itself...")
    Storyprint("So you decided to head towards the city. You have enough experence fighting to atleast handle the daily\n"
               "creatures... as long as it's not another giant trash skeleton... oh god please no...")
    Storyprint("You only have anough sunlight to fight your way through one location, but not sure which path to take...")
    print("///Which location or building would you like to search and loot through???///")
    Chapter3_location()
    ENTER()
    Storyprint("After you cleaned the place dry and head on your own seperate ways...")
    Storyprint("You see a gang of 3 other armored people, you aren't sure if they are friendly or not...")
    Storyprint("They seem like they could be Bandits, they are all wearing the same colors... like a clan")
    Diaprint("|Unknown Guy-1: Well that was some fancy ass fighting in there now wasn't it?\n")
    Diaprint("|Unknown Guy-2: I must say, I thought we were going to have to be on clean up duty, but you pulled through.\n")
    Diaprint("|Unknown Guy-3: Yeah, yeah... that piss for brains can bash whatever he wants, I'm not impressed...\n")
    ENTER()
    ENTER()
    Storyprint("The two guys seem to have a friendly tone to themsevles, but the third in the back seem to have a additude with you.")
    Diaprint("|Unknown Guy-1: We are part of the HWD clan, we try our best to bring people in but only those who can be a asset to our \n"
             "guild. We on't just take in anyone unless they can either fight, loot, cook, or be trained to do one of those things. We \n"
             "saw what you did in there and want you to come with us.\n")
    print("What is your response?\n"
          "1 - Go with them\n"
          "2 - Don't go\n")
    ask_G = input("")
    if ask_G == "2":
        Diaprint("|" + Player_Name + ": Yeah thanks for the offer, but I think I'll keep to myself on my path...\n")
        Diaprint("|Unknown Guy-1: It wasn't an offer, it was a demand...\n")
        Diaprint("|Unknown Guy-2: Last chance to come with us before this turns ugly...\n")
        print("What is your response?\n"
              "1 - Go with them\n"
              "2 - fight them\n")
        ask_GG = input("")
        if ask_GG == "2":
            Diaprint("|" + Player_Name + ": Show me what you got!\n")
            Storyprint("THE THREE OF THEM BEGIN TO CREATE A FIGHTING FORMATION")
            ENTER()
            Chapter3gang()
            Storyprint("You defected the three bandits and find some intresting loot on them...")
            Storyprint("You loot the three of them...")
            print("LOOT:\n"
                  "5x HP Potions\n"
                  "1x Full Healing Potion\n"
                  "1x Homemade Bomb (20 dmg)"
                  "1x NEW WEAPON")
            Item_adding.name = "Homemade Bomb (20 dmg)"
            Item_adding.assign_stats(20, "D")
            add_item()
            Item_adding.name = "Full Healing Potion "
            Item_adding.assign_stats(Player_HP, "H")
            add_item()
            Potions_num = Potions_num + 5
            ENTER()
            ENTER()
            print("NEW WEAPON: Dual Black Daggers [2d12 + 2]")
            print("OLD WEAPON: " + Player_Weapon.name + "\n")
            print("Would you like to swap weapons?\n\n"
                  "1 - YES\n"
                  "2 - NO")
            askWW = input("")
            if askWW == "1":
                Player_Weapon.name = "Dual Black Daggers [2d12 + 2]"
                Weapon_min_value = 6
                Weapon_max_value = 12
                Weapon_s_value = 2
                Player_Weapon_create.weapon_dmg_set(Player_Weapon, Weapon_min_value, Weapon_max_value, Weapon_s_value)
            else:
                Spacer()
                print("\nYou keep your " + Player_Weapon.name)
            ENTER()
            Storyprint("You also find a map and compass that will lead you to this so called 'guild', so why not head over there too?...")
            Storyprint("You follow the map out of the city and towards your next destination")
        else:
            Diaprint("|" + Player_Name + ": Alright fine... lead the way...\n")
            Storyprint("You are lead out of the city and towards your next destination...")
    else:
        Diaprint("|" + Player_Name + ": Ok, Sounds intresting, show me the way...\n")
        Storyprint("You are lead out of the city and towards your next destination...")



######################CH.3###########################
Chapter3_title()
Chapter3_scene()
ENTER()

######################CH.3###########################

print("TO BE CONTINUED...")
def Highscore_screen():
    print("=============================================================================================")
    print("===== " + Player_Name + "  -  SCORE: " + str(SCORE) + " =====")
    print("=============================================================================================\n")
    quit()

Highscore_screen()
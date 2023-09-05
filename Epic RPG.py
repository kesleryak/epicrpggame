#imports
import random

#input variable
home = input("Type s to start.")

#hunt varibles
gainedWolfSkin = 0
gainedZombieEye = 0
gainedUnicornHorn = 0
gainedMermaidHair = 0
gainedRobotChip = 0
mobHealth = 0
maxMobHealth = 0

#profile variables
health = 100
maxHealth = 100
noCoins = 0
coins = 100
noExp = 0
exp = 0
maxExp = 100
level = 1
sword = ""
attack = 1
armor = ""
defence = 1
area = 1

#inv variables
lifePotion = 0
wolfSkin = 0
zombieEye = 0
unicornHorn = 0
mermaidHair = 0
robotChip = 0
wood = 0
fish = 0
apple = 0
potato = 0
carrot = 0
bread = 0
seed = 0

#chop/fish/pickup/drill variables
noWood = 0
noFish = 0
noApple = 0

#farm variables
plantExp = 0
plant = 0

#recipes/craft variables
attackAdder = 0
defenceAdder = 0

#boss variables
randChance = 0
dungeonKey = False
bossHealth = 100
maxBossHealth = 200
bossDamage = 50
maxBossDamage = 50
areaAdder = 0
gainedCoins = 500
coinMultiplier = 1

#training variables
trainingExp = 0
training = 0

#casino variables
coinflip = 0

#start of code
while True:

    #start command
    if home == "s":
        print("Welcome to Epic RPG! Type h to hunt for monsters, p to see profile and inv to see inventory. To buy things from the shop, Type shop. If you want to know more, Type help")

    #help command
    elif home == "help":
        print("Statistics Commands:")
        print("profile (p), inventory (inv), professions (pf), quest (q), horse (h)")
        print("Fighting Commands:")
        print("hunt (h), dungeon")
        print("Economy Commands:")
        print("shop, lootbox, open, buy, sell, use, trade")
        print("Working Commands:")
        print("chop, fish, craft, recipes")
        print("Gambling Commands:")
        print("coinflip")

    #hunt command
    elif home == "h":
        if exp >= maxExp:
            exp -= maxExp
            maxExp += 100
            level += 1
            maxHealth += 5
            attack = level + attackAdder
            defence = level + defenceAdder
        noCoins = random.randint(10 + areaAdder, 20 + areaAdder)
        noExp = random.randint(10 + areaAdder, 20 + areaAdder)
        mobHealth = random.randint(20 + areaAdder, 30 + areaAdder)
        maxMobHealth = mobHealth
        if mobHealth - (attack + defence) <= 0:
            mobHealth = attack + defence
        if area <= 2:
            print("You killed a wolf and gained", noCoins, "coins,", noExp, "Exp but lost", mobHealth - (attack + defence), "health.")
            gainedWolfSkin = random.randint(1,50)
        elif area <= 4:
            print("You killed a zombie and gained", noCoins, "coins,", noExp, "Exp but lost", mobHealth - (attack + defence), "health.")
            gainedZombieEye = random.randint(1,50)
        elif area <= 6:
            print("You killed a unicorn and gained", noCoins, "coins,", noExp, "Exp but lost", mobHealth - (attack + defence), "health.")
            gainedUnicornHorn = random.randint(1,50)
        elif area <= 8:
            print("You killed a mermaid and gained", noCoins, "coins,", noExp, "Exp but lost", mobHealth - (attack + defence), "health.")
            gainedMermaidHair = random.randint(1,50)
        elif area <= 10:
            print("You killed a robot and gained", noCoins, "coins,", noExp, "Exp but lost", mobHealth - (attack + defence), "health.")
            gainedRobotChip = random.randint(1,50)
        coins += noCoins
        exp += noExp
        health -= (mobHealth - (attack + defence))
        if gainedWolfSkin == 1:
            print("You got a wolf skin.")
            wolfSkin += 1
        elif gainedZombieEye == 1:
            print("You got a zombie eye.")
            zombieEye += 1
        elif gainedUnicornHorn == 1:
            print("You got a unicorn horn.")
            unicornHorn += 1
        elif gainedMermaidHair == 1:
            print("You got a mermaid hair.")
            mermaidHair += 1
        elif gainedRobotChip == 1:
            print("You got a robot chip.")
            robotChip += 1
        if health <= 0:
            print("You died. You lost one level.")
            if level > 1:
                level -= 1
                maxHealth -= 5
                health = maxHealth
                maxExp -= 100
                exp = 0
        mobHealth = maxMobHealth
                
    #profile command
    elif home == "p":
        if exp >= maxExp:
            exp -= maxExp
            maxExp += 100
            level += 1
            maxHealth += 5
            attack = level + attackAdder
            defence = level + defenceAdder
        print("Profile:")
        print("Area:", area)
        print("Level:", level)
        print("Health:", str(health) + "/" + str(maxHealth))
        print("Coins:", coins)
        print("Experience:", str(exp) + "/" + str(maxExp))
        print("Sword:", sword)
        print("Armor:", armor)
        print("Atk:", attack)
        print("Def:", defence)

    #inventory command
    elif home == "inv":
        print("Inventory:")
        print("Wolf Skin:", wolfSkin)
        print("Zombie Eye:", zombieEye)
        print("Unicron Horn:", unicornHorn)
        print("Mermaid Hair:", mermaidHair)
        print("Robot Chip:", robotChip)
        print("Life Potion:", lifePotion)
        print("Wood:", wood)
        print("Fish:", fish)
        print("Apple:", apple)
        print("Seed:", seed)
        print("Potato:", potato)
        print("Carrot:", carrot)
        print("Bread:", bread)
        
    #shop command
    elif home == "shop":
        print("Welcome to the shop! what would you like to buy?")
        print("1: Life Potion (can heal to max health) 25 coins.")
        print("2: Dungeon Key (will be able to access the dungeon.) 100 coins.")
        print("3: Seed (will be able to grow into something useful) 40 coins")
        home = input("What would you like to buy? Type the number")
        if home == "1":
            if coins >= 25:
                print("You bought a life potion.")
                lifePotion += 1
                coins -= 25
            else:
                print("You don't have enough money to buy this.")
        elif home == "2":
            if coins >= 100 and dungeonKey == False:
                print("You bought a dungeon key.")
                dungeonKey = True
                coins -= 100
            else:
                print("You don't have enough money to buy this.")
        elif home == "3":
            if coins >= 40:
                print("You bought a seed.")
                seed += 1
                coins -= 40
            else:
                print("You don't have enough money to buy this.")
        else:
            print("Unrecognised number.")

    #use command
    elif home == "use potion":
        if lifePotion >= 1:
            print("You used a life potion.")
            lifePotion -= 1
            health = maxHealth
        else:
            print("You don't have enough life potions.")

    #chop command
    elif home == "chop":
        noWood = random.randint(1,3)
        print("You chopped a tree and gained", noWood, "wood.")
        wood += noWood
         
    #axe command
    elif home == "axe":
        if area >= 3:
            noWood = random.randint(4,9)
            print("You chopped a tree and gained", noWood, "wood.")
            wood += noWood
        else:
            print("You are not in area 3+ yet. Go and fight the boss first.")

    #bowsaw command
    elif home == "bowsaw":
        if area >= 6:
            noWood = random.randint(10,27)
            print("You chopped a tree and gained", noWood, "wood.")
            wood += noWood
        else:
            print("You are not in area 6+ yet. Go and fight the boss first.")

    #chainsaw command
    elif home == "chainsaw":
        if area >= 9:
            noWood = random.randint(28,81)
            print("You chopped a tree and gained", noWood, "wood.")
            wood += noWood
        else:
            print("You are not in area 9+ yet. Go and fight the boss first.")

    #fish command
    elif home == "fish":
        noFish = random.randint(1,3)
        print("You fished in a boat and you gained", noFish, "fish.")
        fish += noFish
        
    #net command
    elif home == "net":
        if area >= 3:
            noFish = random.randint(4,9)
            print("You fished in a boat and you gained", noFish, "fish.")
            fish += noFish
        else:
            print("You are not in area 3+ yet. Go and fight the boss first.")

    #boat command
    elif home == "boat":
        if area >= 6:
            noFish = random.randint(10,27)
            print("You fished in a boat and you gained", noFish, "fish.")
            fish += noFish
        else:
            print("You are not in area 6+ yet. Go and fight the boss first.")

    #bigboat command
    elif home == "bigboat":
        if area >= 9:
            noFish = random.randint(28,81)
            print("You fished in a boat and you gained", noFish, "fish.")
            fish += noFish
        else:
            print("You are not in area 9+ yet. Go and fight the boss first.")

    #pickup command
    elif home == "pickup":
        if area >= 3:
            noApple = random.randint(1,3)
            print("You picked up fruits and you gained", noApple, "apples.")
            apple += noApple
        else:
            print("You are not in area 3+ yet. Go and fight the boss first.")
            
    #ladder command
    elif home == "ladder":
        if area >= 4:
            noApple = random.randint(4,9)
            print("You picked up fruits and you gained", noApple, "apples.")
            apple += noApple
        else:
            print("You are not in area 4+ yet. Go and fight the boss first.")

    #tractor command
    elif home == "tractor":
        if area >= 8:
            noApple = random.randint(10,27)
            print("You picked up fruits and you gained", noApple, "apples.")
            apple += noApple
        else:
            print("You are not in area 8+ yet. Go and fight the boss first.")

    #greenhouse command
    elif home == "tractor":
        if area >= 11:
            noApple = random.randint(28,81)
            print("You picked up fruits and you gained", noApple, "apples.")
            apple += noApple
        else:
            print("You are not in area 11+ yet. Go and fight the boss first.")

            
    #recipe command
    elif home == "recipes":
        print("Recipes:\n")
        print("Level 1:")
        print("Wooden Sword: 40 wood (4 atk).")
        print("Fish Armor: 20 fish and 10 wood (9 def).\n")
        print("Level 2:")
        print("Fish Sword: 125 wood and 100 fish (13 atk).")
        print("Wolf Armor: 170 wood and 2 wolf skin (20 def).\n")
        print("Level 4:")
        print("Apple Sword: 65 apple and 290 wood (32 atk).")
        print("Eye Armor: 1 zombie eye and 930 wood (26 def).\n")
        print("Level 6:")
        print("Zombie Sword: 980 wood, 50 apples and 1 zombie eye (43 atk).")
        print("Banana Armor: 300 apples and 1000 wood (36 def).\n")
        print("To craft, type craft.")

    #craft command
    elif home == "craft":
        home = input("What do you want to craft?")
        if home == "wooden sword":
            if level >= 1:
                if wood >= 40:
                    print("You crafted a wooden sword.")
                    wood -= 40
                    sword = "Wooden Sword"
                    attack = level + 4
                    attackAdder = 4
                else:
                    print("You do not have enough materials to craft this.")
                
        elif home == "fish armor":
            if level >= 1:
                if fish >= 20 and wood >= 10:
                    print("You crafted a fish armor.")
                    fish -= 20
                    wood -= 10
                    armor = "Fish Armor"
                    defence = level + 9
                    defenceAdder = 9
                else:
                    print("You do not have enough materials to craft this.")

        elif home == "fish sword":
            if level >= 2:
                if fish >= 100 and wood >= 125:
                    print("You crafted a fish sword.")
                    fish -= 125
                    wood -= 100
                    sword = "Fish Sword"
                    attack = level + 13
                    attackAdder = 13
                else:
                    print("You do not have enough materials to craft this.")
                    
        elif home == "wolf armor":
            if level >= 2:
                if wolfSkin >= 2 and wood >= 170:
                    print("You crafted a wolf armor.")
                    wolfSkin -= 2
                    wood -= 170
                    armor = "Wolf Armor"
                    defence = level + 20
                    defenceAdder = 20
                else:
                    print("You do not have enough materials to craft this.")

        elif home == "apple sword":
            if level >= 4:
                if apple >= 65 and wood >= 290:
                    print("You crafted a apple sword.")
                    apple -= 65
                    wood -= 290
                    sword = "Apple Sword"
                    attack = level + 32
                    attackAdder = 32
                else:
                    print("You do not have enough materials to craft this.")

        elif home == "eye armor":
            if level >= 4:
                if zombieEye >= 1 and wood >= 930:
                    print("You crafted an eye armor.")
                    zombieEye -= 1
                    wood -= 930
                    armor = "Eye Armor"
                    defence = level + 26
                    defenceAdder = 26
                else:
                    print("You do not have enough materials to craft this.")
                    
        else:
            print("Unrecognised equipment.")

    #dungeon command
    elif home == "dungeon":
        if dungeonKey == True:
            while bossHealth > 0 and health > 0:
                print("Boss:", bossHealth)
                print("You:", health)
                print("Punch: Does 100% damage all the time.")
                print("Kick: Does 120% damage 60% of the time.")
                print("Power: Does 400% damage 40% of the time.")
                home = input("What would you do?")
                if home == "punch":
                    bossHealth -= attack + defence
                    if bossDamage - (attack + defence) <= 0:
                        bossDamage = attack + defence
                    print("You punched it and he lost", attack + defence, "health.")
                    print("It attacked you and you lost", bossDamage - (attack + defence), "health.")
                    health -= bossDamage - (attack + defence)
                    bossDamage = maxBossDamage
                if home == "kick":
                    randChance = random.randint(1,10)
                    if randChance <= 6:
                        bossHealth -= (attack + defence)*1.2//1
                        print("You kicked it and he lost", (attack + defence)*1.2//1, "health.")
                    if bossDamage - (attack + defence) <= 0:
                        bossDamage = attack + defence
                    print("It attacked you and you lost", bossDamage - (attack + defence), "health.")
                    health -= bossDamage - (attack + defence)
                    bossDamage = maxBossDamage
                if home == "power":
                    randChance = random.randint(1,10)
                    if randChance <= 4:
                        bossHealth -= (attack + defence)*4//1
                        print("You powered up and he lost", (attack + defence)*4//1, "health.")
                    if bossHealth > 0:
                        if bossDamage - (attack + defence) <= 0:
                            bossDamage = attack + defence
                        print("It attacked you and you lost", bossDamage - (attack + defence), "health.")
                        health -= bossDamage - (attack + defence)
                        bossDamage = maxBossDamage
            if health <= 0:
                print("You died. You lost one level.")
                if level >= 1:
                    level -= 1
                    maxHealth -= 5
                    health = maxHealth
                    maxExp -= 100
                    exp = 0
            else:
                gainedCoins *= coinMultiplier
                print("You gained", int(gainedCoins), "coins")
                coinMultiplier += 0.5
                coins += int(gainedCoins)
                dungeonKey = False
                area += 1
                areaAdder += 10
                maxBossDamage *= 2
                bossDamage = maxBossDamage
                bossHealth = maxBossHealth
                maxBossHealth *= 2
        else:
            print("Go buy a dungeon key.")

    #farm command
    elif home == "farm":
        if area >= 4:
            if seed >= 1:
                plant = random.randint(1,3)
                plantExp = random.randint(25,50)
                if plant == 1:
                    print("You got a potato and", plantExp, "XP.")
                    potato += 1
                elif plant == 2:
                    print("You got a carrot and", plantExp, "XP.")
                    carrot += 1
                elif plant == 3:
                    print("You got bread and", plantExp, "XP.")
                    bread += 1
                exp += plantExp
                seed -= 1
            else:
                print("Go buy a seed first.")
        else:
            print("You are not in area 4+ yet. Go and fight the boss first.")
            
    #training command
    elif home == "training":
        if area >= 2:
            training = random.randint(1,3)
            if training == 1:
                home = input("What is the 5th letter of apple?")
                if home == "e":
                    trainingExp = random.randint(100,200)
                    print("Correct! You gained", trainingXp, "Exp.")
                    exp += trainingExp
            elif training == 2:
                home = input("What is the 3th letter of banana?")
                if home == "n":
                    trainingExp = random.randint(100,200)
                    print("Correct! You gained", trainingXp, "Exp.")
                    exp += trainingExp
            elif training == 3:
                home = input("What is the 4th letter of apple?")
                if home == "l":
                    trainingExp = random.randint(100,200)
                    print("Correct! You gained", trainingXp, "Exp.")
                    exp += trainingExp
        else:
            print("You are not in area 2+ yet. Go and fight the boss first.")

    #sell command
    elif "sell" in home:
        if "wolf skin" in home:
            if wolfSkin >= 1:
                coins += 500
                wolfSkin -= 1
                print("You sold a wolf skin for 500 coins.")

        elif "zombie eye" in home:
            if zombieEye >= 1:
                coins += 2000
                zombieEye -= 1
                print("You sold a zombie eye for 2000 coins.")
        
        elif "sell" in home:
            print("Type in what you want to sell together with the command.")

    #casino command
    elif home == "coinflip":
        if coins > 0:
            home = input("How much do you want to bet?")
            if int(home) > 0:
                if coins >= int(home):
                    coinflip = random.randint(1,101)
                    if coinflip <= 50:
                        print("It landed on heads. You won", int(home), "coins.")
                        coins += int(home)
                    elif coinflip <= 100:
                        print("It landed on tails. You lost", int(home), "coins.")
                        coins -= int(home)
                    elif coinflip == 101:
                        print("The coin landed on its side!!! You received", int(home)*5, "coins.")
                        coins += (int(home) * 5)
    
    #unrecognised command
    else:
        print("Invalid command.")

    #input command
    home = input("> ")

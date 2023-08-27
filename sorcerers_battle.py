import random

def battle_of_sorcerer(): #prendre en argument les deux dictionnaires de sorts
    #We explain the rules to the player : You need to kill Saruman the grey. For that you need to deal at least 101 of damage. Here are your spells:
    print("The rules")

    #Defining spells avalaible and showing 
    fireball = {
        "name" : "Fireball",
        "power" : 45,
        "position" : "1"
    }
    dark_soul = {
        "name" : "Dark soul",
        "power" : 40,
        "position" : "2"    }
    red_arrow = {
        "name" : "Red arrow",
        "power" : 15,
        "position" : "3"
    }
    black_tentacles = {
        "name" : "Black tentacles",
        "power" : 30,
        "position" : "4"
    }

    # creer deux dictonaire : un pour moi et un pour lui avec des sorts different
    #faire un sort de soin

    your_powers = [fireball, dark_soul, red_arrow, black_tentacles] #=list(dicitonaire.key)
    his_powers = [fireball, dark_soul, red_arrow, black_tentacles]

    print ("Here are your spells and their power")
    for power in your_powers:
        print (power["position"], power["name"], power["power"])

    total_damages_done = 0
    total_damages_received = 0
    target_damages = 100
    #faire une liste pour les dommages et la print a chaque tour

    while total_damages_done < target_damages and total_damages_received < target_damages:
            total_damages_done += my_turn(your_powers)
            print(f"You have dealt {total_damages_done} damages")
            if total_damages_done > target_damages:
                print ('You are the best')
            else:
                total_damages_received += opponent_turn(his_powers)
                print(f"He has dealt {total_damages_received} damages")
                if total_damages_received > target_damages:
                    print ('He is the best')

    if total_damages_done > 51:
        print('you win')

def my_turn(power):
    dammage_done = 0
    name_of_power = [p["position"] for p in power]
    spell_throw = input(f"It's your turn! What spell do you want to do ? {', '.join(n for n in name_of_power)} ?")
    fail = random.randint(1,5)
    print("fail = ", fail)
    if fail == 5:
        print ("Your spell might be correct, but you missed")
        return dammage_done
    else:
        for p in power:
            if spell_throw == p["position"]: #and fail != 5:
                dammage_done += p["power"]
                print("You've hit him! I didn't know you where this powerfull...")
                return dammage_done
        else:
            print("Your skills are too weak. You might become a greater sorcerer to use this spell. Try again at your next turn")
            return dammage_done
        
def opponent_turn(power):
    dammage_done = 0
    print("What the opponent is going to do? ")
    spell_throw = str(random.randint(1,5))
    name_of_power = [p["position"] for p in power]
    spell_throw = input(f"It's his turn! What spell do you want to do ? {', '.join(n for n in name_of_power)} ?")
    for p in power:
        if spell_throw == p["position"]:
            dammage_done += p["power"]
            print("He hits you! Be brave")
            return dammage_done


battle_of_sorcerer()
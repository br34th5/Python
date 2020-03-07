from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item
import random


# Black Magic
fire = Spell("Fire", 15, 400, "Black")
thunder = Spell("Thunder", 15, 400, "Black")
blizzard = Spell("Blizzard", 15, 400, "Black")
meteor = Spell("Meteor", 30, 800, "Black")
quake = Spell("Quake", 20, 600, "Black")

# White Magic
cure = Spell("Cure", 10, 500, "White")
cura = Spell("Cura", 20, 1000, "White")

# Create some Items
potion = Item("Potion", "potion", "Heals for 250 HP", 250)
hipotion = Item("Hi-Potion", "potion", "Heals for 500 HP", 500)
superpotion = Item("Super Potion", "potion", "Heals for 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully Restores HP/MP of a party member", 9999)
hielixer = Item("Mega Elixer", "elixer", "Fully restores HP/MP of all party members", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# Instantiate People
player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, cure]
player_items = [{"item": potion, "quantity": 3}, {"item": hipotion, "quantity": 3},
                {"item": superpotion, "quantity": 3}, {"item": elixer, "quantity": 1},
                {"item": hielixer, "quantity": 1}, {"item": grenade, "quantity": 1}]

player1 = Person("Valos  ", 3000, 100, 200, 30, player_spells, player_items)
player2 = Person("Einaras", 3100, 100, 200, 30, player_spells, player_items)
player3 = Person("Robot  ", 3200, 100, 200, 30, player_spells, player_items)

enemy1 = Person("Dog ", 1200, 130, 500, 200, enemy_spells, [])
enemy2 = Person("Lich", 12000, 400, 800, 25, enemy_spells, [])
enemy3 = Person("Elf ", 1200, 130, 800, 200, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("\n")
    
    print("NAME                  HP                                      MP")
    for player in players:
        player.get_stats()
    
    for enemy in enemies:
        enemy.get_enemy_stats()
    
    for player in players:
        player.choose_action()
        choice = input("    Choose action:")
        index = int(choice) - 1
        
        #if the choice is 1 then it will be a Attack
        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(bcolors.CYELLOW2 + player.name.replace(" ", "") + ' attacked ' + enemies[enemy].name.replace(" ", "") + " for:", dmg, "points of damage" + bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic:")) - 1
            
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            current_mp = player.get_mp()
            
            if spell.cost > current_mp:
                print(bcolors.FAIL + "Not Enough Mana Points!" + bcolors.ENDC)
                continue
            
            if magic_choice == -1:
                continue
            
            player.reduce_mp(spell.cost)
            
            if spell.type == "White":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "Black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name + bcolors.FAIL + bcolors.ENDC)
                
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item:  ")) - 1 
            
            if item_choice == -1:
                continue
            
            item = player.items[item_choice]["item"]
            
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL, "None left...", bcolors.ENDC)
                continue
            
            player.items[item_choice]["quantity"] -= 1
            
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP", bcolors.ENDC)
            elif item.name == "Mega Elixer": 
                for i in players:
                    i.hp = i.maxhp
                    i.mp = i.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " Fully restores HP/MP of all party members" + bcolors.ENDC)
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " Fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died")
                    del enemies[enemy]

        else: 
            print ("Press 1 for Attack, 2 for Magic, 3 for Items")
            continue
    
    #check if battle is over
    defeated_enemies = 0
    defeated_players = 0
    
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    #check if player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False

    #check if enemy won    
    elif defeated_players == 2:
        print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
        running = False
    
    #enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        
        if enemy_choice == 0:
            #chose attack
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()
            #chose target
            players[target].take_damage(enemy_dmg)
            print(bcolors.CYELLOW2 + enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for", enemy_dmg, "points of damage" + bcolors.ENDC)
        elif enemy_choice == 1:
            #chose magic
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)
            
            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals " + enemy.name + " for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                target = random.randrange(0, 2)
                players[target].take_damage(magic_dmg)
                
                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg), "magic damage to " + players[target].name.replace(" ", "") + bcolors.ENDC)
                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + "has died")
                    del players[player]
            #print("Enemy chose", spell, "damage is: ", magic_dmg)

        #vid 12:25-19;50
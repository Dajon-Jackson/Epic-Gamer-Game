from random import *
import sys
#Part 7 (Monsters)
monsta_rat = {'Name': "Rat", 'Strength': 1, 'Defense': 1, 'Magic': 0, 'Agility': 2}
monsta_angryRat = {'Name': "Angry Rat" , 'Strength': 2, 'Defense': 1, 'Magic': 0, 'Agility': 1}
monsta_magicRat = {'Name': "Magic Rat", 'Strength': 1, 'Defense': 1, 'Magic': 1, 'Agility': 1}
monsta_sadRat = {'Name': "Sad Rat", 'Strength': 0, 'Defense': 1, 'Magic': 0, 'Agility': 0}
monsta_fatRat = {'Name': "Fat Rat", 'Strength': 1, 'Defense': 2, 'Magic': 0, 'Agility': 1}
monsta_racingRat = {'Name': "Racing Rat", 'Strength': 1, 'Defense': 1, 'Magic': 0, 'Agility': 3}
monsta_angryMagicRacingRat = {'Name': "Angry Magic Racing Rat", 'Strength': 2, 'Defense': 1, 'Magic': 1, 'Agility': 3}

fishie_tuna = {'Name': "Tuna", 'Value': 8.10, 'HP Gain': 13}
fishie_cod = {'Name': "Cod",'Value': 7.50, 'HP Gain': 9}
fishie_boot = {'Name': "Boot",'Value': 20.00 ,'HP Gain': -1}
fishie_feelgood = {'Name':"Feel Good" ,'Value': 50,'HP Gain': 99999}

scaryMonstas = [monsta_rat, monsta_angryRat, monsta_magicRat, monsta_sadRat, monsta_fatRat, monsta_racingRat, monsta_angryMagicRacingRat]

fishies = [fishie_tuna, fishie_cod, fishie_boot, fishie_feelgood]
xp = 0
lvl_req = 150
cash = 0
lvl = 1
inventory = []
#Fishing (Python Project)
def fishing():
  fish_recieved = randint(0,100)
  if (fish_recieved > 95):
    #Add Feel Good
    inventory.append(fishie_feelgood)
    print("Feel Good GET")
  elif (fish_recieved <5):
    #Add Boot
    inventory.append(fishie_boot)
    print("You fished up a stinky boot")
  elif (fish_recieved >= 5) and (fish_recieved <= 55):
    #Add Cod
    inventory.append(fishie_cod)
    print("You managed to catch a cod")
  elif (fish_recieved >55) and (fish_recieved <= 95):
    #Add Tuna
    inventory.append(fishie_tuna)
    print("You managed to catch a tuna")
  print("~" * 99)
#Level Up (Python Project)
def levelup():
  global xp, lvl_req, lvl, player_strength, player_defense, player_magic, player_agility, player_class
  if xp >= lvl_req:
    print("LEVEL UP!!!")
    xp = 0
    lvl += 1
    lvl_req += (lvl_req * 1.5)

    if player_class in ['Brawler']:
      player.strength += 1
      player.defense += 2
      player.magic += 1
      player.agility += 2

    elif player_class in ['Swordfighter']:
      player.strength += 2
      player.defense += 1
      player.magic += 1
      player.agility += 1

    elif player_class in ['Mage']:
      player.strength += 1
      player.defense += 1
      player.magic += 2
      player.agility += 1
  else:
    print("|Level: {}|".format(lvl))
    print("|XP to next level {}|".format((lvl_req - xp)))

#Inventory(Python Project)
def inventory_check():
  print("Cash: ${0:.2f}".format(cash))
  for item in inventory:
    print("Name: {}\t\t\t\t\t\tValue: ${}\t\tHP Gain: {}".format(item['Name'], item['Value'], item['HP Gain']))
  print("~" * 99)
#Stats(Python Project)
def stat_check():
  print("Strength: {}\nMagic: {}\nDefense: {}\nAgility: {}".format(player.strength, player.magic, player.defense, player.agility))

#RoamTown (Python Project)
def townia_roam():
  levelup()
  print("It's a town, what do you wanna do?\n")
  print("1.Check Inventory\n2.Check Stats\n3.Go Fishing\n4.Go to the attic and do the quest\n5.Go to the store\n9.Leave the game")

  decision = int(input(": "))
  if decision == 1:
    print("~" * 99)
    inventory_check()
  elif decision == 2:
    print("~" * 99)
    stat_check()
  elif decision == 3:
    print("~"*99)
    fishing()
  elif decision == 4:
    print("~" * 99)
    quest1_6rats()
  elif decision == 5:
    print("~" * 99)
    townia_store()
  elif decision == 9:
    print("~" * 99)
    print("Game Over")
    sys.exit()
  else:
    print("***INVALID OPTION***")
#Store(Python Project)
times_visited = 0
def townia_store():
  global times_visited
  if times_visited == 0:
    print("You walk into the store and see an old man relaxing by his window. He's sitting in a chair, leaning it back with his legs on the window sill and his arms behind his head. But once he recognizes your presence, the smile is quickly removed from his face.\n 'What do YOU want' he says. You tell him how you came to visit the only shop available so that you can buy something cool like armor, weapons or at least food. 'We don't sell anything here you dunce. We only buy here, now give me what you're here to sell'")
    print("~"*99)
  else:
    print("The old man gets up from his chair to service you.")
    print("~"*99)
  times_visited += 1
  selling_townia = 1
  while selling_townia == 1:
    global cash
    inventory_check()
    print("Enter the name of an item you would like to sell. Enter 'None' to leave")
    selling = input(": ")
    if selling.lower() == "none":
      selling_townia = 0
    if selling.lower() == "tuna":
      inventory.remove(fishie_tuna)
      cash += fishie_tuna['Value']
    elif selling.lower() == "cod":
      inventory.remove(fishie_cod)
      cash += fishie_cod['Value']
    elif selling.lower() == "feel good":
      inventory.remove(fishie_feelgood)
      cash += fishie_feelgood['Value']
    elif selling.lower() == "boot":
      inventory.remove(fishie_boot)
      cash += fishie_boot['Value']

#Quest 1 (Redo-able) (Python Project)
def quest1_6rats():
  global rats_defeated
  global cash
  global xp
  global lvl_req
  quest1_complete = 0
  while (quest1_complete == 0) :
    print("1. Search current position\n2. Move around\n3. Pick a fight\n9. Exit game")
    choice = int(input(": "))
    print("~" * 99)
    if choice == 9:
      sys.exit()
    elif choice == 1:
      print("You search the empty attic but find nothing but rats staring at you waiting for you to choose choice 3.")
    elif choice == 2:
      print("You move aroung the empty attic but the attic is like an endless room... also the rats follow you...and they are also infinite.")
    elif choice == 3:
      print("You point at one of the rats and it honorably accepts your challenge.")
      currentlyFighting = scaryMonstas[randint(0, 6)]

      print("You are fighting ", currentlyFighting['Name'])
      fightScene(currentlyFighting)
      rats_defeated += 1
    else:
      print("***INVALID OPTION***")

    if rats_defeated >= 6:
      quest1_complete = 1
      cash += 100.00
      xp += 100.00
      print("You've succesfully defeated 6 rats. You head back to town and reap your reward of $100.00")
      rats_defeated = 0
    print("~" * 99)
#Part 9
class Entity:
  def __init__(self, name, strength, defense, magic, agility):
    self.name = name
    self.strength = strength
    self.defense = defense
    self.magic = magic
    self.agility = agility
    self.health = (self.defense * 3)
#Fight Scenes
def fightScene(enemy):
  global cash
  global xp
  flee = 0
  enemy_alive = 1
  current_enemy = Entity(enemy['Name'], enemy['Strength'], enemy['Defense'], enemy['Magic'], enemy['Agility'] )
  cash_gain = (current_enemy.strength + current_enemy.magic + current_enemy.agility + current_enemy.defense)/4
  xp_gain = cash_gain
  #Reminder: make rat posion
  #Option to poison the rat's cake
  while (enemy_alive == 1) and (flee == 0):
    pdmg = randint (0, player.strength)
    pmdmg = randint (0, player.magic)
    edmg = randint (0, current_enemy.strength)
    emdmg = randint (0, current_enemy.magic)
    pesc = randint (0, player.agility)
    eesc = randint (0, current_enemy.agility)

    print("1. Attack ")
    print("2. Magic Attack")
    print("3. Defend")
    print("4. Flee")
    choice = input(": ")
    print("")
    if choice == "1":
      print("You swing and hit the enemy and do {:1f}".format(pdmg))
      current_enemy.health -= pdmg

    elif choice == "2":
      print("You shoot magic stuff at your enemy and it does {:1f}".format(pmdmg))
      current_enemy.health -= pmdmg

    elif choice == "3":
      print("You put up your guard")
      pgrd = randint (0,100)
      if pgrd < 50:
        print("You failed to guard and will take full damage")
      elif pgrd > 50:
        print("You managed to block the attack and will only take half damage")
        edmg = edmg - (edmg * 0.5)
        emdmg = emdmg - (edmg * 0.5)
      elif pgrd == 50:
        print("PERFECT GUARD! No damage will be taken!")
        edmg = 0
        emdmg = 0

    elif choice == "4":
      if pesc > eesc:
        print("You managed to escape...but not with your dignity")
        flee = 1

      else:
        print("The enemy blocks your escape!")

    else:
      print("INVALID CHOICE: Choosing to attack")
      print("You swing and hit the enemy and do {:1f}".format(pdmg))
      current_enemy.health -= pdmg

    enemy_attack_choice = 0

    if current_enemy.magic > 0:
      enemy_attack_choice = randint (0,1)

    if enemy_attack_choice == 0:
      print("The enemy attacks you and does {:1f}".format(edmg))
      player.health -= edmg

    elif enemy_attack_choice == 1:
      player.health -= emdmg
      print("The enemy shoots some sparkles at you and does {:1f}".format(emdmg))

    print("~" * 99)


    if player.health <= 0:
      print("You died. It's a shame, really.")
      sys.exit()

    if current_enemy.health <= 0:
      print("Good fight. You won!")
      cash += cash_gain
      xp += xp_gain
      enemy_alive = 0
quest1 = 0
while (quest1 == 0):
  #Part 1
  print("~" * 99)
  print("Welcome to E.G.G.!")
  print("~" * 99)

  print("WARNING: spell your race perfectly (Spaces, caps, and all) or you default to Human. ")
  print("")
  print("Choose your race from Human, Dark Elf, Dwarf, or Wood Elf")
  race = input(": ")
  print("~" * 99)

  #Part 2
  if race in ['Human', 'Dark Elf', 'Dwarf', 'Wood Elf']:
    print("Good choice. You chose: "+race+"")
  elif race in ['Shaggydelic']:
    print("May [REDACTED] have mercy on our souls...")
  else:
    print("Invalid choice. You are now human")
    race = "Human"
  print("~" * 99)
  #Part 3
  print("warning: spell your class perfectly (Spaces, caps, and all) or you default to Brawler")
  print("")
  print("Choose your class from Brawler, Swordfighter, or Mage")
  player_class = input(": ")
  print("~" * 99)

  if player_class in ['Brawler', 'Swordfighter', 'Mage']:
    print("You chose: "+player_class+"")
  else:
    print("Invalid choice. You are now a brawler")
    player_class = "Brawler"
  print("~" * 99)
  #Part 4
  print("Now enter your name")
  name = input(": ")
  print("~" * 99)

  print("Name: "+name+"")
  print("Race: "+race+"")
  print("Class: "+player_class+"")

  print("~" * 99)

  #Part 5
  player_strength = 10
  player_defense = 10
  player_magic = 10
  player_agility = 10

  if race in ['Human']:
    player_strength += 5
    player_defense -= 2
    player_magic -= 3
    player_agility += 1

  elif race in ['Dark Elf']:
    player_strength -= 4
    player_defense -= 5
    player_magic += 8
    player_agility += 1

  elif race in ['Dwarf']:
    player_strength += 12
    player_defense += 5
    player_magic -= 7
    player_agility -= 7

  elif race in ['Wood Elf']:
    player_strength -= 3
    player_defense -= 5
    player_magic += 3
    player_agility += 5

  elif race in ['Shaggydelic']:
    player_strength += 69656
    player_defense += 69656
    player_magic += 69656
    player_agility += 69656

  else:
    print("wtf happened")
    sys.exit()

  player = Entity(name, player_strength, player_defense, player_magic, player_agility)

  #Part 6
  print("You enter a placeholder town that is clearly just there until the creator comes up with a better design.")
  print("")
  print("The first lifeless husk you meet in this town is a person simply named, 'Questgiver'.")
  print("")
  print("You walk up to them and they immediately turn to you and say 'Hello there! you clearly have nothing better to do and we're too lazy to do this ourselves!")
  print("")
  print("He hands you a scroll. You open the scroll and begin to skim over it. You then look up to ask why this needs to be done but Placeholer Questgiver is already gone.")
  print("")
  print("You look back to the scroll and it says 'There are some angry rats in my attic, come kill them.' (Kill 6 Rats) ")
  rats_defeated = 0
  print("~" * 99)

  while 1==1:
    townia_roam()

print("Game Over")

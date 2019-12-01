import random
import time

PlayerMaxHealth = 100
PlayerCurrentHealth = 100
PlayerAttack = 10
PlayerWind = 0
PlayerWater = 0
PlayerEarth = 0
PlayerFire = 0
PlayerLevel = 1
PlayerExperience = 0
PlayerGold = 0
PlayerApple = 0
PlayerPotion = 0
MapProgress = 0
PlayerName = None

def MonsterExamination(MapProgress):
	MonsterType, MonsterMultiplier, StrElement, MonsterElement, MonsterLevel, MonsterHealth, MonsterAttack = MonsterStats(MapProgress)
	print("You have enounctered a level " + str(MonsterLevel) + " " + str(StrElement) + " " + str(MonsterType))
	time.sleep(1)	
	print("It has " + str(MonsterHealth) + " health and " + str(MonsterAttack) + " attack")
	time.sleep(1)	
	return(MonsterElement, MonsterHealth, MonsterAttack, MonsterMultiplier)

def MonsterTypeFunction(MapProgress):
	MonsterIndex = random.uniform(0, MapProgress)
	if 4 - MapProgress <= MonsterIndex <= 3.2:
		Monster = "minotaur"
		MonsterMultiplier = 3
	elif 5 > MonsterIndex > 3.2:
		Monster = "dragon"
		MonsterMultiplier = 5
	else:
		Monster = "slime"
		MonsterMultiplier = 1
	return(Monster, MonsterMultiplier)

def MonsterElementFunction(MapProgress):
	if MapProgress == 0:
		MonsterElement = 0
	elif MapProgress == 1:
		MonsterElement = 1
	elif MapProgress == 2:
		MonsterElement = 2
	elif MapProgress == 3:
		MonsterElement = 3
	elif MapProgress == 4:
		MonsterElement = random.randint(0,3)
	elif MapProgress == 5:
		MonsterElement = random.randint(0,3)
	if MonsterElement == 0:
		StrElement = "wind"
	elif MonsterElement == 1:
		StrElement = "water"
	elif MonsterElement == 2:
		StrElement = "earth"
	elif MonsterElement == 3:
		StrElement = "fire"
	return(StrElement, MonsterElement)
	 
def MonsterLevelFunction(MapProgress):
	if MapProgress == 0:
		MonsterLevel = random.randint(1,3)
	elif MapProgress == 1:
		MonsterLevel = random.randint(4,8)
	elif MapProgress == 2:
		MonsterLevel = random.randint(9,13)
	elif MapProgress == 3:
		MonsterLevel = random.randint(14,18)
	elif MapProgress == 4:
		MonsterLevel = random.randint(19,23) 
	return(MonsterLevel)

def MonsterStats(MapProgress):
	MonsterType, MonsterMultiplier = MonsterTypeFunction(MapProgress)
	StrElement, MonsterElement = MonsterElementFunction(MapProgress)
	MonsterLevel = MonsterLevelFunction(MapProgress)
	MonsterHealth = 8 * MonsterMultiplier * MonsterLevel
	MonsterAttack = 2 * MonsterMultiplier * MonsterLevel
	return(MonsterType, MonsterMultiplier, StrElement, MonsterElement, MonsterLevel, MonsterHealth, MonsterAttack)
	 
def Travel(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerLevel, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion):
	for i in range(0,random.randint(MapProgress + 2, MapProgress + 3)):
		PlayerCurrentHealth, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion, MonsterElement, MonsterMultiplier = Decision(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion)
		PlayerWind, PlayerWater, PlayerEarth, PlayerFire = Blessing(PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterMultiplier, MonsterElement)
		PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerLevel, PlayerExperience = LevelUp(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerLevel, PlayerExperience)
	return(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerLevel, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion)

def Decision(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion):
	MonsterElement, MonsterHealth, MonsterAttack, MonsterMultiplier = MonsterExamination(MapProgress)
	print("Do you fight? Or do you run?")
	time.sleep(1)
	while True:
		FightOrRun = input("enter [q] for fight [w] for run: ")
		if FightOrRun == "q":
			PlayerCurrentHealth, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion = CombatCycle(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion, MonsterElement, MonsterHealth, MonsterAttack, MonsterMultiplier)
			'''
			LevelUp(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerLevel, PlayerExperience)
			'''
			break
		if FightOrRun == "w":
			PlayerCurrentHealth -= MonsterAttack
			print("The monster managed to hit you once but you ran away")
			time.sleep(1)			
			print("You now have " + str(PlayerCurrentHealth) + " health")
			time.sleep(1)			
			if PlayerCurrentHealth <= 0:
				print ("You lost")
				time.sleep(3)				
				exit()                   	 
			break
	return(PlayerCurrentHealth, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion, MonsterElement, MonsterMultiplier)

def CombatCycle(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion, MonsterElement, MonsterHealth, MonsterAttack, MonsterMultiplier):
	SkillPoint = 0
	while MonsterHealth * PlayerCurrentHealth > 0:
		PlayerCurrentHealth, PlayerApple, PlayerPotion, MonsterDamage, SkillPoint, Idle = Combat(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion, MonsterElement, MonsterHealth, MonsterAttack, SkillPoint)
		if MonsterDamage > 0:
			MonsterHealth -= MonsterDamage
			if MonsterHealth <= 0:
				print("The monster has taken " + str(MonsterDamage) + " damage, it has been defeated")
				time.sleep(1)
				print ("you won, with " + str(PlayerCurrentHealth) + " health left.")
				time.sleep(1)
				PlayerExperience += MonsterAttack * 3
				print ("you have gained " + str(MonsterAttack * 3) + " experience")
				PlayerGold += MonsterAttack
				print ("you have gained " + str(MonsterAttack) + " gold, you now have " + str(PlayerGold) + " gold")
				time.sleep(1)
				'''
				LevelUp(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerLevel, PlayerExperience)
				'''
				return(PlayerCurrentHealth, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion)
			else:
				print("The monster has taken " + str(MonsterDamage) + " damage, it has " + str(MonsterHealth) + " health left")
		if Idle == 0:
			PlayerCurrentHealth -= MonsterAttack
			print("You have taken " + str(MonsterAttack) + " damage, you have " + str(PlayerCurrentHealth) + " health left")
			if PlayerCurrentHealth <= 0:
				print ("You lost")
				exit()
			SkillPoint += 1
			print("You now have " + str(SkillPoint) + " skill points")
			time.sleep(1)

def Combat(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion, MonsterElement, MonsterHealth, MonsterAttack, SkillPoint):
	while True:
		option = input("enter [q] to attack, [w] to use item: ")
		if option == "q":
			while True:
				option = input("enter [q] to normal attack, [w] to use special skill: ")
				if option == "q":
					Idle = 0
					Hit = 1
					HitStrength = 1
					MonsterDamage = DamageCalculation(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, Hit, HitStrength)
					return(PlayerCurrentHealth, PlayerApple, PlayerPotion, MonsterDamage, SkillPoint, Idle)
				if option == "w":
					Idle = 0
					SkillPoint, MonsterDamage, Idle = Skill(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, SkillPoint, Idle)
					return(PlayerCurrentHealth, PlayerApple, PlayerPotion, MonsterDamage, SkillPoint, Idle)
		if option == "w":
			Idle = 0
			PlayerCurrentHealth, PlayerApple, PlayerPotion, MonsterDamage, SkillPoint, Idle = UseItem(PlayerMaxHealth, PlayerCurrentHealth, PlayerApple, PlayerPotion, MonsterAttack, SkillPoint, Idle)
			return(PlayerCurrentHealth, PlayerApple, PlayerPotion, MonsterDamage, SkillPoint, Idle)
				 
def Skill(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, SkillPoint, Idle):
	print("Skill List:")
	print("[q] Double Strike: 1 SP [Strike the target twice for 70% damage each]")
	print("[w] Triple Strike: 2 SP [Strike the target thrice for 60% damage each]")
	print("[e] Divine Sword: 2 SP [Strike the target random amoount of times for 50% each]")
	print("[r] Reckless Strike: 0 SP [50% chance to strike target for 200% damage...50% to miss")
	print("[t] Storm Strike: 1 SP [Strike the target with 100% wind damage]")
	print("[y] Aqua Strike: 1 SP [Strike the target with 100% water damage]")
	print("[u] Stone Strike: 1 SP [Strike the target with 100% earth damage]")
	print("[i] Infernal Strike: 1 SP [Strike the target with 100% fire damage]")
	while True:
		option = input("which skill will you use? [a] to go back: ")
		HitStrength = 1
		if option == "q":
			if SkillPoint >= 1:
				SkillPoint -= 1
				Hit = 2
				HitStrength = 0.7
				print("You've struck the monster " + str(Hit) + " times")
				MonsterDamage = DamageCalculation(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, Hit, HitStrength)
				return(SkillPoint, MonsterDamage, Idle)
			else:
				print("You don't have enough SP!")
		if option == "w":
			if SkillPoint >= 2:
				SkillPoint -= 2
				Hit = 3
				HitStrength = 0.6
				print("You've struck the monster " + str(Hit) + " times")
				MonsterDamage = DamageCalculation(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, Hit, HitStrength)
				return(SkillPoint, MonsterDamage, Idle)
			else:
				print("You don't have enough SP!")  
		if option == "e":
			if SkillPoint >= 2:
				SkillPoint -= 2
				Hit = 1
				while True:
					x = random.randint(0,1)
					if x == 0:
						Hit += 1
					else:
						break
				HitStrength = 0.5
				print("You've struck the monster " + str(Hit) + " times")
				MonsterDamage = DamageCalculation(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, Hit, HitStrength)
				return(SkillPoint, MonsterDamage, Idle)
			else:
				print("You don't have enough SP!")
		if option == "r":
			Hit = random.randint(0,1)
			HitStrength = 2
			print("You've struck the monster " + str(Hit) + " times")
			MonsterDamage = DamageCalculation(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, Hit, HitStrength)
			return(SkillPoint, MonsterDamage, Idle)		
		if option == "t":
			if SkillPoint >= 1:
				SkillPoint -= 1
				Hit = 1
				PlayerWind += PlayerAttack
				PlayerAttack = 0
				print("You've struck the monster " + str(Hit) + " times")
				MonsterDamage = DamageCalculation(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, Hit, HitStrength)
				return(SkillPoint, MonsterDamage, Idle)
			else:
				print("You don't have enough SP!")
		if option == "y":
			if SkillPoint >= 1:
				SkillPoint -= 1
				Hit = 1
				PlayerWater += PlayerAttack
				PlayerAttack = 0
				print("You've struck the monster " + str(Hit) + " times")
				MonsterDamage = DamageCalculation(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, Hit, HitStrength)
				return(SkillPoint, MonsterDamage, Idle)
			else:
				print("You don't have enough SP!")	
		if option == "u":
			if SkillPoint >= 1:
				SkillPoint -= 1
				Hit = 1
				PlayerEarth += PlayerAttack
				PlayerAttack = 0
				print("You've struck the monster " + str(Hit) + " times")
				MonsterDamage = DamageCalculation(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, Hit, HitStrength)
				return(SkillPoint, MonsterDamage, Idle)
			else:
				print("You don't have enough SP!")
		if option == "i":
			if SkillPoint >= 1:
				SkillPoint -= 1
				Hit = 1
				PlayerFire += PlayerAttack
				PlayerAttack = 0
				print("You've struck the monster " + str(Hit) + " times")
				MonsterDamage = DamageCalculation(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, Hit, HitStrength)
				return(SkillPoint, MonsterDamage, Idle)
			else:
				print("You don't have enough SP!")	
		if option == "a":
			Idle = 1
			MonsterDamage = 0
			return(SkillPoint, MonsterDamage, Idle)

def DamageCalculation(PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterElement, Hit, HitStrength):
	MonsterDamage = PlayerAttack * Hit * HitStrength
	if MonsterElement == 0:
		MonsterDamage += PlayerWind * Hit
		MonsterDamage += PlayerWater * Hit
		MonsterDamage += PlayerEarth * Hit / 2
		MonsterDamage += PlayerFire * Hit * 2
	elif MonsterElement == 1:
		MonsterDamage += PlayerWind * Hit
		MonsterDamage += PlayerWater * Hit
		MonsterDamage += PlayerEarth * Hit * 2
		MonsterDamage += PlayerFire * Hit / 2
	elif MonsterElement == 2:
		MonsterDamage += PlayerWind * Hit * 2
		MonsterDamage += PlayerWater * Hit / 2
		MonsterDamage += PlayerEarth * Hit
		MonsterDamage += PlayerFire * Hit
	elif MonsterElement == 3:
		MonsterDamage += PlayerWind * Hit / 2
		MonsterDamage += PlayerWater * Hit * 2
		MonsterDamage += PlayerEarth * Hit
		MonsterDamage += PlayerFire * Hit
	MonsterDamage = (round(MonsterDamage))
	return(MonsterDamage)

def UseItem(PlayerMaxHealth, PlayerCurrentHealth, PlayerApple, PlayerPotion, MonsterAttack, SkillPoint, Idle): #experimental
	while True:
		option = input("enter [q] to eat apple, [w] to drink potion, [a] to go back: ")
		if option == "q":
			if PlayerApple != 0:
				MonsterDamage = 0
				PlayerApple -= 1
				OldHealth = PlayerCurrentHealth
				NewHealth = PlayerCurrentHealth + PlayerMaxHealth / 5
				if NewHealth > PlayerMaxHealth:
					NewHealth = PlayerMaxHealth
				print("You ate an apple and healed " + str(NewHealth - OldHealth) + " health")
				PlayerCurrentHealth = NewHealth
				return(PlayerCurrentHealth, PlayerApple, PlayerPotion, MonsterDamage, SkillPoint, Idle)
			else:
				print("You do not have enough item")
		if option == "w":
			if PlayerPotion != 0:
				MonsterDamage = 0
				SkillPoint += 2
				PlayerPotion -= 1
				return(PlayerCurrentHealth, PlayerApple, PlayerPotion, MonsterDamage, SkillPoint, Idle)
			else:
				print("You do not have enough item")			
		if option == "a":
			Idle = 1
			MonsterDamage = 0
			return(PlayerCurrentHealth, PlayerApple, PlayerPotion, MonsterDamage, SkillPoint, Idle)
		
def Blessing(PlayerWind, PlayerWater, PlayerEarth, PlayerFire, MonsterMultiplier, MonsterElement):
	if MonsterMultiplier == 1:
		chance = random.randint(0,0)
		if chance == 0:
			if MonsterElement == 0:
				PlayerWind += 2
				print("You've gain the wind spirit's blessing your hits now do 2 additional wind damage")
			elif MonsterElement == 1:
				PlayerWater += 2
				print("You've gain the water spirit's blessing your hits now do 2 additional water damage")
			elif MonsterElement == 2:
				PlayerEarth += 2
				print("You've gain the earth spirit's blessing your hits now do 2 additional earth damage")
			elif MonsterElement == 3:
				PlayerFire += 2
				print("You've gain the fire spirit's blessing your hits now do 2 additional fire damage")
	elif MonsterMultiplier == 3:
		chance = random.randint(0,2)
		if change == 0:
			if MonsterElement == 0:
				PlayerWind += 4
				print("You've gain the wind spirit's blessing your hits now do 4 additional wind damage")
			elif MonsterElement == 1:
				PlayerWater += 4
				print("You've gain the water spirit's blessing your hits now do 4 additional water damage")
			elif MonsterElement == 2:
				PlayerEarth += 4
				print("You've gain the earth spirit's blessing your hits now do 4 additional earth damage")
			elif MonsterElement == 3:
				PlayerFire += 4
				print("You've gain the fire spirit's blessing your hits now do 4 additional fire damage")
	else:
		if MonsterElement == 0:
			PlayerWind += 6
			print("You've gain the wind spirit's blessing your hits now do 6 additional wind damage")
		if MonsterElement == 1:
			PlayerWater += 6
			print("You've gain the water spirit's blessing your hits now do 6 additional water damage")
		if MonsterElement == 2:
			PlayerEarth += 6
			print("You've gain the earth spirit's blessing your hits now do 6 additional earth damage")
		if MonsterElement == 3:
			PlayerFire += 6
			print("You've gain the fire spirit's blessing your hits now do 6 additional fire damage")
	return(PlayerWind, PlayerWater, PlayerEarth, PlayerFire)
    
def LevelUp(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerLevel, PlayerExperience):
	NewPlayerLevel = PlayerLevel
	NewPlayerExperience = PlayerExperience
	while NewPlayerExperience >= NewPlayerLevel * NewPlayerLevel * 2:
		NewPlayerLevel += 1
		NewPlayerExperience -= (NewPlayerLevel * NewPlayerLevel * 3)
		print("You have leveled up!")
		time.sleep(1)		
		print("You are now level " + str(NewPlayerLevel) + "!")
		time.sleep(1)		
		print("Choose a stat to enhance")
		time.sleep(1)		
		option = input("Enter [q] for health, [w] for attack: ")
		if option == "q":
			PlayerMaxHealth += 25
			PlayerCurrentHealth += 25
			print("You enhanced your max health! Now your max health is " + str(PlayerMaxHealth))
			time.sleep(1)			
		if option == "w":
			PlayerAttack += 5
			print("You enhanced your attack! Now your attack is " + str(PlayerAttack))
			time.sleep(1)			
	return(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, NewPlayerLevel, NewPlayerExperience)

def Town(MapProgress, PlayerMaxHealth, PlayerCurrentHealth, PlayerGold, PlayerApple, PlayerPotion):
	if MapProgress == 0:
		TownName = "Stormouver"
	if MapProgress == 1:
		TownName = "Aquaton"
	if MapProgress == 2:
		TownName = "Mountreal"
	if MapProgress == 3:
		TownName = "Volronto"
	if MapProgress == 4:
		TownName = "Chaos Town"
	print("You've arrived to " + TownName)
	PlayerCurrentHealth = PlayerMaxHealth
	print("You took a break in town and restored your health")
	time.sleep(1)	
	print("Where would you like to go?")
	time.sleep(1)	
	while True:
		option = input("[q] for shop, [w] for next, [e] for previous: ")
		if option == "q":
			print("Shop stock")
			while True:
				shop = input("[q] apple for 10 gold, [w] potion for 20 gold, [a] to exit shop: ")
				if shop == "q":
					if PlayerGold >= 10:
						PlayerGold -= 10
						PlayerApple += 1
						print("You have purchased 1 apple, you have " + str(PlayerApple) + " apple(s) and " + str(PlayerGold) + " gold left")
						time.sleep(1)
						shop = None #prevents infinite loop
						boughtitem = True
					else:
						print("You do not have enough gold")
						time.sleep(1)
						shop = None
				if shop == "w":
					if PlayerGold >= 20:
						PlayerGold -= 20
						PlayerPotion += 1
						print("You have purchased 1 potion, you have " + str(PlayerPotion) + " potion(s) and " + str(PlayerGold) + " gold left")
						time.sleep(1)
						shop = None
					else:
						print("You do not have enough gold")
						time.sleep(1)
						shop = None
				if shop == "a":
					break
		if option == "w":
			NewMapProgress = MapProgress + 1
			break
		if option == "e":
			if MapProgress == 0:
				print("Your path back out of this town is blocked by a storm!")
			else:
				NewMapProgress = MapProgress - 1
				break
	return(NewMapProgress, PlayerCurrentHealth, PlayerGold, PlayerApple, PlayerPotion)

def TutorialSection(TutorialConcept, RequiredInput, NarratorOutput):
	'''
	Inputs: TutorialConcept, RequiredInput, NarratorOutput
	Outputs: NarratorOutput
	Use it by selecting the concept you want to highlight and its required input. Also select the guide's output with 
	NarratorOutput
	'''
	TutorialSectionComplete = False
	while TutorialSectionComplete == False:
		print("Input " + "[" + RequiredInput + "] " + "when prompted to " + TutorialConcept)
		time.sleep(1)
		TutorialChoice = input("Enter " + "[" + RequiredInput + "] ")
		if TutorialChoice == RequiredInput:
			print(NarratorOutput)
			time.sleep(1)
			TutorialSectionComplete = True	
		else: 
			print("You didn't enter a valid input!")
			time.sleep(1)
def Introduction():
	print("<<<You have arrived at the start>>>")
	time.sleep(2)
	print("Hello, welcome to the land of Dreams...at least that is what we used to call it")
	time.sleep(3)
	print("This used to be a peaceful land...until he who shall not be named arrived...")
	time.sleep(2)
	print("A young adventurer like you might just be the one to defeat the monsters once and for all")
	time.sleep(3)
	print("Here, show us your skills with this training dummy")
	time.sleep(2)
	print("You have encountered a level 100 training dummy")
	time.sleep(2)
	print("Swing at the dummy by pressing [q]")
	time.sleep(2)
	TutorialSection("attack", "q", "You attacked the dummy")
	print("The dummy's swung back and hit you! You need to heal with this apple")
	TutorialSection("open your bag", "w", "You opened your bag")
	TutorialSection("use an apple and heal", "q", "You healed")
	print("Maybe you should use one of your skill moves, here take this potion")
	time.sleep(2)
	TutorialSection("use a potion to gain Skill Points", "w", "You gained SP!")
	print("You gain SP naturally from fighting, potions are a good way to speed up the process!")
	time.sleep(2)
	TutorialSection("open your skills","w", "You opened your skills")
	TutorialSection("use double strike", "q", "You used double kick")
	print("That'll teach it, when you defeat monsters in the wild they will drop gold that you can use in shops and give you experience")
	time.sleep(2)
	print("Haha now that you know how to defeat monsters wouldn't it be crazy if a monster attacked?")
	time.sleep(3)
	print("Now you must go on your quest...it won’t be easy to defea-")
	time.sleep(2)
	print("What's that?")
	time.sleep(2)
	print("OH NO A MONSTER IS ATTACKING")
	time.sleep(3)

def GameWinner():
	print("You have saved the kingdom from the Demon Lord! Rejoice and add your name to the hall of fame!")
	time.sleep(3)
	HOFfile = open("CSCA20ProjectHallofFame.txt", "a")
	PlayerName = (input("What is your name adventurer ([First Name] [Last Name]): "))
	if PlayerName == "":
		print("You didn't enter your name ;(")
	else:
		HOFfile.write(PlayerName + "\n")
		HOFfile.close()
		print("Welcome to the Hall of Fame " + PlayerName)
		time.sleep(2)

def HallofFameReading():
	HOFfile = open("CSCA20ProjectHallofFame.txt", "r")
	print("These are the current heroes in the hall of fame: ")
	time.sleep(2)
	for nameindex in HOFfile:
		print((nameindex)[:-1])
		time.sleep(2)
	HOFfile.close()
	
Introduction()
while MapProgress != 5:
	PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerLevel, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion = Travel(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerLevel, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion)
	MapProgress, PlayerCurrentHealth, PlayerGold, PlayerApple, PlayerPotion = Town(MapProgress, PlayerMaxHealth, PlayerCurrentHealth, PlayerGold, PlayerApple, PlayerPotion)
if MapProgress == 5:
	MonsterType = "Demon Lord, Zyx"
	MonsterMultiplier = 10	
	MonsterLevel = 25
	MonsterElement = random.randint(0,3)
	if MonsterElement == 0:
		StrElement = "wind"
	elif MonsterElement == 1:
		StrElement = "water"
	elif MonsterElement == 2:
		StrElement = "earth"
	elif MonsterElement == 3:
		StrElement = "fire"
	MonsterHealth = 2000
	MonsterAttack = 750	
	print("You have enounctered a level " + str(MonsterLevel) + " " + str(StrElement) + " " + str(MonsterType))
	time.sleep(1)	
	print("It has " + str(MonsterHealth) + " health and " + str(MonsterAttack) + " attack")
	time.sleep(1)		
	CombatCycle(PlayerMaxHealth, PlayerCurrentHealth, PlayerAttack, PlayerWind, PlayerWater, PlayerEarth, PlayerFire, PlayerExperience, PlayerGold, PlayerApple, PlayerPotion, MonsterElement, MonsterHealth, MonsterAttack, MonsterMultiplier)
	GameWinner()
	HallofFameReading()
	exit()
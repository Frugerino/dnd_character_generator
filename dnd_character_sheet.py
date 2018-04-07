from random import randint
from random import choice

character = {}

def roll_d_sided(sided): # Makes and any-sided die roll
    return randint(1, sided)

def roll_attribute(): # Rolls 3d6 and sums the value
    return sum(roll_d_sided(6) for i in range(3))

def character_initilization():
	print("Let's create a character . . .")
	player_name = input("First, tell me your name, player?: ")
	character_name = input("Name your adventurer: ")
	character_classes = ('fighter', 'cleric', 'wizard', 'rouge', 'elf', 'dwarf', 'halfling')
	character_class = input("Choose a class . . . \n"
	                        "Fighter,\n"
	                        "Cleric,\n"
	                        "Wizard,\n"
	                        "Rouge,\n"
	                        "Elf,\n"
	                        "Dwarf,\n"
	                        "or Halfling \n")

	while character_class.lower() not in character_classes:
		character_class = input("Please choose a valid class, fool: ")

	character_age = input(f"So, {character_name} the {character_class}, what is your age? ")
	character = {
	    "name": character_name,
	    "player": player_name,
	    "class": character_class,
	    "age": character_age
	}
	# print("Here is what we have so far: ")
	# for stat in character:
	#     print(f"{stat.upper()}: {character[stat]}")
	# for (k, v) in attributes.items():
	#     print(f"{k}: {v}")

attributes = dict(zip(["STR", "DEX", "CON", "INT", "WIS", "CHA"],
    [roll_attribute() for i in range(6)]))

character_initilization()

print("Here is what we have so far: ")
for stat in character:
	print(f"{stat.upper()}: {character[stat]}")
for (k, v) in attributes.items():
	print(f"{k}: {v}")



#print("Great! Now let's roll some attributes.")

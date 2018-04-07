from random import randint

# character = {
#     "name": "Lannis",
#     "player": "Frug",
#     "class": "Elf",
#     "age": 401
# }
#
# print("Here is what we have so far: ")
# for stat in character:
#     print(f"{stat.upper()}: {character[stat]}")\

def roll_d_sided(sided): # Makes and any-sided die roll
    return randint(1, sided)

def roll_attribute(): # Rolls 3d6 and sums the value
    # score =0
    # for j in range(3):
    #     score += roll_d_sided(6)
    # return score
    return sum(roll_d_sided(6) for i in range(3))

#print(roll_attribute())

# attributes = {
#     "STR": roll_attribute(),
#     "DEX": roll_attribute(),
#     "CON": roll_attribute(),
#     "INT": roll_attribute(),
#     "WIS": roll_attribute(),
#     "CHA": roll_attribute()
# }

attributes = dict(zip(["STR", "DEX", "CON", "INT", "WIS", "CHA"],
    [roll_attribute() for i in range(6)]))
for (k, v) in attributes.items():
    print(f"{k}: {v}")
# print(attributes)
# print(attributes)


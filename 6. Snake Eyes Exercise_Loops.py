# We are rolling 2 dices, when both are 1, we've got snake eyes

import random
roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
roll_count = 1

while roll1 !=1 or roll2 !=1:
    print(roll1, roll2)
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll_count +=1
    
print (roll1, roll2)
print("Here you go, snake eyes!")
print(f"It took {roll_count} number of rolls")
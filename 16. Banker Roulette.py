# Select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# Easiest version below

# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ") 

# pays_bill = random.choice(names)
# print(pays_bill)


# My version

import random
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ") 

# The last index is one less than the total number of items beause we start counting from 0

all_names = len(names)
print (f"{random.sample(names, all_names -1)[0]} is going to buy the meal today!")
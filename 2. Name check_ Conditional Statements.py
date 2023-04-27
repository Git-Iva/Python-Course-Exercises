# Check if a user's name is longer or shorter than the average American name
# The average American name is 12 characters long 

first_name = input ("What is your first name? ")
last_name = input("What is your last name? ")
print ("*"*30)
if len(first_name + last_name) < 12:
    print (f"{first_name} {last_name} is shorter than the average American name.")
elif len(first_name + last_name) > 12:
    print(f"{first_name} {last_name} is longer than the average American name.")

else:
    print(f"{first_name} {last_name} is exactly as long as the average American name!")

print ("*"*30)
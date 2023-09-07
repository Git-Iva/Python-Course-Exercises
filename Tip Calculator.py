print ("Welcome to the tip calculator!")
print(25 * "*")

total_bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give - 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
split_amount = (total_bill / people) * (tip / 100 + 1)

print(25 * "*")
print (f"Each person should pay ${split_amount: .2f}")
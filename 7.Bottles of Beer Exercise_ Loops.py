#Bottles of beer loop exercise with a while loop. Here we go:

bottles_of_beer = 99
print("99 Bottles of beer on the wall.")
print("99 Bottles of beer.")
bottles_of_beer -= 1
print(f"Take one down, pass it around. {bottles_of_beer} bottles of beer on the wall.")
print("*" * 50 )

while bottles_of_beer > 0:
  
  print(f"{bottles_of_beer} bottles of beer on the wall.")
  print(f"{bottles_of_beer} bottles of beer.")
  bottles_of_beer -= 1
  if bottles_of_beer == 1:
    print (f"take one down, pass it around. No more bottles of beer on the wall!")
  else:
    print(f"Take one down, pass it around. {bottles_of_beer} bottles of beer on the wall!")
  print("*" * 50 )


# more elegant version of the while loop:

bottles_of_beer = 99

while bottles_of_beer > 0:
    print(f"There are {bottles_of_beer} bottles of beer on the wall.")
    print(f"There are {bottles_of_beer} bottles of beer.")

    if bottles_of_beer == 1:
        print("Take one down, pass it around. There are no more bottles of beer on the wall!")
    else:
        print(f"Take one down, pass it around. There are {bottles_of_beer - 1} bottles of beer on the wall.")
    bottles_of_beer -= 1
    print("*" * 50)


#Bottles of beer loop exercise with a for loop. Here we go:
for bottles_of_beer in range(99,0,-1):
    print(f"{bottles_of_beer} bottles of beer on the wall.")
    print(f"{bottles_of_beer} bottles of beer.")
 
    if bottles_of_beer == 1:
        print(f"Take one down, pass it around. No more bottles of beer on the wall!")
    else:
         print(f"Take one down, pass it around. {bottles_of_beer - 1} bottles of beer on the wall.")
    print("*" * 50 )



  
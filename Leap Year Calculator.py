year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code below 👇

#Write your code below this line 👇


if year % 4 == 0:
 if year % 100 == 0:
   if year % 400 == 0:
     print("Leap year.")
   else:
     print("Not leap year.")
 else:
    print ("Leap year.")

else:
  print ("Not leap year.")






#if year % 4 == 0 and year % 100 !=0 and year % 400 ==0:
 #   print ("It's a leap year.")
    
#else:
  #  print ("It's not a leap year.")

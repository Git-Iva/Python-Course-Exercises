# Create a simple script that calculates a user's bodymass index

height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))
BMI = round((weight * 703) / (height * height),1)


if BMI <16.0:
   category =  "Severely Underweight"

elif BMI < 18.4:
    category = "Underweight"

elif BMI < 24.9:
    category = "Normal"

elif BMI < 29.9:
   category =" Overweight"

elif BMI < 34.9:
    category =" Moderately Obese"

elif BMI < 39.9:
    category = "Severely Obese"

else:
    category = "Morbidly Obese"
    
print(f"Your BMI of {BMI} makes you {category}")
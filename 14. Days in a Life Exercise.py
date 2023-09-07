
# Days in a Life Exercise
# Oh man, life is short!

age = input("What is your current age? ")

int_age = int(age)
total_days = 90 * 365
total_weeks = 90 * 52
total_months = 90 * 12


days_left = total_days - int_age * 365
weeks_left = total_weeks - int_age * 52
months_left = total_months -int_age * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")





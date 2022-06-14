# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
months = 12
weeks = 52
days = 365
final = 90

calc_age = final - age
calc_months = calc_age * months
calc_weeks = calc_age * weeks
calc_days = calc_age * days

print(f'You have {calc_days} days, {calc_weeks} weeks and {calc_months} months')
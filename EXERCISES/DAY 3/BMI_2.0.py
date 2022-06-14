# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#calculating the weight divided by height x height.
bmi = round(weight / height**2)

# If the calculation value got <18.5 or < 25, you gonna print: "you are underweight"... That's to all them.

if bmi < 18.5:
  print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
  print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
  print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35:
  print(f'Your BMI is {bmi}, you are obese.')
else:
  print(f'Your BMI is {bmi}, you are clinically obese.')

#When we get to the last number, that was 35, we just need to put the else because every number that isn't in the else-elif, will be considered what the print is saying.
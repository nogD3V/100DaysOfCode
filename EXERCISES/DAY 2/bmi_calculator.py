# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#I transformed the variables above that was ready in float.

#calculating the weight divided by height x height.
bmi = weight / height**2
#To got just the numbers before the comma, I transformed the variable in INT. 
bmi_as_int = int(bmi)
print(bmi_as_int)


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1 + name2
names_lower = names.lower()

t1 = names_lower.count("t")
t2 = names_lower.count("r")
t3 = names_lower.count("u")
t4 = names_lower.count("e")

l1 = names_lower.count("l")
l2 = names_lower.count("o")
l3 = names_lower.count("v")
l4 = names_lower.count("e")

true = t1 + t2 + t3 + t4
love = l1 + l2+ l3 + l4

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
  print(f'Your score is {score}, you go togheter like coke and mentos.')

elif (score >=40) and (score <= 50):
  print(f'Your score is {score}, you are alright togheter')

else:
  print(f'Your score is {score}')
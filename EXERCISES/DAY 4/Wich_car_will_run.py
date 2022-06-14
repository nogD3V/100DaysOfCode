import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#get all numbers in a list
num_items = len(names)
#Generate random numbers between 0 and the last one.
random_choice = random.randint(0, num_items -1)

car_wich_will_run = names[random_choice]

print(f"{car_wich_will_run} is gonna run today")
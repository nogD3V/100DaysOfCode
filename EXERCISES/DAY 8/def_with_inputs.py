#Function
#def greet():
#  print("Hello")
#  print("How do you do?")
#  print("Isn't the weather nice today?")

#Function with input
#def greet_with_name(name):
#  print(f"Hello {name}")
#  print(f"How do you do {name}?")

# greet_with_name(input('What's your name: ))

#Functions with multiples inputs
#def greet_with(name, location):
#  print(f"My name is {name} and I live in {location}")
  
#greet_with(input(f"What's your name? "), input("What's your location? "))

#Functions with keywords arguments
def greet_with(name, location):
  print(f"My name is {name} and I live in {location}")

greet_with(name = "Lucas", location = "Osasco")
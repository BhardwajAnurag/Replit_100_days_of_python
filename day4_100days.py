print(
    "Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!"
)
print()
name = input("What is your name? ")
enemy = input("What is your worst enemy’s name? ")
power = input("What is your superpower? ")

print("Hello", name, "! Your ability to", "\033[31m", power, "\033[0m"
      "will make sure you never have to look at", enemy, "again.")

address = input("Where do you live? ")
food = input("What is your favorite food? ")

print("Go eat", food, "as you walk down the streets of", address, "and use",
      power, "for good and not evil!")

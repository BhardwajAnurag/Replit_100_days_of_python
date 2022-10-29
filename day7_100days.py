print("Fake Fan Finder")
print("----------------------------")
anime = input("""What's your Favourite Anime? 
""")
if anime == "One piece":
  character = input("Oh really? Tell me a few of the characters \n")
  if character == "Nami":
    job = input("You got this by pure chance. Tell me what does she do on the ship?")
    if job == "Navigator":
        bounty = input("Hmm! What was her first bounty then?")
        if bounty == "money":
            print("You are true fan")
        else:
            print("Gotcha! A FAKE one piece fan!")
    else:
        print("Gotcha! A FAKE one piece fan!")
  else:
    print("Gotcha! A FAKE one piece fan!")
else:
  print("Gotcha! A FAKE one piece fan!")
          
# order = input("What would you like to order: pizza or hamburger? ")
# if order == "hamburger":
#   print("Thank you.")
#   cheese = input("Do you want cheese? ")
#   if cheese == "yes":
#     print("You got it.")
#   else: 
#     print("No cheese it is.")
# elif order == "pizza":
#   print("Pizza coming up.")
#   toppings = input("Do you want pepperoni on that? ")
#   if toppings == "yes":
#     print("We will add pepperoni.")
#   else:
#     print("Your pizza will not have pepperoni.")

# tvShow = input("What is your favourite tv show? ")
# if tvShow == "the office":
#   print("Ugh, why?")
#   faveCharacter = input("Who is your favourite character? ")
#   if faveCharacter == "jim":
#     print("he is tall")
#   elif faveCharacter == "dwight":
#     print("he has short nose")
#   else:
#     print("bad choice")
# elif tvShow == "friends":
#   print("Aww, it's very old")
# else:
#   print("Yeah, that's cool and all…")
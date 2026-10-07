
# if = Do some code only IF some condition is True
# Else do some other shit

# age = int(input("Enter your age: "))

# if age >= 100:
#     print("Get out of here you old sack of bones")
# elif age >= 18:
#     print("You qualify to enlist in the army")
# elif age < 0:
#     print("How are you typing this?")
# else:
#    print("You don't qualify to enlist in the army, good for you")

response = input("Would you like to go and be gay today? (Y/N): ")

if response == "Y":
    print("It's time to be gay and do crimes")
elif response == "N":
    print("Well fine, go be straight on your own time")
elif response != "Y" or "N":
    print("Huh?")



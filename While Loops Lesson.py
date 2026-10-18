# while loop = execute some code WHILE some condition remains true

# name = input("Enter your name: ")

# while name == "":
#     print("You didn't enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age <0:
#     print("Da fuck you mean you ain't born?")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter your favorite food (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("Bye")

num = int(input("Enter a number between 1 and 100: "))

while num < 1 or num > 100:
    print(f"You stupid? Read the damn question")
    num = int(input("Enter a number between 1 and 100: "))

print(f"Your number is {num}")
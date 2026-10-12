# var.index("") = state what you want to find in "" and it will return an int value
# of where it's first found

email = input("Enter your email: ")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

# print(f"Your username is {username} and domain is {domain}")

print(email.index("@"))
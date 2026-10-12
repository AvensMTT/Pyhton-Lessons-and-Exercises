# 1. username is no more than 12 characters
# 2. username must not contain space
# 3. username must not contain digits

username = input("Please enter a username to create: ")



if len(username) > 12:
    print("Username must be no more than 12 characters long")
elif username.isdigit():
    print("Username must not include numbers or spaces")
else:
    print(f"Welcome {username}")
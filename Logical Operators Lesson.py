# logical operators = used on conditional statements

#      and = checks for TWO or more conditions if True
#      or = checks if at least ONE condition is True
#      not = True if condition is False, and vice versa

temp = 25
sunny = True

if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

if not sunny:
    print("It's sunny outside")
else:
    print("It's cloudy outside")


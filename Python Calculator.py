
operators = input("Enter the operator ( +, -, *, / ): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
add = num1 + num2
sub = num1 - num2
multi = num1 * num2
divide = num1 / num2

if operators == "+":
    print(add)
elif operators == "-":
    print(sub)
elif operators == "*":
    print(multi)
elif operators == "/":
    print(divide)
elif operators != "+" or "-" or "*" or "/":
    print("What the fuck do you mean NUH UH?")
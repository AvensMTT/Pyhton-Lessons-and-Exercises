# Python Compound Interest Calc (Calc is short for calculator)

principle = 0
rate = 0
time = 0


while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be lower than or equal to 0")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest Rate can't be lower than or equal to 0")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Amount of time can't be lower than or equal to 0")
    else:
        break

total = principle * pow(1 + rate / 100, time)

print(f"Balance after {time} years: ${total:.2f} ")

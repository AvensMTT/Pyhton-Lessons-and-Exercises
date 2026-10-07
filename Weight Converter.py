
measure = input("Enter unit of measurement you want to convert (lbs/grams): ")
num1 = float(input("Enter number: "))
lbs_grams = num1 * 453.59237

if measure == "lbs":
    print(f"{lbs_grams} grams")



# format specifiers = {value:flags} format a value based on what
#                              flags are inserted

# .(number) = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place a sign to inidicate postitive value
# :  = insert a space before positve numbers
# :, = comma seprator

price1 = 12343.1459
price2 = -987.87
price3 = 12.34

print(f"Price 1 is ${price1:,.2f}")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")
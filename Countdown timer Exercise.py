# countdown timer
import time

timer = int(input("Enter a time to countdown from: "))

for x in range(timer, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds:02}")
    time.sleep(1)


print("TIME'S UP!")

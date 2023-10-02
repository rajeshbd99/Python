#Time greeting
#write a program that greets the user with "Good morning", "Good afternoon" or "Good evening" depending on the time of the day.
import time

timestamp = (time.strftime("%H:%M:%S"))
print(timestamp)

if timestamp < "12:00:00":
    print("Good morning")
elif timestamp < "18:00:00":
    print("Good afternoon")
else:
    print("Good evening")

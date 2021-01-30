import os
import time

#This is a countdown. Or call it timer. What ever. You just have to run this code and it'll ask you what amount of seconds it should run.
#Savity warning: Only works on Mac (Apple). 

#preparation
os.system("clear")
print("______________________  _____________________  ")
print("___  __/____  _/___   |/  /___  ____/___  __ \ ")
print("__  /    __  /  __  /|_/ / __  __/   __  /_/ / ")
print("_  /    __/ /   _  /  / /  _  /___   _  _, _/  ")
print("/_/     /___/   /_/  /_/   /_____/   /_/ |_|   ")

print("Credits to Schnitchen1423:")
print("YouTube: https://www.youtube.com/channel/UCkZxbU5wz6hNQM771SlL12w ")
print("GitHub: https://github.com/Schnittchen1423 ")

# String
CountDown = raw_input("Seconds: ")

# Integer
int_CountDown = int(CountDown)
expired = False


while expired == False:
	try:
		print(int_CountDown)
		time.sleep(1)
		int_CountDown = int_CountDown - 1
		
		if int_CountDown == 0:
		 print("Countdown expired")
		 expired = True
		 print("Stopped")
		 time.sleep(3)
		 os.system("clear")
		 print("Countdown expired.")
		 print("Program stopped.")
		 os.system("exit")

	except:
		print("Error")

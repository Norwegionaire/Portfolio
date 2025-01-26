import random
import time

randNum = random.randint(1, 100)

#introductory text
print("Welcome to the great guessing game")
time.sleep(2)
print("In this game you have to guess a number between 1 and 100")
time.sleep(2)
print("If you win you get a glorious reward")
time.sleep(2)

#input for names
player_1 = input("Player 1, please enter your name: ")
print("Welcome, ", player_1)

time.sleep(2)

player_2 = input("Now, player 2, please input your name: ")
print("Welcome, ", player_2)
time.sleep(2)

print("Now it's time to guess the number.")
#number starts
Guess = 1
player_1Guess = 0
player_2Guess = 0

time.sleep(1)

while player_1Guess != randNum and player_2Guess != randNum:
	if Guess == 1:
		#first player guess
		print(player_1)
		time.sleep(1)
		player_1Guess = int(input("Give me a number between 1 and 100: "))

		if player_1Guess > randNum:
			print("sorry,", player_1," thats too high, try again")

		elif player_1Guess < randNum:
			print("sorry,", player_1," thats too low, try again")

		elif player_1Guess == randNum:
			print("You did it, the number was ", randNum, "now for your reward.")
			time.sleep(5)
			print("lol fuk u")
			break

	Guess = 2
	#second player Guesses
	if Guess == 2:
		print(player_2)
		time.sleep(1)
		player_2Guess = int(input("Give me a number between 1 and 100: "))

		if player_2Guess > randNum:
 			print("sorry,", player_2," thats too high, try again")

		elif player_2Guess < randNum:
			print("sorry,", player_2," thats too low, try again")

		elif player_2Guess == randNum:
			print("You did it, the number was ", randNum)
			print("You win", player_2,"now for your reward.")
			time.sleep(5)
			print("lol fuk u")
			break
	Guess = 1

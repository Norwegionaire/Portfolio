import time

cart_items = []
cart_cost = 0

fruit = {"banana": [0.3, 150],"apple":[0.6, 100], "Melon":[1.5, 60], "Orange":[0.5, 100], "Dragonfruit":[5.9, 20]}


while True:

	purchase = input("What would you like to buy?(press q to finish) :") .lower()
	if purchase == "q":
		break
	elif purchase in fruit:
		price = fruit[purchase][0]
		stock = fruit[purchase][1]
		amount = int(input("How much do you want to buy?: "))
		print("The price of ", purchase.capitalize() ,"is", price, "dollars per kilo.")
		cart_cost = (price*amount)
		purchased = stock
		stock = purchased - amount
		cart_items.append(purchase)
	else:
		print("this Item is not available in our store")


if cart_items == []:
	print("fuck off")
else:
	print("Your total is", cart_cost,"and the price has been deduced from your bank account, have a nice day")

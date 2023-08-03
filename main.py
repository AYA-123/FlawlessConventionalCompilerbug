# List 5 products with costs - Good aesthetics
# Welcome to Tesco etc.
# List products continually to user
# Y to continue, X to exit etc

from beautifultable import BeautifulTable
import os
import pyfiglet
from termcolor import colored




products = {"1":["Apple",2],
		   "2":["Banana",1],
		   "3":["Cake",7],
		   "4":["Pineapple",2],
		   "5":["Milk",10]}
Cart = []

rows = []
for j in range(len(products)):
	l = j+1
	rows.append(str(l))

table = BeautifulTable()
for i in range(len(products)):
	k = i+1
	k = str(k)
	i = int(i)
	table.rows.append(products[k])

table.columns.header = ["Item", "Price"]
table.rows.header = rows
table.set_style(table.STYLE_SEPARATED)

Welcome = pyfiglet.figlet_format("Welcome to Tesco's!", font = "banner3-D")
Welcome = colored(Welcome, 'blue')
print(Welcome)

def ListingProduct():
	global table
	return table
def ItemChoice():
	os.system('clear')
	print(ListingProduct())
	Ichoice = int(input('Which item do you want to buy [Enter a number from 1 to 5]? '))
	while Ichoice <1 or Ichoice >5:
		print('Invalid input - please try again:')
		Ichoice = int(input('Which item do you want to buy [Enter a number from 1 to 5]? '))
	return Ichoice
def ListingCart():
	global Cart

	
	SCTrows = []
	for x in range(len(Cart)):
		y = x+1
		SCTrows.append(str(y))
		
	SCtable = BeautifulTable()	
	for z in range(len(Cart)):
		SCtable.rows.append(Cart[z])

	SCtable.columns.header = ["Item", "Price"]
	SCtable.rows.header = SCTrows

	# SCtable.rows[y] = ["Total Price: ", sum(list(table.columns["Price"]))]
	SCtable.rows.insert(y+1, ["", sum(list(SCtable.columns["Price"]))], header='Total: ')
	
	SCtable.set_style(SCtable.STYLE_SEPARATED)

	
	return SCtable
def Remove():
	global Cart
	os.system('clear')
	print(ListingCart())
	RmItems = int(input("Do you want to remove any items? [Enter the number of the item in the left hand side of the cart] [Enter 0 to skip]: "))
	if RmItems <= (len(Cart)+1) and RmItems > 0:
		Cart.pop((RmItems-1))
		print(ListingCart())

	
	elif RmItems == 0:
		os.system('clear')
		return True
	
	Again = int(input("Do you want to remove any more items? [0 for yes or 1 for no]: "))
	while Again != 1 and Again != 0:
		os.system('clear')
		print("Invalid input - please try again: ")
		Again = int(input("Do you want to remove any more items? [0 for yes or 1 for no]: "))
	if Again == 0:
		Remove()
	elif Again == 1:
		print(ListingCart())
		return True
def choice():
	global Cart
	
	Shop = str(input("Do you want to go shopping [Y for yes/ X for no]? "))
	if Shop.lower() == "y":
		return True
	elif Shop.lower() == "x":
		print("Here is your cart + bill at the bottom: ")
		print(ListingCart())

		Remove()		

		os.system('clear')

		print(ListingCart())
		print("Thank you for visiting Tesco's")
		return False


GoShopping = choice()
def main():
	global GoShopping
	global Cart
	
	UsrChoice = str(ItemChoice())
	Cart.append(products[UsrChoice])

	print(ListingCart())
	
	GoShopping = choice()
	if GoShopping == True:
		main()


while GoShopping:
	main()

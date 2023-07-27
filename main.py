# List 5 products with costs - Good aesthetics
# Welcome to Tesco etc.
# List products continually to user
# Y to continue, X to exit etc

products = {"1":["Apple",2.00],
		   "2":["Banana",1.50],
		   "3":["Cake",7.00],
		   "4":["Pineapple",2.50],
		   "5":["Milk",10.00]}

print("The products in this store are:")
for i in range(1,len(products)+1):
	i = str(i)
	print(products[i])

control = True

while control:
	Shop = str(input(print("Do you want to go shopping [Y for yes/ X for no]? "))).strip().lower()
	if Shop == "y":
		control = True
	elif Shop == "x":
		print("Thank you for visiting Tesco's")
		control = False


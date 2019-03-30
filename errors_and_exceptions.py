def prob1():
	try:
		for i in ['a', 'b', 'c']:
			print(i**2)
	except TypeError:
		print("The items in the list must all be integers")
	except:
		print("All other exceptions...")

def prob2():
	x = 5
	y = 0

	try:
		z = x / y
	except ZeroDivisionError:
		print("Cannot divide by zero!")
	except:
		print("All other exceptions...")
	finally:
		print("All Done.")

def ask():
	while True:
		try:
			num = int(input("Please provide an integer: "))
		except:
			print("An error occured! Please try again!")
		else:
			print("Thank you, your number squared is: " + str(num**2))
			break
def main():
	prob1()
	prob2()
	ask()

main()

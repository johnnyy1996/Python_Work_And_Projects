import random

#Problem 1
#Create a generator that generates the squares of numbers up to some number N.

def gensquares(N):
	for i in range(N):
		yield i**2

#Problem 2
#Create a generator that yields "n" random numbers between a low and high number (that are inputs). 
#Note: Use the random library. For example:

def rand_num(low, high, n):
	for i in range(n):
		yield random.randint(low, high)

#Problem 3
#Use the iter() function to convert the string below into an iterator:

s = 'hello'
str_iter = iter(s)

#Problem 4
#Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.

#You would want to use a generator to avoid having an output that would take up a lot of memory if you only intend to iterate through it

#Extra Credit
#Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)

#It turns a list comprehension into a generator
def gencomp_func():
	my_list = [1,2,3,4,5]

	gencomp = (item for item in my_list if item > 3)

	for item in gencomp:
		print(item)

def main():
	for x in gensquares(10):
		print(x)

	print('\n')

	low = int(input("Please provide a low number: "))

	high = int(input("Please provide a high number: "))

	n = random.randint(low, high)

	for num in rand_num(low, high, n):
		print(num)

	print('\n')

	print(next(str_iter))
	print(next(str_iter))
	print(next(str_iter))
	print(next(str_iter))
	print(next(str_iter))

	print('\n')

	gencomp_func()

main()

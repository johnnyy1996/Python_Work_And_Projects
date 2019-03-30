def print_s_words():
	print("\nUse for, .split(), and if to create a Statement that will print out words that start with 's':\n")

	st = 'Print only the words that start with s in this sentence'

	for word in st.split():
		if word[0].lower() == 's':
			print(word)

def print_even_numbers():
	print("\nUse range() to print all the even numbers from 0 to 10.\n")
	print(list(range(0,11,2)))

def list_comprehension():
	print("\nUse a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.\n")
	print([num for num in range(1,51) if num % 3 == 0])

def even_word_length():
	print("\nGo through the string below and if the length of a word is even print \"even!\"\n")
	st = 'Print every word in this sentence that has an even number of letters'
	print("The following words have an even length:")
	for word in st.split():
		if len(word) % 2 == 0:
			print(word)

def fizzbuzz():
	print("\nWrite a program that prints the integers from 1 to 100. But for multiples of three print \"Fizz\" instead of the number, and for the multiples of five print \"Buzz\". For numbers which are multiples of both three and five print \"FizzBuzz\".\n")
	for num in range(1,101):
		if num % 3 == 0 and num % 5 == 0:
			print("FizzBuzz")
		elif num % 3 == 0:
			print("Fizz")
		elif num % 5 == 0:
			print("Buzz")
		else:
			print(num)

def first_letters():
	print("\nUse List Comprehension to create a list of the first letters of every word in the string below:\n")
	st = 'Create a list of the first letters of every word in this string'
	print([word[0] for word in st.split()])

def main():
	print_s_words()
	print_even_numbers()
	list_comprehension()
	even_word_length()
	fizzbuzz()
	first_letters()

main()

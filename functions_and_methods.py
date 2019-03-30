import math
import string

#Write a function that computes the volume of a sphere given its radius.
def vol(rad):
	return (4 * math.pi * math.pow(rad, 3)) / 3

#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
	if num in range(low, high+1):
		print(str(num) + " is in the range " + str(low) + " and " + str(high))
	else:
		print(str(num) + " is not the range " + str(low) + " and " + str(high))

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
	upper = 0
	lower = 0
	for letter in s:
		if letter.isupper():
			upper += 1
		elif letter.islower():
			lower += 1
	print("Original String : " + s)
	print("No. of Upper case characters : " + str(upper))
	print("No. of Lower case characters : " + str(lower))

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
	return list(set(lst))

#Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
	total = numbers[0]
	for num in numbers[1:]:
		total *= num
	return total

#Write a Python function that checks whether a passed in string is palindrome or not.
def palindrome(s):
	palindrome = s.split()
	for letter in range(0,len(palindrome)):
		palindrome[letter] = palindrome[letter].upper()
	return palindrome == palindrome[::-1]	

#Write a Python function to check whether a string is pangram or not.
def ispangram(str1, alphabet=string.ascii_lowercase):
	lst = list(alphabet)
	for letter in set(str1):
		if letter in lst:
			lst.pop(lst.index(letter))
	return len(lst) == 0

def main():
	print(vol(2))
	ran_check(5,2,7)
	up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
	print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
	print(multiply([1,2,3,-4]))
	print(palindrome('helleh'))
	print(ispangram("The quick brown fox jumps over the lazy dog"))

main()

#WARMUP SECTION

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(num1, num2):
	if num1 % 2 == 0 and num2 % 2 == 0:
		if num1 < num2:
			return num1
		else:
			return num2
	if num1 > num2:
		return num1
	return num2

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
def animal_crackers(twoWords):
	wordList = twoWords.split()
	if len(wordList) > 2:
		print("Parameter string must contain extactly two words")
		return
	if wordList[0][0].lower() == wordList[1][0].lower():
		return True
	else:
		return False

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(int1, int2):
	return (int1 + int2) == 20 or int1 == 20 or int2 == 20

#LEVEL 1 PROBLEMS

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
	name = name.capitalize()
	return name[:3] + name[3].upper() + name[4:]

#MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(sentence):
	return " ".join(sentence.split()[::-1])

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(num):
	return abs((num - 100)) <= 10 or abs((num - 200)) <= 10
	
#LEVEL 2 PROBLEMS

#FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
	for i in range(0, len(nums)-1):
		if nums[i:i+2] == [3,3]:
            		return True  
	return False

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
	newString = ''
	for letter in text:
		newString = newString + (letter*3)
	return newString

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
	if a and b and c not in range(1,12):
		return "Integers must be between 1 and 11"
	total = a + b + c
	if total <= 21:
		return total
	elif total > 21 and (a == 11 or b == 11 or c == 11):
		total = total - 10
		if total <= 21:
			return total
	return 'BUST'

#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
	total = 0
	flag = True
	if len(arr) == 0:
		return total
	for num in range(0, len(arr)):
		if arr[num] == 6:
			flag = False
		if arr[num] == 9:
			flag = True
			continue
		if flag:
			total = total + arr[num]
	return total

#CHALLENGING PROBLEMS

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
	code = [0,0,7,'x']
	for num in nums:
		if num == code[0]:
			code.pop(0)
	return len(code) == 1	

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):
	primes = [2]
	x = 3
	if num < 2:
		return 0
	while x <= num:
		for y in range(3,x,2):
			if x % y == 0:
				x += 2
				break
		else:
			primes.append(x)
			x += 2
	return len(primes)

#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
def print_big(letter):
	patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
	alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
	for pattern in alphabet[letter.upper()]:
		print(patterns[pattern])

def main():
#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5
	print(lesser_of_two_evens(2,4))
	print(lesser_of_two_evens(2,5))
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
	print(animal_crackers('Levelheaded Llama'))
	print(animal_crackers('Crazy Kangaroo'))
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False
	print(makes_twenty(20,10))
	print(makes_twenty(12,8))
	print(makes_twenty(2,3))
#old_macdonald('macdonald') --> MacDonald
	print(old_macdonald('macdonald'))
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'
	print(master_yoda('I am home'))
	print(master_yoda('We are ready'))
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True
	print(almost_there(90))
	print(almost_there(104))
	print(almost_there(150))
	print(almost_there(209))
#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False
	print(has_33([1, 3, 3]))
	print(has_33([1, 3, 1, 3]))
	print(has_33([3, 1, 3]))
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
	print(paper_doll('Hello'))
	print(paper_doll('Mississippi'))
#blackjack(5,6,7)
#blackjack(9,9,9)
#blackjack(9,9,11)
	print(blackjack(5,6,7))
	print(blackjack(9,9,9))
	print(blackjack(9,9,11))
#summer_69([1, 3, 5])
#summer_69([4, 5, 6, 7, 8, 9])
#summer_69([2, 1, 6, 9, 11])
	print(summer_69([1, 3, 5]))
	print(summer_69([4, 5, 6, 7, 8, 9]))
	print(summer_69([2, 1, 6, 9, 11]))
#spy_game([1,2,4,0,0,7,5])
#spy_game([1,0,2,4,0,5,7])
#spy_game([1,7,2,0,4,5,0])
	print(spy_game([1,2,4,0,0,7,5]))
	print(spy_game([1,0,2,4,0,5,7]))
	print(spy_game([1,7,2,0,4,5,0]))
#count_primes(100) --> 25
	print(count_primes(100))
#print_big('a')
	print_big('a')

main()

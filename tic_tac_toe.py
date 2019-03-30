import random

def display_board(board):
	print('\n'*100)
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-----')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-----')
	print(board[1] + '|' + board[2] + '|' + board[3])
	
def player_input():
	'''
	OUTPUT = (Player 1 marker, Player 2 marker)
	'''

	marker = ''

	while marker.upper() not in ('X', 'O'):
		marker = input("Player 1, would you like to be 'X' or 'O': ").upper()

	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

def place_marker(board, marker, position):
	board[position] = marker

def win_check(board, mark):
	return(
		board[7] == board[8] == board[9] == mark or \
		board[4] == board[5] == board[6] == mark or \
		board[1] == board[2] == board[3] == mark or \
		board[1] == board[5] == board[9] == mark or \
		board[3] == board[5] == board[7] == mark or \
		board[1] == board[4] == board[7] == mark or \
		board[2] == board[5] == board[8] == mark or \
		board[3] == board[6] == board[9] == mark)

def choose_first():
	print("Flipping coin...")
	ran = random.randint(0,1)

	if ran == 0:
		return "Player 1"
	else:
		return "Player 2"

def space_check(board, position):
	return board[position] == ' '

def full_board_check(board):
	if " " in board[1:]:
		return False
	return True

def player_choice(board):
	position = 0
	while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and not space_check(board, int(position)):
		position = input("Choose a position: (1 - 9) ")
		if position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			print("Please enter a valid input")
			position = 0
		
		elif not space_check(board, int(position)):
			print("That position is taken")
			position = 0

	return int(position)

def replay():
	answer = ''

	while answer not in ('yes', 'no'):
		answer = input("Would you like to play again? (yes or no) ")
		answer = answer.lower()

		if answer == 'yes':
			return True
		elif answer == 'no':
			return False
		else:
			print("Please enter an appropriate answer")

def main():
	print('Welcome to Tic Tac Toe!')

	while True:
		#Game setup
		board = ['#'] +[' ']*9
		player1, player2 = player_input()
		turn = choose_first()
		print(turn + " will go first")
		ready = ''
		while ready not in ('yes', 'no'):
			ready = input("Begin? (yes or no) ").lower()	
		if ready == 'yes':
			game_on = True
		elif ready == 'no':
			game_on = False
			break

		while game_on:
			if turn == 'Player 1':
				#Player1's Turn
				display_board(board)
				print(turn + "'s Turn")
				position = player_choice(board)
				place_marker(board, player1, position)
				if win_check(board, player1):
					display_board(board)
					print(turn + " wins!")
					break
				if full_board_check(board):
					display_board(board)
					print("It's a tie")
					break
				turn = 'Player 2'
			else:
				#Player2's Turn
				display_board(board)
				print(turn + "'s Turn")
				position = player_choice(board)
				place_marker(board, player2, position)
				if win_check(board, player2):
					display_board(board)
					print(turn + " wins!")
					break
				if full_board_check(board):
					display_board(board)
					print("It's a tie!")
					break
				turn = 'Player 1'

		#Play again?
		if not replay():
			break

	print("Thanks for playing!")

main()  

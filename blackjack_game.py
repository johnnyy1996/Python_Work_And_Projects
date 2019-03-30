import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	
	def __str__(self):
		return "{0} of {1}".format(self.rank, self.suit)
		#return self.rank + " of " + self.suit

class Deck():
	def __init__(self):
		self.deck = []

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))

	def __str__(self):
		deck_str = ''

		for card in self.deck:
			deck_str += card.__str__() + '\n'

		return deck_str

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]

		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_aces(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

class Chips():
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("Bet Amount: "))
		
		except ValueError:
			print("Something went wrong...")
			print("Please try again")
		else:
			if chips.bet > chips.total:
				print("Insufficient chips!")
			else:
				print(str(chips.bet) + " chips were bet")
				break

def hit(deck, hand):
	hand.add_card(deck.deal())
	hand.adjust_for_aces()

def hit_or_stand(deck, hand):
	global playing

	decision = ''

	while decision not in ['hit', 'stand']:
		print('\n')
		decision = input("Hit or Stand: ").lower()

		if decision == 'hit':
			hit(deck, hand)

		elif decision == 'stand':
			playing = False

		else:
			print("Please provide an appropriate decision")

def show_some(player, dealer):
	print('\n')
	print("Dealer's Cards")
	print("*HIDDEN*")
	print(dealer.cards[1])

	print('\n')

	print("Player's Cards")
	for card in player.cards:
		print(card)

def show_all(player, dealer):
	print('\n')
	print("Dealer's Cards")
	for card in dealer.cards:
		print(card)
	print("Total value: " + str(dealer.value))

	print('\n')
	print("Player's Cards")
	for card in player.cards:
		print(card)
	print("Total Value: " + str(player.value))
	print('\n')

def player_busts(chips):
	print("BUST PLAYER!")
	chips.lose_bet()

def player_wins(chips):
	print("PLAYER WINS!")
	chips.win_bet()

def dealer_busts(chips):
	print("PLAYER WINS! DEALER BUSTED!")
	chips.win_bet()

def dealer_wins(chips):
	print("DEALER WINS!")
	chips.lose_bet()

def push():
	print("Dealer and player tie! PUSH")

def play_again():
	global playing

	print('\n')
	choice = ''
	options = ['yes', 'no']
	while choice not in options:
		choice = input("Play again? (Yes or no): ").lower()

		if choice not in options:
			print("Please provide an appropriate answer")

	if choice == 'no':
		return False

	playing = True
	return True

def main():
	chips = Chips()

	while chips.total > 0:
		print("********BLACKJACK********")

		deck = Deck()
		deck.shuffle()

		player = Hand()
		player.add_card(deck.deal())
		player.add_card(deck.deal())

		dealer = Hand()
		dealer.add_card(deck.deal())
		dealer.add_card(deck.deal())

		take_bet(chips)

		show_some(player, dealer)

		while playing:
			hit_or_stand(deck, player)

			show_some(player, dealer)

			if player.value > 21:
				player_busts(chips)
				show_all(player, dealer)
				break

		if player.value <= 21:
			while dealer.value < 17:
				hit(deck, dealer)

			show_all(player, dealer)

			if dealer.value > 21:
				dealer_busts(chips)

			elif player.value > dealer.value:
				player_wins(chips)

			elif player.value < dealer.value:
				dealer_wins(chips)

			else:
				push()

		print("Total Chips: " + str(chips.total))

		if not play_again():
			break
	
	if chips.total <= 0:
		print("\n" + "You are out of chips!")

	print("\n"  + "Thanks For Playing!")

main()

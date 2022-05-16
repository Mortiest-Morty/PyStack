import numpy as np

from Settings.constants import constants


class CardCombinations():
	def __init__(self):
		self.C = {}
		self.max_choose = 55
		self._init_choose()


	def _init_choose(self):
		''' init C(k,n) = n!/(k!(n-k)!) '''
		for i in range(0, self.max_choose+1):  # 0~55
			for j in range(0, self.max_choose+1):  # 0~55
				self.C[i*self.max_choose + j] = 0  # max_len: 3080

		for i in range(0,self.max_choose+1):
			self.C[i*self.max_choose] = 1  # C(0,n) = 1
			self.C[i*self.max_choose + i] = 1  # C(n,n) = 1

		for i in range(1,self.max_choose+1):  # 1~55  # e.g. 5
			for j in range(1,i+1):  # e.g. 1~5
				self.C[i*self.max_choose + j] = self.C[(i-1)*self.max_choose + j-1] + self.C[(i-1)*self.max_choose + j]  # C(k,n) = C(k-1,n-1) + C(k,n-1)


	def choose(self, n, k):
		''' returns C(k,n) = n!/(k!(n-k)!) '''
		return self.C[n*self.max_choose + k]


	def count_last_street_boards(self, street):
		'''
		@param: int :current street/round
		@return int :number of possible last round boards
		'''
		BCC, SC, CC = constants.board_card_count, constants.streets_count, constants.card_count
		used_cards = BCC[street-1]
		new_cards = BCC[SC-1] - BCC[street-1]
		return card_combinations.choose(CC - used_cards, new_cards)


	def count_next_street_boards(self, street):
		''' counts the number of boards in next street
		@param: int :current street/round
		@return int :number of all next round boards
		'''
		BCC, CC = constants.board_card_count, constants.card_count
		used_cards = BCC[street-1] # street-1 = current_street
		new_cards = BCC[street] - BCC[street-1]
		return card_combinations.choose(CC - used_cards, new_cards)


	def count_last_boards_possible_boards(self, street):
		''' counts the number of possible boards if 2 cards where already taken (in players hand)
			the answer will be the same for all player's holding cards
		@param: int :current street/round
		@return int :number of possible last round boards
		'''
		num_cards_on_board = constants.board_card_count[street-1]
		max_cards_on_board = constants.board_card_count[-1]
		max_cards_in_deck = constants.card_count
		num_cards_in_hand = constants.hand_card_count
		num_left_cards = max_cards_in_deck - num_cards_in_hand - num_cards_on_board
		num_cards_to_draw = max_cards_on_board - num_cards_on_board
		return self.choose(num_left_cards, num_cards_to_draw)


	def count_next_boards_possible_boards(self, street):
		''' counts the number of possible boards if 2 cards where already taken (in players hand)
			the answer will be the same for all player's holding cards
		@param: int :current street/round
		@return int :number of possible next round boards
		'''
		num_cards_on_board = constants.board_card_count[street-1] # has to be -1, because of indexing  e.g. 4
		num_cards_on_next_board = constants.board_card_count[street]  # 5
		max_cards_in_deck = constants.card_count
		num_cards_in_hand = constants.hand_card_count
		num_left_cards = max_cards_in_deck - num_cards_in_hand - num_cards_on_board
		num_cards_to_draw = num_cards_on_next_board - num_cards_on_board
		return self.choose(num_left_cards, num_cards_to_draw)




card_combinations = CardCombinations()

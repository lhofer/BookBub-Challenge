#!/usr/bin/python
# Filename: genredict.py

import itertools
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict

class genreDict(dict):
	def get_item(self, key):
		return self.__dict__[key]

	def add_item(self, key, item):
		self.__dict__.setdefault(key, []).append(item)

	'''GET GENRE FROM WORD'''
	def set_phrase(self, key, genre, score):
		self.keyword_list = []
		self.keyword_list = word_tokenize(key.strip())
		# 1. TWO PART KEYWORD: set dict at first keyword with reference to next included. 
		if len(self.keyword_list) > 1:
			self.add_item(self.keyword_list[0],(self.keyword_list[1], genre, score))
		# 2. ONE PART KEYWORD: set dict at keyword with reference to itself included.
		else:
			self.add_item(self.keyword_list[0],(key, genre, score))

	'''GET GENRE FROM WORD'''
	def get_genre(self,key,prev_two_words,next_two_words):
		self.return_genres = []
		# 1. GET GENRE OPTIONS: if key in dict, get list of genres linked to key word
		if key in self.__dict__.keys(): 
			for option in self.get_item(key):
				# 2. TWO PART KEYWORD: look for second keyword in next two words and word as counted
				if option[0] != key:
					if (option[0] in map(str,next_two_words)):
						self.return_genres.append([option[1],option[2]])
				else:
					self.return_genres.append([option[1], option[2]])
			return self.return_genres

# End of genredict.py
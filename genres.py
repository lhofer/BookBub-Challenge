#!/usr/bin/python
# Filename: genres.py
import sys
import csv
import json
import genredict
import re
from nltk.tokenize import sent_tokenize, word_tokenize
    
keyword_dict = genredict.genreDict()
book_genres = []

'''PARSE CSV'''
with open(sys.argv[1], 'rb') as csv_file:
    text = csv.reader(csv_file)
    # 1. ITERATE THROUGH ROWS
    for csv_row in text:
        genre, key_phrase, score = csv_row[0].strip(), csv_row[1].strip(), int(csv_row[2].strip()) 
        # 2. SET KEY PHRASE IN DICT
        keyword_dict.set_phrase(key_phrase,genre,score)

'''PARSE JSON'''
with open(sys.argv[2]) as json_file:    
    books = json.load(json_file)
    # 1. ITERATE THROUGH BOOKS
    for index,book in enumerate(books):
        return_genres, description = {}, re.findall(r'\w+|\S\w*', book['description']) #word_tokenize(book['description'])
        # 2. ITERATE THROUGH WORDS IN BOOK
        for word in description:
            prev_words = 0 if index == 0 else 1 if index == 1 else index-2
            # 3. GET LIST OF POSSIBLE GENRES
            possible_genres = keyword_dict.get_genre(word,description[prev_words:index], description[index+1:index+3])
            if possible_genres is None:
                possible_genres = []
            for genre_info in possible_genres:
                return_genres.setdefault(genre_info[0], []).append(genre_info[1])
        # 4. ADD RELEVANT GENRES TO TITLE
        if return_genres:
            genres = []
            for genre in return_genres.iteritems():
                genres.append([genre[0],sum(genre[1])/len(genre[1])])
            book_genres.append([book['title'],genres])

'''SORT AND PRINT'''
book_genres = sorted(book_genres, key=lambda book: sorted(book[1], key=lambda genre_score: genre_score[1]))
for book in book_genres:
    print book[0] + '\n'
    for genre in book[1]:
        print genre[0] + ': ' + str(genre[1]) + '\n'




from pprint import pprint

# dicts = ["verbs", "adjectives", "obscenes", "adverbs", "places", "peoples", "nouns"]
dicts = ["out"]

dictionaries = dict()




import os
def initDicts():
	for root, dirs, files in os.walk("./dictionaries/temp"):
		for file in files:
			if file.endswith(".txt"):
				path = os.path.join(root, file)
				filename = str(file)
				penn = filename.split('_')[0]
				for word in open(path, "r"):
					word = word.strip()

					if penn not in dictionaries:
						dictionaries[penn] = set()
					dictionaries[penn].add(word)





from textblob import TextBlob, Word
from nltk.corpus import words

available = dict()
def getWordsInSsid(ssid):
	# print "-"*10
	# print ssid
	len_ssid = len(ssid)

	for penn in dictionaries:
		for word in dictionaries[penn]:
			if word in ssid.lower():
				# print "\t\t", word, penn
				if penn not in available:
					available[penn] = dict()
				available[penn][word] = [1, ssid]



def printAvailable():
	pprint(available)

# 'Yes' if fruit == 'Apple' else 'No'
bla = False
n_list = []
b_list = ["-*_*_*_*_*_*_*_*_"]
import tracery
from tracery.modifiers import base_english

def build_sentence():
	rules = {
	    's1': '#nothing# #someone.a.capitalize# is normally #adjective# at #location.a#!',
	    's2': '#someone.capitalize# is #verb#ing at #location.a#.',
	    'verb': [verb for verb in available["VB"]],
	    'gerund': [gerund for gerund in available["VBG"]],
	    'adjective': [adj for adj in available["JJ"]],
	    'someone': [people for people in available["people"]],
	    'location': [l for l in available["places"]] if len(available["places"]) > 0 else b_list,
	    'nothing': n_list if len(n_list) > 0 else b_list

	}

	grammar = tracery.Grammar(rules)
	grammar.add_modifiers(base_english)
	print grammar.flatten("#s1#") # prints, e.g., "Hello, world!"





import json
from textblob import TextBlob, Word
from pprint import pprint

words_by_pos = dict()

rawjson = open("verbs_corpora.json").read()  #puts the file as a big string into the variable rawjson
data = json.loads(rawjson) #json.loads take a string and turns it into a data structure

for elem in data['verbs']:
	w = elem["present"]
	pos = TextBlob(w).tags[-1][1]
	if pos not in words_by_pos:
		words_by_pos[pos] = set()
	words_by_pos[pos].add(w)
	w = elem["past"]
	pos = TextBlob(w).tags[-1][1]
	if pos not in words_by_pos:
		words_by_pos[pos] = set()
	words_by_pos[pos].add(w)

for penn in words_by_pos:
	print penn
	writer = open(str(penn) + "_common4.txt", "w")
	for w in words_by_pos[penn]:
		print "\t\t", w
		writer.write(w)
		writer.write("\n")
		
		if penn.startswith("VB") and Word(w).lemmatize('v') is not w:
			print "\t\t\t\t\t", Word(w).lemmatize('v')
			writer.write(Word(w).lemmatize('v'))
			writer.write("\n")
		if penn.startswith("NN") and Word(w).lemmatize('n') is not w:
			print "\t\t\t\t\t", Word(w).lemmatize('n')
			writer.write(Word(w).lemmatize('n'))
			writer.write("\n")
		if penn.startswith("JJ") and Word(w).lemmatize('a') is not w:
			print "\t\t\t\t\t", Word(w).lemmatize('a')
			writer.write(Word(w).lemmatize('a'))
			writer.write("\n")
	writer.close()

from pprint import pprint

# dicts = ["verbs", "adjectives", "obscenes", "adverbs", "places", "peoples", "nouns"]
dicts = ["out"]

dictionaries = dict()






def initDicts():
	for cat in dicts:
		dictionaries[cat] = set()
		d = open("dictionaries/" + cat + ".txt", 'r')
		for line in d:
			line = line.strip()
			dictionaries[cat].add(line)

	# pprint(dictionaries)



from textblob import TextBlob, Word
from nltk.corpus import words
def getWordsInSsid(ssid):
	print "-"*10
	print ssid
	len_ssid = len(ssid)

	# for i in range(len_ssid):
	# 	for j in range(len_ssid - i):
	# 		ssidSlice = ssid[i:i+j+1]
	# 		if Word(ssidSlice).spellcheck()[0][1] == 1.0:
	# 			print ssidSlice, Word(ssidSlice).spellcheck()
	words_found = set()
	for word in dictionaries["out"]:
		if word in ssid.lower():
			print word, TextBlob(word).tags[0][1]
			words_found.add(word)




	# for cat in dicts:
	# 	for word in dictionaries[cat]:
	# 		if word in ssid.lower():
	# 			print word, cat
	# for word in words.words():
	# 	if word in ssid.lower():
	# 		print word







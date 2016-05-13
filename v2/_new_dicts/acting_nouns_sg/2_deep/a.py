import json
from textblob import TextBlob, Word
from pprint import pprint
from pattern.en import tag


words_by_pos = dict()

def add_word(w,pos):
	if pos not in words_by_pos:
		words_by_pos[pos] = set()
	words_by_pos[pos].add(w)

def count_types():
	for t in words_by_pos:
		print t, len(words_by_pos[t])

def print_type(startswith):
	for t in words_by_pos:
		if t.startswith(startswith):
			print "\n", "-"*50, t, "\n"
			pprint(words_by_pos[t])

def to_files():
	for t in words_by_pos:
		writer = open("out_files/" + str(t) + "_1.txt", "w")
		for w in words_by_pos[t]:
			print "\t\t", w
			writer.write(w)
			writer.write("\n")
	writer.close()
	print "[+] saved to files."

def to_files_special_dict(dict_name):
	writer = open("out_files/" + str(dict_name) + ".txt", "w")
	count = 0
	for t in words_by_pos:
		for w in words_by_pos[t]:
			print "\t\t", w
			try:
				writer.write(w)
				writer.write("\n")
				count += 1
			except:
				nevermind = 1
	writer.close()
	print "[+] saved to files. Saved", count, "words."

dicts = dict()
dicts["archetypes_characters_corpora"] = ["characters", "name"]




for d in dicts:
	rawjson = open(d + ".json").read()  #puts the file as a big string into the variable rawjson
	data = json.loads(rawjson) #json.loads take a string and turns it into a data structure
	for elem in data[dicts[d][0]]:
		w = elem[dicts[d][1]]

		pos = tag(w)[-1][1]
		# print "-"*20
		# print w, pos
		add_word(w,pos)

		if pos.startswith("VB") and Word(w).lemmatize('v') is not w:
			w = Word(w).lemmatize('v')
			pos = tag("to " + w)[-1][1]
			# print "-"*5
			# print w, pos
			add_word(w,pos)
		if pos.startswith("NN") and Word(w).lemmatize('n') is not w:
			w = Word(w).lemmatize('n')
			pos = tag(w)[-1][1]
			# print "-"*5
			# print w, pos
			add_word(w,pos)
		if pos.startswith("JJ") and Word(w).lemmatize('a') is not w:
			w = Word(w).lemmatize('a')
			pos = tag("a " + w + " thing")[-2][1]
			# print "-"*5
			# print w, pos
			add_word(w,pos)

count_types()
# pprint(words_by_pos)
# print_type("NNP-ORG")
# to_files()
to_files_special_dict("actorSG_1")

# 
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




# ----------------------------




rawjson = open("archetypes_settings_corpora.json").read()  #puts the file as a big string into the variable rawjson
data = json.loads(rawjson) #json.loads take a string and turns it into a data structure
for elem in data["settings"]:
	w = elem["name"]
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

	for s in elem["synonyms"]:
		w = s
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





# ----------------------------






rawjson = open("geography_us_cities.json").read()  #puts the file as a big string into the variable rawjson
data = json.loads(rawjson) #json.loads take a string and turns it into a data structure
for elem in data["cities"]:
	w = elem["city"]
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

	w = elem["state"]
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



# ----------------------------

rawjson = open("geography_venues_corpora.json").read()  #puts the file as a big string into the variable rawjson
data = json.loads(rawjson) #json.loads take a string and turns it into a data structure
for elem in data["categories"]:
	w = elem["name"]
	# print w

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

	if "categories" in elem:
		for e in elem["categories"]:
			w = e["name"]
			# print "\t", w
			
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

			if "categories" in e:
				for x in elem["categories"]:
					w = x["name"]
					# print "\t\t", w

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


					if "categories" in x:
						for z in x["categories"]:
							w = z["name"]
							# print "\t\t\t", w

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

					


# ----------------------------




rawjson = open("planets_corpora.json").read()  #puts the file as a big string into the variable rawjson
data = json.loads(rawjson) #json.loads take a string and turns it into a data structure
for elem in data["planets"]:
	w = elem["name"]
	# print w

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



# pprint(words_by_pos)
count_types()
to_files_special_dict("places2")












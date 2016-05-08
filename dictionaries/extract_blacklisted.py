# put all the names of dictionairies to combine in this list:
# e.g. '["verbs1", "verbs2"]'
inputdicts = ["adjectives", "adverbs", "nouns", "obscenes", "peoples", "places", "verbs"]

write = True

count = 0
for d in inputdicts:
	if(write): writer = open("after_blacklist_cp/" + d + ".txt", 'w')
	for word in open("pre_blacklist/" + d + ".txt", "r"):
		word = word.strip()
		black = False
		for blackword in open("blacklist.txt", "r"):
			blackword = blackword.strip()
			if word == blackword:
				print "found in " + d + ":"
				print word
				print blackword + " <-- removed."
				
				black = True
			# else:
				# if(write): writer.write(word)
				# if(write): writer.write("\n")
		if(not black and write): writer.write(word)
		if(not black and write): writer.write("\n")
	if(write): writer.close()

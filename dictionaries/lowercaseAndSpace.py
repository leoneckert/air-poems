# put all the names of dictionairies to combine in this list:
# e.g. '["verbs1", "verbs2"]'
inputdicts = ["adjectives", "adverbs", "nouns", "obscenes", "peoples", "places", "verbs"]
# inputdicts = ["peoples_combined"]

#before: 168269 words
count = 0
for d in inputdicts:
	writer = open(d + "_lower_and_space.txt", "w")
	for word in open(d + ".txt", "r"):
		word = word.strip()
		
		# print word
		word = word.lower()
		writer.write(word)
		count += 1
		writer.write("\n")
		if len(word.split(" ")) > 1:
			# print word
			# print "".join(word.split(" "))
			writer.write("".join(word.split(" ")))
			count += 1
			writer.write("\n")


	writer.close()
print count

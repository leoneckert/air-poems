# put all the names of dictionairies to combine in this list:
# e.g. '["verbs1", "verbs2"]'
inputdicts = ["countries_corpora_formatted", "places1", "rooms_corpora_formatted", "setting_corpora_formatted", "us_cities_states_formatted", "venues_corpora_formatted"]



outputName = "_".join(inputdicts) + "_combined.txt"

print "\n[+] Cobining dicionairies:"
output = list()
totalinputcount = 0
for d in inputdicts:
	count = 0
	for word in open(d + ".txt", "r"):
		word = word.strip()
		# print word
		output.append(word)
		count += 1
	print d + ".txt has " + str(count) + " words." 
	totalinputcount += count

#uniquify:
outputUni = set(output)
output = list(outputUni)

writer = open(outputName, "w")
countNew = 0
for w in sorted(output):
	writer.write(w)
	writer.write("\n")
	countNew += 1
writer.close()

print "\n" + outputName + " has " + str(countNew) + " WORDS."
print "--> there were " + str(totalinputcount - countNew) + " DUPLICATS in the input-dictionairies.\n"
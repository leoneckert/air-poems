import os
import time
from pprint import pprint
import conjugate

# count_all = 0

output_list = dict()

order = ["verbInf", "verbThird", "verbGer", "verbPast"]

for root, dirs, files in os.walk("."):
	for file in files:
		if file.endswith(".txt") and not file.startswith("_"):
			filename = str(file)
			penn = filename.split('_')[0]
			print "--\n", filename, penn

			for word in open(filename, "r"):
				word = word.strip()
				w1 = conjugate.inf(word)
				w2 = conjugate.third(word)
				w3 = conjugate.gerund(word)
				w4 = conjugate.past(word)

				word_forms = {"verbInf": w1, "verbThird": w2, "verbGer": w3, "verbPast": w4}

				for f in order:
					if f not in output_list:
						output_list[f] = set()
					output_list[f].add(word_forms[f])




for form in output_list:
	list_to_export = set()
	print form
	# lowercase
	lowercased = set()
	for word in output_list[form]:
		# print word
		lowercased.add(word.lower())
	# pprint(lowercased)

	len_before = 0
	spacified = set()
	for line in lowercased:
		spacified.add(line)
		len_before += 1
		if len(line.split()) > 1:
			spacified.add("".join(line.split()))
			
	# print "spacify - length", len_before, len(spacified)

	for line in spacified:
		list_to_export.add(line)


	list_to_export = list(list_to_export)

	currentDateForIndexing = time.strftime("%x")[6:] + time.strftime("%x")[:2] + time.strftime("%x")[3:-3]
	writer = open("_" + form + "_" + str(currentDateForIndexing) + ".txt", "w")
	count = 0
	for name in sorted(list_to_export):
		# print name
		writer.write(name)
		count += 1
		writer.write("\n")
	writer.close()
	print "--\n", "[+] merged and processed all names of above files."
	print "[+] saved into _" + form + "_" + str(currentDateForIndexing) + ".txt"
	print "[+] number of names in final file:", count


import os
import time
from pprint import pprint

# count_all = 0

output_list = set()

for root, dirs, files in os.walk("."):
	for file in files:
		if file.endswith(".txt") and not file.startswith("_"):
			filename = str(file)
			penn = filename.split('_')[0]
			print "--\n", filename, penn

			# lowercase
			lowercased = set()
			for line in open(filename, "r"):
				line = line.strip()
				lowercased.add(line.lower())
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
				output_list.add(line)
			# print len(output_list)
			# pprint(output_list)


output_list = list(output_list)

currentDateForIndexing = time.strftime("%x")[6:] + time.strftime("%x")[:2] + time.strftime("%x")[3:-3]
writer = open("_citiesCountries_" + str(currentDateForIndexing) + ".txt", "w")
count = 0
for name in sorted(output_list):
	# print name
	writer.write(name)
	count += 1
	writer.write("\n")
writer.close()
print "--\n", "[+] merged and processed all names of above files."
print "[+] saved into _citiesCountries_" + str(currentDateForIndexing) + ".txt"
print "[+] number of names in final file:", count


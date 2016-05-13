import os

count_all = 0

for root, dirs, files in os.walk("."):
	for file in files:
		if file.endswith(".txt") and len(dirs) == 1:
			filename = str(file)
			penn = filename.split('_')[0]
			print "--\n",filename, penn

			# make unique:

			len_before = 0
			unique = set()
			for line in open(filename, "r"):
				line = line.strip()
				unique.add(line)
				len_before += 1
			print "uniquify - length", len_before, len(unique)

			# unique: check
			
			# make version with and without space
			len_before = 0
			spacified = set()
			for line in unique:
				spacified.add(line)
				len_before += 1
				if len(line.split()) > 1:
					spacified.add("".join(line.split()))
			print "spacify - length", len_before, len(spacified)


			# spacified: check
			lowercased = list()
			for line in spacified:
				# print line.lower()
				lowercased.append(line.lower())
			
			writer = open("_uniquified_spacified_lowercased/" + penn + "_formatted.txt", "w")
			for word in sorted(lowercased):
				print "\t", word
				count_all += 1
				writer.write(word)
				writer.write("\n")
			writer.close()








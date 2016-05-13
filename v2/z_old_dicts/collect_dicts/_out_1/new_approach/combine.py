import os

first = True
currentPenn = ""
loop = 0

for root, dirs, files in os.walk("."):
	for file in files:
		if file.endswith(".txt") and len(dirs) == 1:


			filename = str(file)
			penn = filename.split('_')[0]
			# print dirs, len(dirs), filename, penn, currentPenn


			
			if first is True:
				currentPenn = penn
				writer = open("_combined/" + penn + "_combined.txt", "w") 

			# print filename, penn, currentPenn

			if penn != currentPenn:
				if not first:
					writer.close()
					loop = 0
					print "[-] closing pen-tag:", currentPenn
				currentPenn = penn
				writer = open("_combined/" + penn + "_combined.txt", "w") 

			print "[+] loop", loop, "on penn-tag:", currentPenn
			for line in open(filename, "r"):
				line = line.strip()
				# print "\t", line
				writer.write(line)
				writer.write("\n")
			loop += 1
			first = False

writer.close()

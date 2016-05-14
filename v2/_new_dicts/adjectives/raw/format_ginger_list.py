writer = open('ginger_list_formatted.txt', 'w')

for line in open('list_ginger_software_grammar.txt', 'r'):
	line = line.strip()
	for word in line.split():
		print word
		writer.write(word)
		writer.write("\n")

writer.close()
# blackListExtendMode = False
blackListExtendMode = True

def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

    return int(cr[1]), int(cr[0])


import time
def printp(poetry_data):
	t_width = getTerminalSize()[0]
	t_height = getTerminalSize()[1]

	indexForPoem = -1
	indexLog = open("index_count.log", "r")
	indexLog_line =  indexLog.read()
	indexLog.close()
	indexLog_elems = indexLog_line.split(" ")
	currentDateForIndexing = time.strftime("%x")[6:] + time.strftime("%x")[:2] + time.strftime("%x")[3:-3]
	indexLog = open("index_count.log", "w")
	if indexLog_elems[0] == currentDateForIndexing:
		indexForPoem = int(indexLog_elems[1]) + 1
		indexLog.write(currentDateForIndexing + " " + str(indexForPoem))
		indexLog.close()
	else:
		indexForPoem = 1
		indexLog.write(currentDateForIndexing + " " + str(indexForPoem))
		indexLog.close()


	# print str(currentDateForIndexing) + str(indexForPoem)
	poem_index = "#" + str(currentDateForIndexing) + str(indexForPoem)
	# print " "*(t_width/2 - len(poem_index)/2), poem_index

	
	line_length_of_poem = (len([d for d in poetry_data if len(d) is 5])*2 + 3)
	# print line_length_of_poem
	lines_top_print = t_height/2 - line_length_of_poem/2 - 1
	for i in range(lines_top_print):
		if i is lines_top_print - 3:
			print " "*(t_width/2 - len(poem_index)/2), poem_index
		else:
			print " "*(t_width/2), "|"

	# print " "*(t_width/2), "|", "\n"
	print ""
	for d in poetry_data:

		if len(d) is 5:
			print " "*(t_width/2 - d[3]),
			if blackListExtendMode is True:
				print d[2], "[" + str(d[0]) + "#" + str(d[1]) + "]"
			else:
				print d[2]
	print "\n", " "*(t_width/2), "|", "\n"
	# print "-"

	first = True
	chunks_to_print = list()
	string_to_prepend = ""
	c = 0
	for d in poetry_data:
		if len(d) is 1:
			if first:
				string_to_prepend = "[" + d[0] + "]"
			else:
				filler_elems = d[0].split()
				if len(filler_elems) > 1:		
					if c is len(poetry_data) - 1:
						chunks_to_print[len(chunks_to_print)-1][0] = chunks_to_print[len(chunks_to_print)-1][0] + " [" + " ".join(filler_elems) + "]"
					else:
						cut_filler_here = len(filler_elems)/2
						chunks_to_print[len(chunks_to_print)-1][0] = chunks_to_print[len(chunks_to_print)-1][0] + " [" + " ".join(filler_elems[:cut_filler_here]) + "]"
						string_to_prepend = "[" + " ".join(filler_elems[cut_filler_here:]) + "]"
				else:
					chunks_to_print[len(chunks_to_print)-1][0] = chunks_to_print[len(chunks_to_print)-1][0] + " [" + filler_elems[0] + "]"



		elif len(d) is 5:
			word = d[0]
			penn = d[1] 
			ssid = d[2]
			start_idx = d[3] 
			end_idx = d[4] 
			string_to_print = ssid[start_idx:end_idx]
			offset = 0

			if len(string_to_prepend) > 0:
				offset = len(string_to_prepend) + 1
				string_to_print = " ".join([string_to_prepend, string_to_print])
				string_to_prepend = ""
			chunks_to_print.append([string_to_print, offset])


		c += 1
		first = False
	# if len(string_to_prepend) > 0:

	# print chunks_to_print
	for d in chunks_to_print:
		print " "*(t_width/2 - d[1]),
		print d[0]



	print ""
	for i in range(t_height/2 - line_length_of_poem/2 - 1):
		print " "*(t_width/2), "|"
	# print "\n", " "*(t_width/2), "|", "\n"


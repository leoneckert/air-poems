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


def printp(poetry_data):
	t_width = getTerminalSize()[0]

	print " "*(t_width/2), "|", "\n"
	# print 
	for d in poetry_data:
		if len(d) is 5:
			print " "*(t_width/2 - d[3]),
			print d[2]
	print "\n", " "*(t_width/2), "|", "\n"
	# print "-"

	first = True
	chunks_to_print = list()
	string_to_prepend = ""
	for d in poetry_data:
		if len(d) is 1:
			if first:
				first = False
				string_to_prepend = "[" + d[0] + "]"
			filler_elems = d[0].split()
			if len(filler_elems) > 1:
				# print filler_elems

				cut_filler_here = len(filler_elems)/2
				
				chunks_to_print[len(chunks_to_print)-1][0] = chunks_to_print[len(chunks_to_print)-1][0] + " [" + " ".join(filler_elems[:cut_filler_here]) + "]"
				# print chunks_to_print[len(chunks_to_print)-1][0]
				# print filler_elems[:cut_filler_here]

				string_to_prepend = "[" + " ".join(filler_elems[cut_filler_here:]) + "]"


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

	# print chunks_to_print
	for d in chunks_to_print:
		print " "*(t_width/2 - d[1]),
		print d[0]

	print "\n", " "*(t_width/2), "|", "\n"


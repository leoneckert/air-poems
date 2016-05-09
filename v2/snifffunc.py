def routerIsNull(line):
	elems = line.split(',')
	if len(elems) == 4:
		s = str(elems).split(",")[3]
		if s.startswith(" '\\x00"):
			return True
	return False

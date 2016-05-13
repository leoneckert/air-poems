import syssniff
import snifffunc
import poetfunc
from pprint import pprint


import string

printable = set(string.printable)




seenBefore = set()
# this function is called everytime a new frame is captured:
def sniffing_handler(line):
	if snifffunc.routerIsNull(line):
		return
	elems = line.split(',')
	if len(elems) == 4:
		timestamp = elems[0]
		request_type = elems[1]
		MAC = elems[2]
		ssid = elems[3]
		# print ssid
		ssid  = filter(lambda x: x in printable, ssid)
		if ssid not in seenBefore:
			# ssid  = filter(lambda x: x in printable, ssid)
			seenBefore.add(ssid)
			poetfunc.getWordsInSsid(ssid)
			# print ssid
			# for l in ssid:
			# 	print l
			# print "\t\t", filter(lambda x: x in printable, ssid)







def Main():  
	poetfunc.initDicts()
	# poetfunc.printDictionairies()
	syssniff.sniffloop(sniffing_handler)

	# poetfunc.printAvailable()
	# for i in range(30):
	# 	poetfunc.build_sentence()
	# 	poetfunc.build_sentence()
	# 	poetfunc.build_sentence()
	# 	poetfunc.build_sentence()
	# 	poetfunc.build_sentence()


if __name__ == '__main__':
    Main()

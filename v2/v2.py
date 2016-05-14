import syssniff
import snifffunc
import poetfunc
from pprint import pprint
import string


printable = set(string.printable)
def formatSSID(ssid):
	ssid = filter(lambda x: x in printable, ssid)
	ssid = ssid.strip('#')
	return ssid


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

		ssid = formatSSID(ssid)

		if ssid not in seenBefore:
			seenBefore.add(ssid)
			poetfunc.getWordsInSsid(ssid)








def Main():  
	poetfunc.initDicts()
	# poetfunc.printDictionairies()
	syssniff.sniffloop(sniffing_handler)

	# poetfunc.printAvailable()


if __name__ == '__main__':
    Main()

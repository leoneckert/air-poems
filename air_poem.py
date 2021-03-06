import sys
import time
import random
import subprocess
from pprint import pprint


                                          
#   ___ ___  _ __ ___  _ __   __ _ _ __ ___ 
#  / __/ _ \| '_ ` _ \| '_ \ / _` | '__/ _ \
# | (_| (_) | | | | | | |_) | (_| | | |  __/
#  \___\___/|_| |_| |_| .__/ \__,_|_|  \___|
#                     | |                   
#                     |_|          
#                        _     
#                       | |    
# __      _____  _ __ __| |___ 
# \ \ /\ / / _ \| '__/ _` / __|
#  \ V  V / (_) | | | (_| \__ \
#   \_/\_/ \___/|_|  \__,_|___/
                             

#------------------------------------------------------------
# run time increases a lot with longer networknames (->perhaps only allow below a threshold)
def check_if_part_of_word1_equals_word2(word1, word2, min_length):
	match = ""
	word1Length = len(word1)
	requiredLength = min_length

	for i in range(word1Length):
		for j in range(word1Length - i):
			word1slice = word1[i:i+j+1]
			# print word1slice
			if word1slice == word2 and len(word2) > requiredLength:
				# print word1
				# print word2
				requiredLength = len(word2)
				match = word2
	return match
# #------------------------------------------------------------

#  _                   _             
# | |                 (_)            
# | | ___   ___  _ __  _ _ __   __ _ 
# | |/ _ \ / _ \| '_ \| | '_ \ / _` |
# | | (_) | (_) | |_) | | | | | (_| |
# |_|\___/ \___/| .__/|_|_| |_|\__, |
#               | |             __/ |
#               |_|            |___/ 
#      _ _      _   _                   _      _           
#     | (_)    | | (_)                 (_)    (_)          
#   __| |_  ___| |_ _  ___  _ __   __ _ _ _ __ _  ___  ___ 
#  / _` | |/ __| __| |/ _ \| '_ \ / _` | | '__| |/ _ \/ __|
# | (_| | | (__| |_| | (_) | | | | (_| | | |  | |  __/\__ \
#  \__,_|_|\___|\__|_|\___/|_| |_|\__,_|_|_|  |_|\___||___/
                                                         

#------------------------------------------------------------
# all dictionairies need to be named in plural (ending on "s", e.g. "peoples").
# the order in the next list matters: it will always take the longest corresponding word,
# however, if two are the same length, the one from the earlier dictionairy will be taken
dictionaries = [ "verbs", "adjectives", "obscenes", "adverbs", "places", "peoples", "nouns"]



# there can be more than one match, we want the longest one
def check_for_words_in_network_name(_network_name):
	networkname = _network_name.lower()
	longestmatch = list()
	longestmatch.append("") #actual match
	longestmatch.append("") #type

	# count = 0
	for d in dictionaries:
		dictionairy = open("dictionaries/" + d + ".txt", 'r')
		for elem in dictionairy:
			elem = elem.strip()
			matchingWord = check_if_part_of_word1_equals_word2(networkname,elem,len(longestmatch[0]))
			if len(matchingWord) > 0:
				longestmatch[0] = matchingWord
				# longestmatch[1] = dictionaries[count][:-1]
				longestmatch[1] = d[:-1]
		# count += 1	
	return longestmatch


#------------------------------------------------------------
# this function expects an array of wordtypes as an input. These are seperated by [space] 
# and expressed as the singular form of the dictionairy name
# (e.g. "["people verb people adverb")

#unused collects networknames and correspinding words that have been found but not used in a senteence yet
unused = dict() 
for d in dictionaries:
	dictName = d[:-1]
	unused[dictName] = dict()

def returnElements(elementListSpaceDivided):
	outputList = list()
	elems = elementListSpaceDivided.split(" ")
	#count how many of each element we need
	requiredDic = dict()
	for elem in elems:
		if elem in requiredDic:
			requiredDic[elem] += 1
		else:
			requiredDic[elem] = 0

	hasAll = True
	for elemType in requiredDic:
		if len(unused[elemType]) <= requiredDic[elemType]:
			hasAll = False
			break
	
	if(hasAll): 
		for elem in elems:
			randomNetworkName = random.sample(unused[elem], 1)[0]
			# print randomNetworkName
			correspodingWord = unused[elem].pop(randomNetworkName)
			# print correspodingWord
			resultElem = list()
			resultElem.append(randomNetworkName)
			resultElem.append(correspodingWord)
			outputList.append(resultElem)
		return outputList
	else:
		return outputList #test empty returns true


#             _       _                                
#            (_)     | |                               
#  _ __  _ __ _ _ __ | |_   _ __   ___   ___ _ __ ___  
# | '_ \| '__| | '_ \| __| | '_ \ / _ \ / _ \ '_ ` _ \ 
# | |_) | |  | | | | | |_  | |_) | (_) |  __/ | | | | |
# | .__/|_|  |_|_| |_|\__| | .__/ \___/ \___|_| |_| |_|
# | |                      | |                         
# |_|                      |_|                         

# this function expects a list of elements (constructed by the returnElements function) 
# and a list of integers. The integer pattern list describes the pattern in which the elements
# are goning to be printed. number describe word on a line, lines are comma seperated
# eg. "[1,2,1]" means the poem will have 3 line with 1 element on the first line etc.
# the whole thing will be printed twice, one time with network names, another time with correspinaing words
def printNewPoem(parts, _pattern):
	#sort out indexing:
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
	
	if(sys.argv[1] > 0):
		outPutLog_filename = sys.argv[1]
	else:
		outPutLog_filename = "poems_gen_output"
	outPutLog = open("logged_poems/" + outPutLog_filename + ".log", "a")
	print "-"*30
	outPutLog.write("-"*30 + "\n")
	print "\n\n\n\tNew Air Poem - " + str(currentDateForIndexing) + str(indexForPoem) + "\n\n\n"
	outPutLog.write("\n\n\n\tNew Air Poem - " + str(currentDateForIndexing) + str(indexForPoem) + "\n\n\n" + "\n")


	for i in range(2): #for networknames and words
		count = 0
		for line in range(len(_pattern)): #for each line
			print "\t",
			outPutLog.write("\t")
			for word in range(_pattern[line]):
				print parts[count][i],
				outPutLog.write(parts[count][i] + " ")
				count += 1
			print ""
			outPutLog.write("\n")
		print ""
		outPutLog.write("\n")
	print "\n\n"
	outPutLog.write("\n\n")
	print "\t\textracted from air,"
	outPutLog.write("\t\textracted from air," + "\n")
	print "\t\t" + time.strftime("%A") + ", " + time.strftime("%B") + " " + time.strftime("%d") + " " + time.strftime("%Y") + ", " + time.strftime("%X")
	outPutLog.write("\t\t" + time.strftime("%A") + ", " + time.strftime("%B") + " " + time.strftime("%d") + " " + time.strftime("%Y") + ", " + time.strftime("%X"))
	print "\n\n"
	outPutLog.write("\n\n\n\n")			
	print "-"*30
	outPutLog.write("-"*30 + "\n")
	outPutLog.close()

#                      _                   _   
#                     | |                 | |  
#   ___ ___  _ __  ___| |_ _ __ _   _  ___| |_ 
#  / __/ _ \| '_ \/ __| __| '__| | | |/ __| __|
# | (_| (_) | | | \__ \ |_| |  | |_| | (__| |_ 
#  \___\___/|_| |_|___/\__|_|   \__,_|\___|\__|                                                                                         
#                 _                           
#                | |                          
#  ___  ___ _ __ | |_ ___ _ __   ___ ___  ___ 
# / __|/ _ \ '_ \| __/ _ \ '_ \ / __/ _ \/ __|
# \__ \  __/ | | | ||  __/ | | | (_|  __/\__ \
# |___/\___|_| |_|\__\___|_| |_|\___\___||___/

def constructSentence():
	combos = [["people", "people"], ["people", "noun"], ["noun", "people"], ["noun", "noun"]]
	for i in range(4):
		sentenceParts10 = returnElements("place adjective " + combos[i][0] + " verb " + combos[i][1] + " adverb obscene")
		if (len(sentenceParts10)):
			pattern = [1,5,1] #describe words per line
			printNewPoem(sentenceParts10, pattern)

		sentenceParts110 = returnElements("place " + combos[i][0] + " verb " + combos[i][1] + " adverb obscene")
		if (len(sentenceParts110)):
			pattern = [1,4,1] #describe words per line
			printNewPoem(sentenceParts110, pattern)

		sentenceParts120 = returnElements("place adjective " + combos[i][0] + " verb " + combos[i][1] + " obscene")
		if (len(sentenceParts120)):
			pattern = [1,4,1] #describe words per line
			printNewPoem(sentenceParts120, pattern)

		sentenceParts130 = returnElements("place " + combos[i][0] + " verb " + combos[i][1] + " obscene")
		if (len(sentenceParts130)):
			pattern = [1,3,1] #describe words per line
			printNewPoem(sentenceParts130, pattern)


		sentenceParts11 = returnElements("adjective " + combos[i][0] + " verb " + combos[i][1] + " adverb obscene")
		if (len(sentenceParts11)):
			pattern = [5,1] #describe words per line
			printNewPoem(sentenceParts11, pattern)

		sentenceParts111 = returnElements(combos[i][0] + " verb " + combos[i][1] + " adverb obscene")
		if (len(sentenceParts111)):
			pattern = [4,1] #describe words per line
			printNewPoem(sentenceParts111, pattern)

		sentenceParts121 = returnElements("adjective " + combos[i][0] + " verb " + combos[i][1] + " obscene")
		if (len(sentenceParts121)):
			pattern = [4,1] #describe words per line
			printNewPoem(sentenceParts121, pattern)

		sentenceParts131 = returnElements(combos[i][0] + " verb " + combos[i][1] + " obscene")
		if (len(sentenceParts131)):
			pattern = [3,1] #describe words per line
			printNewPoem(sentenceParts131, pattern)




		sentenceParts12 = returnElements("place adjective " + combos[i][0] + " verb " + combos[i][1] + " adverb")
		if (len(sentenceParts12)):
			pattern = [1,5] #describe words per line
			printNewPoem(sentenceParts12, pattern)

		sentenceParts112 = returnElements("place " + combos[i][0] + " verb " + combos[i][1] + " adverb")
		if (len(sentenceParts112)):
			pattern = [1,4] #describe words per line
			printNewPoem(sentenceParts112, pattern)

		sentenceParts122 = returnElements("place adjective " + combos[i][0] + " verb " + combos[i][1])
		if (len(sentenceParts122)):
			pattern = [1,4] #describe words per line
			printNewPoem(sentenceParts122, pattern)

		sentenceParts132 = returnElements("place " + combos[i][0] + " verb " + combos[i][1])
		if (len(sentenceParts132)):
			pattern = [1,3] #describe words per line
			printNewPoem(sentenceParts132, pattern)



		sentenceParts13 = returnElements("adjective " + combos[i][0] + " verb " + combos[i][1] + " adverb")
		if (len(sentenceParts13)):
			pattern = [5] #describe words per line
			printNewPoem(sentenceParts13, pattern)

		sentenceParts113 = returnElements(combos[i][0] + " verb " + combos[i][1] + " adverb")
		if (len(sentenceParts113)):
			pattern = [4] #describe words per line
			printNewPoem(sentenceParts113, pattern)

		sentenceParts123 = returnElements("adjective " + combos[i][0] + " verb " + combos[i][1])
		if (len(sentenceParts123)):
			pattern = [4] #describe words per line
			printNewPoem(sentenceParts123, pattern)

		sentenceParts133 = returnElements(combos[i][0] + " verb " + combos[i][1])
		if (len(sentenceParts133)):
			pattern = [3] #describe words per line
			printNewPoem(sentenceParts133, pattern)




#            _  __  __      _                   
#           (_)/ _|/ _|    | |                  
#  ___ _ __  _| |_| |_     | | ___   ___  _ __  
# / __| '_ \| |  _|  _|    | |/ _ \ / _ \| '_ \ 
# \__ \ | | | | | | |      | | (_) | (_) | |_) |
# |___/_| |_|_|_| |_|      |_|\___/ \___/| .__/ 
#                                        | |    
#                                        |_|

# adapted from here: http://stackoverflow.com/a/4417735
def run(command):    
    popen = subprocess.Popen(command, stdout=subprocess.PIPE)
    return iter(popen.stdout.readline, b"")

#GLOBAL variables:
current_channel = 1
def channel_controller(c, c_hop_interval):
    global current_channel
    if c > c_hop_interval:
            idx = channel_range.index(current_channel)
            idx = idx + 1
            if idx >= len(channel_range):
                idx = 0;
            current_channel = channel_range[idx]

            subprocess.call("airport -c" + str(current_channel), shell=True)
            # print "///////////////////////////////////////////// Switched to channel: " + str(current_channel)
            c = 0   
    else:
        c = c + 1 
    return c

def sniffloop():
    global current_channel
    count = 10
    alreadyInspected = set()
    current_channel = channel_range[-1]
    #next line makes all the difference, making sure the hoping works by disassociating fro any network before start:
    subprocess.call("airport -z", shell=True)		# DEactivate for TESTING

    for line in run("./bps_v1"):		# DEactivate for TESTING
    # for line in open("no_realtime_experiment_log.log", "r"):  # activate for TESTING
		#next line for channel hoping:
		count = channel_controller(count, channel_hop_interval)		# DEactivate for TESTING
		line = line.strip()

		words = line.split(',')
		if(words[1] == "probe"): # ultimately I'll change the lbtins exec to only show probes (probably)
			if words[3] not in alreadyInspected:
				alreadyInspected.add(words[3])
				returnList = check_for_words_in_network_name(words[3])
				if(len(returnList[0]) > 0):
					unused[returnList[1]][words[3]] = returnList[0]
					# pprint(unused)
		constructSentence()         	

           

# GLOBAL variables:
channel_range = [1,6,11,36,40,44,48]
channel_hop_interval = 50

def Main():  
    sniffloop();

if __name__ == '__main__':
    Main()

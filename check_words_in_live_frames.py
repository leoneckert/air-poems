import sys
from pprint import pprint
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
#------------------------------------------------------------

# there can be more than one match, we want the longest one
def check_for_words_in_network_name(_network_name):
	networkname = _network_name.lower()
	longestmatch = list()
	longestmatch.append("") #actual match
	longestmatch.append("") #type

	places = open('places.txt', 'r')
	for place in places:
		place = place.strip()
		matchinplace = check_if_part_of_word1_equals_word2(networkname,place,len(longestmatch[0]))
		if len(matchinplace) > 0:
			longestmatch[0] = matchinplace
			longestmatch[1] = "place"

	peoples = open('people.txt', 'r')
	for people in peoples:
		people = people.strip()
		matchingpeople = check_if_part_of_word1_equals_word2(networkname,people,len(longestmatch[0]))
		if len(matchingpeople) > 0:
			longestmatch[0] = matchingpeople
			longestmatch[1] = "people"

	nouns = open('91Knouns.txt', 'r')
	for noun in nouns:
		noun = noun.strip()
		matchingnoun = check_if_part_of_word1_equals_word2(networkname,noun,len(longestmatch[0]))
		if len(matchingnoun) > 0:
			longestmatch[0] = matchingnoun
			longestmatch[1] = "noun"

	verbs = open('31Kverbs.txt', 'r')
	for verb in verbs:
		verb = verb.strip()
		matchinverb = check_if_part_of_word1_equals_word2(networkname,verb,len(longestmatch[0]))
		if len(matchinverb) > 0:
			longestmatch[0] = matchinverb
			longestmatch[1] = "verb"

	adjectives = open('28Kadjectives.txt', 'r')
	for adjective in adjectives:
		adjective = adjective.strip()
		matchingadjective = check_if_part_of_word1_equals_word2(networkname,adjective,len(longestmatch[0]))
		if len(matchingadjective) > 0:
			longestmatch[0] = matchingadjective
			longestmatch[1] = "adjective"

	adverbs = open('6Kadverbs.txt', 'r')
	for adverb in adverbs:
		adverb = adverb.strip()
		matchingadverb = check_if_part_of_word1_equals_word2(networkname,adverb,len(longestmatch[0]))
		if len(matchingadverb) > 0:
			longestmatch[0] = matchingadverb
			longestmatch[1] = "adverb"

	obscenes = open('obscene.txt', 'r')
	for obscene in obscenes:
		obscene = obscene.strip()
		matchingadobscene = check_if_part_of_word1_equals_word2(networkname,obscene,len(longestmatch[0]))
		if len(matchingadobscene) > 0:
			longestmatch[0] = matchingadobscene
			longestmatch[1] = "obscene"

	return longestmatch
#------------------------------------------------------------


# networkname = sys.argv[1]
# print check_for_words_in_network_name(networkname)
# print time.time() - startTime
alreadyInspected = set()

import subprocess
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


unused = dict()
unused["people"] = dict() #network name: word
unused["noun"] = dict()
unused["verb"] = dict()
unused["place"] = dict()
unused["adjective"] = dict()
unused["adverb"] = dict()
unused["obscene"] = dict()

# places adjective people verb people2 adverb obscene


def returnElements(elementListSpaceDivided):
	# inputString = elementListSpaceDivided
	elems = elementListSpaceDivided.split(" ")
	#count how many of each element we need
	requiredDic = dict()
	for elem in elems:
		if elem in requiredDic:
			requiredDic[elem] += 1
		else:
			requiredDic[elem] = 0

	hasAll = True
	for e in requiredDic:
		if len(unused[e]) > requiredDic[e]

	if len(unused["people"]) > 1 and len(unused["verb"]) > 0 :

	print requiredDic


def constructSentence():
	# people verb people
	# -
	# people verb noun
	# -
	# place 
	# adjective people
	# obscene
	# - 
	# adjective people
	# obscene
	# -
	# place 
	# adjective people
	# -
	# adjective people
	# -
	# --
	# place 
	# adjective noun
	# obscene
	# - 
	# adjective noun
	# obscene
	# -
	# place 
	# adjective noun
	# -
	# adjective noun
	returnElements("noun people noun place")

	# # people verb people
	# if len(unused["people"]) > 1 and len(unused["verb"]) > 0 :
	# 	print "-"*30
	# 	print "\n\nNew Air Poem:\n\n\n"

	# 	for a in unused["people"]:
	# 		peo1net = a #this has to be random
	# 		break
	# 	peo1word = unused["people"].pop(peo1net)
		
	# 	for b in unused["verb"]:
	# 		ver1net = b
	# 		break
	# 	ver1word = unused["verb"].pop(ver1net)

	# 	for c in unused["people"]:
	# 		peo2net = c
	# 		break
	# 	peo2word = unused["people"].pop(peo2net)

	# 	print peo1net, ver1net, peo2net
	# 	print "\n"
	# 	print peo1word, ver1word, peo2word
	# 	print "\n\n"
	# 	print "-"*30

	# # people verb noun
	# if len(unused["people"]) > 0 and len(unused["verb"]) > 0 and len(unused["noun"]) > 0 :
	# 	print "-"*30
	# 	print "\n\nNew Air Poem:\n\n\n"

	# 	for a in unused["people"]:
	# 		peo1net = a
	# 		break
	# 	peo1word = unused["people"].pop(peo1net)
		
	# 	for b in unused["verb"]:
	# 		ver1net = b
	# 		break
	# 	ver1word = unused["verb"].pop(ver1net)

	# 	for c in unused["noun"]:
	# 		nou1net = c
	# 		break
	# 	nou1word = unused["noun"].pop(nou1net)

	# 	print peo1net, ver1net, nou1net
	# 	print "\n"
	# 	print peo1word, ver1word, nou1word
	# 	print "\n\n"
	# 	print "-"*30

	# # place 
	# # adjective people
	# # obscene
	# if len(unused["place"]) > 0 and len(unused["adjective"]) > 0 and len(unused["people"]) > 0 and len(unused["obscene"]) > 0:
	# 	print "-"*30
	# 	print "\n\nNew Air Poem:\n\n\n"

	# 	for a in unused["place"]:
	# 		pla1net = a
	# 		break
	# 	pla1word = unused["place"].pop(pla1net)

	# 	for b in unused["adjective"]:
	# 		adj1net = b
	# 		break
	# 	adj1word = unused["adjective"].pop(adj1net)

	# 	for c in unused["people"]:
	# 		peo1net = c
	# 		break
	# 	peo1word = unused["people"].pop(peo1net)

	# 	for d in unused["obscene"]:
	# 		obs1net = d
	# 		break
	# 	obs1word = unused["obscene"].pop(obs1net)
		
	# 	print pla1net
	# 	print "\n"
	# 	print adj1net, peo1net
	# 	print "\n"
	# 	print obs1net
	# 	print "\n"
	# 	print pla1word
	# 	print "\n"
	# 	print adj1word, peo1word
	# 	print "\n"
	# 	print obs1word
	# 	print "\n\n"
	# 	print "-"*30

	# # adjective people
	# # obscene
	# if len(unused["adjective"]) > 0 and len(unused["people"]) > 0 and len(unused["obscene"]) > 0:
	# 	print "-"*30
	# 	print "\n\nNew Air Poem:\n\n\n"

	# 	for a in unused["adjective"]:
	# 		adj1net = a
	# 		break
	# 	adj1word = unused["adjective"].pop(adj1net)

	# 	for b in unused["people"]:
	# 		peo1net = b
	# 		break
	# 	peo1word = unused["people"].pop(peo1net)

	# 	for c in unused["obscene"]:
	# 		obs1net = c
	# 		break
	# 	obs1word = unused["obscene"].pop(obs1net)
		
		
	# 	print adj1net, peo1net
	# 	print "\n"
	# 	print obs1net
	# 	print "\n"
	# 	print adj1word, peo1word
	# 	print "\n"
	# 	print obs1word
	# 	print "\n\n"
	# 	print "-"*30

	# # place 
	# # adjective people
	# if len(unused["place"]) > 0 and len(unused["adjective"]) > 0 and len(unused["people"]) > 0:
	# 	print "-"*30
	# 	print "\n\nNew Air Poem:\n\n\n"

	# 	for a in unused["place"]:
	# 		pla1net = a
	# 		break
	# 	pla1word = unused["place"].pop(pla1net)

	# 	for b in unused["adjective"]:
	# 		adj1net = b
	# 		break
	# 	adj1word = unused["adjective"].pop(adj1net)

	# 	for c in unused["people"]:
	# 		peo1net = c
	# 		break
	# 	peo1word = unused["people"].pop(peo1net)

	# 	print pla1net
	# 	print "\n"
	# 	print adj1net, peo1net
	# 	print "\n"
	# 	print pla1word
	# 	print "\n"
	# 	print adj1word, peo1word
	# 	print "\n\n"
	# 	print "-"*30

	# # adjective people
	# if len(unused["adjective"]) > 0 and len(unused["people"]) > 0 :
	# 	print "-"*30
	# 	print "\n\nNew Air Poem:\n\n\n"

	# 	for a in unused["adjective"]:
	# 		adj1net = a
	# 		break
	# 	adj1word = unused["adjective"].pop(adj1net)

	# 	for b in unused["people"]:
	# 		peo1net = b
	# 		break
	# 	peo1word = unused["people"].pop(peo1net)
		
	# 	print adj1net, peo1net
	# 	print "\n"
	# 	print adj1word, peo1word
	# 	print "\n\n"
	# 	print "-"*30


	# # place 
	# # adjective noun
	# # obscene
	# if len(unused["place"]) > 0 and len(unused["adjective"]) > 0 and len(unused["noun"]) > 0 and len(unused["obscene"]) > 0:
	# 	print "-"*30
	# 	print "\n\nNew Air Poem:\n\n\n"

	# 	for a in unused["place"]:
	# 		pla1net = a
	# 		break
	# 	pla1word = unused["place"].pop(pla1net)

	# 	for b in unused["adjective"]:
	# 		adj1net = b
	# 		break
	# 	adj1word = unused["adjective"].pop(adj1net)

	# 	for c in unused["noun"]:
	# 		nou1net = c
	# 		break
	# 	nou1word = unused["noun"].pop(nou1net)

	# 	for d in unused["obscene"]:
	# 		obs1net = d
	# 		break
	# 	obs1word = unused["obscene"].pop(obs1net)
		
	# 	print pla1net
	# 	print "\n"
	# 	print adj1net, nou1net
	# 	print "\n"
	# 	print obs1net
	# 	print "\n"
	# 	print pla1word
	# 	print "\n"
	# 	print adj1word, nou1word
	# 	print "\n"
	# 	print obs1word
	# 	print "\n\n"
	# 	print "-"*30

	# # adjective noun
	# # obscene
	# if len(unused["adjective"]) > 0 and len(unused["noun"]) > 0 and len(unused["obscene"]) > 0:
	# 	print "-"*30
	# 	print "\n\nNew Air Poem:\n\n\n"

	# 	for a in unused["adjective"]:
	# 		adj1net = a
	# 		break
	# 	adj1word = unused["adjective"].pop(adj1net)

	# 	for b in unused["noun"]:
	# 		nou1net = b
	# 		break
	# 	nou1word = unused["noun"].pop(nou1net)

	# 	for c in unused["obscene"]:
	# 		obs1net = c
	# 		break
	# 	obs1word = unused["obscene"].pop(obs1net)
		
		
	# 	print adj1net, nou1net
	# 	print "\n"
	# 	print obs1net
	# 	print "\n"
	# 	print adj1word, nou1word
	# 	print "\n"
	# 	print obs1word
	# 	print "\n\n"
	# 	print "-"*30

	# # place 
	# # adjective noun
	# if len(unused["place"]) > 0 and len(unused["adjective"]) > 0 and len(unused["noun"]) > 0:
	# 	print "-"*30
	# 	print "\n\nNew Air Poem:\n\n\n"

	# 	for a in unused["place"]:
	# 		pla1net = a
	# 		break
	# 	pla1word = unused["place"].pop(pla1net)

	# 	for b in unused["adjective"]:
	# 		adj1net = b
	# 		break
	# 	adj1word = unused["adjective"].pop(adj1net)

	# 	for c in unused["noun"]:
	# 		nou1net = c
	# 		break
	# 	nou1word = unused["noun"].pop(nou1net)

	# 	print pla1net
	# 	print "\n"
	# 	print adj1net, nou1net
	# 	print "\n"
	# 	print pla1word
	# 	print "\n"
	# 	print adj1word, nou1word
	# 	print "\n\n"
	# 	print "-"*30

	# # adjective noun
	# if len(unused["adjective"]) > 0 and len(unused["noun"]) > 0 :
	# 	print "-"*30
	# 	print "\n\nNew Air Poem:\n\n\n"

	# 	for a in unused["adjective"]:
	# 		adj1net = a
	# 		break
	# 	adj1word = unused["adjective"].pop(adj1net)

	# 	for b in unused["noun"]:
	# 		nou1net = b
	# 		break
	# 	nou1word = unused["noun"].pop(nou1net)
		
	# 	print adj1net, nou1net
	# 	print "\n"
	# 	print adj1word, nou1word
	# 	print "\n\n"
	# 	print "-"*30



def sniffloop():
    global current_channel
    count = 10
    current_channel = channel_range[-1]
    #next line makes all the difference, making sure the hoping works by disassociating fro any network before start:
    subprocess.call("airport -z", shell=True)

    for line in run("./bps_v1"):
		#next line for channel hoping
		count = channel_controller(count, channel_hop_interval)
		line = line.strip()
		# print line

		words = line.split(',')
		# print words
		if(words[1] == "probe"): #ultimately I'll change the lbtins exec to only show probes
            
			if words[3] not in alreadyInspected:
				
				alreadyInspected.add(words[3])
				returnList = check_for_words_in_network_name(words[3])
				if(len(returnList[0]) > 0):
					# print words[3]
					# print "\t-->"
					# print "\t\tresult:", returnList
					unused[returnList[1]][words[3]] = returnList[0]
					pprint(unused)

		constructSentence()         	

     

       
        

# GLOBAL variables:
channel_range = [1,6,11,36,40,44,48]
channel_hop_interval = 50


def Main():  
    sniffloop();

if __name__ == '__main__':
    Main()

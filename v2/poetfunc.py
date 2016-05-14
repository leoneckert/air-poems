from pprint import pprint
import random
import os
from textblob import TextBlob, Word
from nltk.corpus import words
import tracery
from tracery.modifiers import base_english
import printpoetry



dictionaries = dict()
blacklist = dict()


def initDicts():
	# here we should also initialise the BLACKLIST # this format: [gordon#names]
	for root, dirs, files in os.walk("./dictionaries"):
		for file in files:
			if file.endswith(".txt") and file.startswith("_"):
				path = os.path.join(root, file)
				filename = str(file)
				penn = filename.split('_')[1]
				for word in open(path, "r"):
					word = word.strip()

					if penn not in dictionaries:
						dictionaries[penn] = set()
					dictionaries[penn].add(word)

					if penn not in blacklist:
						blacklist[penn] = set()
	
	for root, dirs, files in os.walk("./dictionaries"):
		for file in files:
			if file.endswith(".txt") and file.startswith("blacklist"):
				path = os.path.join(root, file)
				filename = str(file)
				for word in open(path, "r"):
					word = word.strip()
					# print word
					# print word[1:-1]
					# print word[1:-1].split("#")
					back_listed_word = word[1:-1].split("#")[0]
					penn = word[1:-1].split("#")[1]
					# print back_listed_word, penn
					if penn not in blacklist:
						blacklist[penn] = set()
					blacklist[penn].add(back_listed_word)
	# pprint(blacklist)




def printDictionairies():
	for d in dictionaries:
		print "--\ndictionairy:", d
		print "\t\twords", len(dictionaries[d])

available = dict()
shortestWordLength = 2
def getWordsInSsid(ssid):
	# print "-"*10
	# print ssid
	len_ssid = len(ssid)
	for penn in dictionaries:
		for word in dictionaries[penn]:
			if len(word) > shortestWordLength and word in ssid.lower():
				# print "\t\t", word, penn

				# here we build in a BLACKSLIST mechanism
				if word in blacklist[penn]:
					break

				if penn not in available:
					available[penn] = dict()
				if word not in available[penn]:
					available[penn][word] = list()
				

				temp_tuple = (ssid,ssid.lower().index(word),ssid.lower().index(word) + len(word))
				available[penn][word].append(temp_tuple)
	build_sentence()
			


def printAvailable():
	# pprint(available)
	for penn in available:
		print penn
		for word in available[penn]:
			print "\t\t", word
			for ssid_data in available[penn][word]:
				print "\t\t\t\t", ssid_data
				for dataPoint in ssid_data:
					print "\t\t\t\t\t\t", dataPoint
				print "\t\t\t\t\t\t\t\t\t", ssid_data[0][ssid_data[1]:ssid_data[2]]


def deleteUsedData(data):
	word = data[0]
	penn = data[1] 
	ssid = data[2]
	start_idx = data[3] 
	end_idx = data[4] 
	# print str(ssid)
	# print "delete:", (ssid, start_idx, end_idx)

	# if the word was ued twice in the sentence we return directly:
	if penn not in available:
		return True
	# else:
		# print available[penn]

	if word not in available[penn]:
		return True
	if (ssid, start_idx, end_idx) not in available[penn][word]:
		return True
	
	

	available[penn][word].remove((ssid, start_idx, end_idx))
	

	if len(available[penn][word]) < 1:
		del available[penn][word]
	if len(available[penn]) < 1:
		del available[penn]

def hasData(penn):
	if penn in available and len(available[penn]):
		return True
	return False

noData = ["*X*X*X*X*"]
start_ind = "@sta*rt@"
sep_ind = "@sepe*rate@"
end_ind = "@e*nd@"
start_and_end_Mark = "***@***"


def returnList(penn):
	return [elem.split()[0] + start_and_end_Mark + start_ind + elem + sep_ind + penn + sep_ind + str(available[penn][elem][0]) + end_ind + start_and_end_Mark + elem.split()[-1] for elem in available[penn]]





def build_sentence():
	rules = {

		# 's0': '#name.capitalize# and #name# are happy happy happy',
		# 's1': '#actorSG.a.capitalize# and #name# are happy happy happy',
		# 's0': '#adjective.a# #actorSG# and #adjective.a# #actorSG# do it #adverb#.',
		's0': '#name# #verbThird# #adverb#.',
		's1': '#name# is #verbGer# #adverb#.',
		's2': '#name# and #name# #verbInf# #adverb#.',
		's3': '#name# and #name# #verbPast# #adverb#.',
		's4': '#name# and #name# are #verbGer# #adverb#.',
		# 's0': '#name# #verbPast# #adverb# and #name# #verbPast# #adverb#.',
		# 's1': '#name# is #verbGer# #adverb# and #name# is #verbGer# #adverb#.',
		# 's2': '#name# #verbThird# #adverb# and #name# #verbThird# #adverb#.',
		# 's3': '#name.capitalize# and #actorSG.a# are happy happy happy',

	    # 's0': '#nounS.a.capitalize# and #nounS.a# #verb# with #nounS.a#',
	    # 's1': '#name# and #name# #verb# with #nounS.a#',
	    # 's2': 'The #adjective# #name# and the #adjective# #name# #verb# with #nounS.a#',
	    
	    # 'nounS': returnList("nounS") if hasData("nounS") > 0 else noData,
	    # 'verb': returnList("VB") if hasData("VB") > 0 else noData,


	    'name': returnList("names") if hasData("names") > 0 else noData,
	    'actorSG': returnList("actorsSG") if hasData("actorsSG") > 0 else noData,


	    'verbInf': returnList("verbInf") if hasData("verbInf") > 0 else noData,
	    'verbThird': returnList("verbThird") if hasData("verbThird") > 0 else noData,
	    'verbGer': returnList("verbGer") if hasData("verbGer") > 0 else noData,
	    'verbPast': returnList("verbPast") if hasData("verbPast") > 0 else noData,

	    
	    'adjective': returnList("adjectives") if hasData("adjectives") > 0 else noData,
	    'adverb': returnList("adverbs") if hasData("adverbs") > 0 else noData,

	    'obscene': returnList("obscenes") if hasData("obscenes") > 0 else noData
	    

	}
	numPennInRules = 9

	grammar = tracery.Grammar(rules)
	grammar.add_modifiers(base_english)
	
	s_structures = range(len(rules) - numPennInRules)
	random.shuffle(s_structures)

	# print "\tAVAILABLE:", available
	for s_idx in s_structures:
		# print s_idx
		gen_sentence = grammar.flatten("#s" + str(s_idx) + "#")
		# print gen_sentence
		if noData[0] in gen_sentence:
			# print "\tnot enough data"
			gen_sentence = ""
		else:
			break 

	
	if len(gen_sentence) > 0:
		sentence_details = list()
		# print gen_sentence
		gen_sentence_list = gen_sentence.split(start_and_end_Mark)
		for i in range(len(gen_sentence_list)):
			elem = gen_sentence_list[i]
			# print "ELEM:", elem
			sentence_details.append(elem)

			if elem.startswith(start_ind) and i > 0:
				sentence_details[i - 1] = " ".join(sentence_details[i - 1].split()[:-1])


		for i in range(len(gen_sentence_list)):
			elem = gen_sentence_list[i]
			if elem.endswith(end_ind) and i < len(gen_sentence_list):
				sentence_details[i + 1] = " ".join(sentence_details[i + 1].split()[1:])


		# print "-"
		temp_list = list()
		for e in sentence_details:
			if len(e) > 0:
				temp_list.append(e)

		sentence_details = list()
		sentence_details = temp_list
		temp_list = list()
		for e in sentence_details:
			# print "\t\t", e
			if e.startswith(start_ind):
				e = e[len(start_ind):-len(end_ind)]
				word = e.split(sep_ind)[0]
				penn = e.split(sep_ind)[1]
				ssid_data = e.split(sep_ind)[2]
				ssid = ssid_data.split(',')[0][2:-1]

				ssid_word_start_index = int(ssid_data.split(',')[1][1:])
				ssid_word_end_index = int(ssid_data.split(',')[2][1:-1])
				e = [word, penn, ssid, ssid_word_start_index, ssid_word_end_index]
			else:
				e = [e]
			temp_list.append(e)
		sentence_details = list()
		sentence_details = temp_list
		
		#check if we want to use the data we picked:
		wordsSeen = set()
		ssidsSeen = set()
		useThisData = True
		for e in sentence_details:
			if len(e) == 5:
				word = e[0]
				if word not in wordsSeen:
					wordsSeen.add(word)
				else:
					useThisData = False
				ssid = e[2]
				if ssid not in ssidsSeen:
					ssidsSeen.add(ssid)
				else:
					useThisData = False

		if useThisData is True:
			# delete the data that was picked from the available-dictionairy
			for e in sentence_details:
				if len(e) == 5:
					deleteUsedData(e)
			# print sentence_details

			printpoetry.printp(sentence_details)
			# pprint(available)




	



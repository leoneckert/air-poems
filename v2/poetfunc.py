from pprint import pprint
import random

# # dicts = ["verbs", "adjectives", "obscenes", "adverbs", "places", "peoples", "nouns"]
# dicts = ["out"]

dictionaries = dict()




import os
def initDicts():
	for root, dirs, files in os.walk("./dictionaries/temp"):
		for file in files:
			if file.endswith(".txt"):
				path = os.path.join(root, file)
				filename = str(file)
				penn = filename.split('_')[0]
				for word in open(path, "r"):
					word = word.strip()

					if penn not in dictionaries:
						dictionaries[penn] = set()
					dictionaries[penn].add(word)


def printDictionairies():
	for d in dictionaries:
		print "--\ndictionairy:", d
		print "\t\twords", len(dictionaries[d])



from textblob import TextBlob, Word
from nltk.corpus import words

available = dict()
shortestWordLength = 2
def getWordsInSsid(ssid):
	print "-"*10
	print ssid
	len_ssid = len(ssid)
	for penn in dictionaries:
		for word in dictionaries[penn]:
			if len(word) > shortestWordLength and word in ssid.lower():
				# print "\t\t", word, penn
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

	# if the word was ued twice in the sentence we return directly:
	if penn not in available:
		print "already deleted:", penn
		return True
	if word not in available[penn]:
		print "already deleted:", word, "in", penn
		return True
	if (ssid, start_idx, end_idx) not in available[penn][word]:
		print "already deleted:", (ssid, start_idx, end_idx), "in", word, "in", penn
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




import tracery
from tracery.modifiers import base_english
def build_sentence():
	rules = {
	    's0': '#nounS.a.capitalize# and #nounS.a# #verb# with #nounS.a#',
	    's1': '#name# and #name# #verb# with #nounS.a#',
	    's2': 'The #adjective# #name# and the #adjective# #name# #verb# with #nounS.a#',
	    
	    'nounS': returnList("nounS") if hasData("nounS") > 0 else noData,
	    'verb': returnList("VB") if hasData("VB") > 0 else noData,
	    'name': returnList("names") if hasData("names") > 0 else noData,
	    'adjective': returnList("JJ") if hasData("JJ") > 0 else noData

	}
	numPennInRules = 4

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


		print "-"
		temp_list = list()
		for e in sentence_details:
			if len(e) > 0:
				temp_list.append(e)

		sentence_details = list()
		sentence_details = temp_list
		temp_list = list()
		for e in sentence_details:
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
		for e in sentence_details:
			print e
			if len(e) == 5:
				deleteUsedData(e)
		# print "\tAVAILABLE:", available


		# next up: removing the word fro the available dicts and print it out




	



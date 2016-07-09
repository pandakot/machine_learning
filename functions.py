
import re
from nltk.corpus import stopwords
from string import punctuation
from stemming.porter2 import stem

####################################
def build_params(filename):
	
	fp = open(filename, 'r')

	Xbig = []
	y = []	

	i = 0
	for line in fp.readlines() :
	
		x = []
		line = line.split(' ')
		j = 1
		line_len = len(line)
		for p in line :

			if j < line_len :	
				x.append(int(p))
			else: 
				y.append(int(p.strip('\n')))
			j += 1	
		Xbig.append(x)
		i += 1

	print i
	fp.close()
	return {'x': Xbig, 'y': y}
#############################

def strip_punctuation(s):
	return ''.join(c for c in s if c not in punctuation)

###########################
def dict_stemmed(text, wordDict):

	for word in text.split(' '):    

		if word in wordDict.keys() :
			wordDict[word] += 1
		else:
			wordDict[word] = 1

	return wordDict

##################################
def dict_process(wordDict):
	
	print len(wordDict)
	
	dictList = []
	for word in wordDict:
		if len(word)>1 and wordDict[word] > 20 :
			dictList.append(word)

	return sorted(dictList)



#################################
def save_dict_to_file(wordDict):

	print len(wordDict)

	file_name = 'dict.txt'
	f = open(file_name, 'w')

	i = 1
	for word in wordDict:
		f.write( str(i) + '\t' + word + '\n')
		i += 1

	f.close()

#################################
def stemm(text, companyA, companyB) :
	#text = text.replace("~~~'s", '~~~')
	#companyA = '~~~' + companyA + '~~~'
	#companyB = '~~~' + companyB + '~~~'
	#stemmed = text.replace(companyA, 'companya ')
	#stemmed = stemmed.replace(companyB, 'companyb ')

	letters_only = re.sub("[^\w]", " ", text) 
	#text = letters_only
	#words = letters_only.lower().split()       
	#stops = set(stopwords.words("english")) 
	#meaningful_words = [stem_word(w) for w in words if not w in stops] 

	#text = " ".join( meaningful_words )
	text = remove_brands(text)
	return text

###################################
def stem_word(word):
	to_return = '';

	if word.find('suppl') == -1:
		to_return = stem(word)
	else:
		to_return = word

	return to_return

 
###########################
def remove_brands(text):
	brands = ['(', ')', '*', "'", ',', '!', '.']

	for brand in brands:
		text = text.replace(brand, '')

	return text

###############################
def example_result(text_result):
	count_images = [0]*601;
	
	count = 0
	for i in count_images:
 		
		if count_images[count] == (int(text_result)-1):
			print str(count) + ': !!!!!!!!!!!!!!'
			count_images[count] = 1
		count += 1

	return count_images

##################################
def show_relation(relation_num):
	relation = 'Relation unclassified'

	if relation_num == 1 :
		relation = 'No relation exists between the companies'
	elif relation_num == 2 :
		relation = 'Some direct relation exists between the companies, but is not a valid supplier-customer relation'
 	elif relation_num == 3 :
		relation = 'B supplies A'
	elif relation_num == 4 : 
		relation = 'A supplies B'

	return relation

############################
def load_dict(filename) :
	wordDict = {};
	dictFile = open(filename, 'r')

	wd = []
	for line in dictFile.readlines() :
		line = line.split('\t')
		wordDict[line[1].strip('\n')] = line[0]
		wd.append(line[1].strip('\n'))

	dictFile.close()
	return wd


############################
###########################
############################
def stemm_old(text, companyA, companyB) :
	companyA = '~~~' + companyA + '~~~'
	companyB = '~~~' + companyB + '~~~'
	stemmed = text.replace(companyA, 'companya ')
	stemmed = stemmed.replace(companyB, 'companyb ')
	stemmed = stemmed.replace('%', 'percent')
	stemmed = stemmed.lower()
	stemmed = re.sub("\d+", "number", stemmed)
	stemmed = re.sub('\s+', ' ', stemmed)
	stemmed = re.sub(r'\W*\b\w{1,2}\b', '', stemmed)
	stemmed = stemmed.replace('  ', ' ')
	stemmed = stemmed.replace('  ', ' ')
	stemmed = stemmed.replace('  ', ' ')
	stemmed = remove_brands(stemmed)
	stemmed = strip_punctuation(stemmed)

	#to_return = stemmed
	to_return = '';
	for word in stemmed.split(' '):    
		if word.find('suppl') == -1:
			to_return += stem(word) + ' '
		else:
			to_return += word + ' '
	return to_return



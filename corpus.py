# -*- coding: utf-8 -*-
from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import PlaintextCorpusReader
import StringIO
import sys

def std_to_str(text, words):

	old_stdout = sys.stdout
	sys.stdout = mystdout = StringIO.StringIO()
	
	#text.common_contexts([u'был'], 10) 
	#text.concordance(u'был')
	text.similar(words)
	x = mystdout.getvalue()
	sys.stdout = old_stdout
	mystdout.close()
	return x


corpus_root = './'
newcorpus = PlaintextCorpusReader(corpus_root , '.*')
words = newcorpus.words('corpus.txt')
text = nltk.Text(words)

z = std_to_str(text, u'кот чешет себя')

#text.common_contexts([u'был'], 10) 
#text.concordance(u'был')
#text.similar(u'был')

print z

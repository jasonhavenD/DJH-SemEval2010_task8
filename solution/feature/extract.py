#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:pos
   Author:admin
   date:2018/4/8
-------------------------------------------------
   Change Activity:2018/4/8:
-------------------------------------------------
"""

'''
实体词性、实体位置、实体上下文左右两个单词
'''
from stanfordcorenlp import StanfordCoreNLP
import re
from bs4 import BeautifulSoup

delimiter = '\t'
E1 = 'e1'
E2 = 'e2'


def extract_features(train_sents):
	'''
	:param train_sents:list
	:return:features:list
	'''
	features = []

	nlp = StanfordCoreNLP(r'C:\stanford-corenlp-full-2018-02-27')

	for line in train_sents:
		feature = {}
		soup = BeautifulSoup(line, 'html.parser')
		e1 = soup.find(E1).text
		e2 = soup.find(E2).text
		# print(e1, e2)

		sent = re.split(r'[."\s]+', line)

		for w in sent:
			if w.startswith("<" + E1 + ">"):
				feature['index1'] = sent.index(w)
				break
		for w in sent:
			if w.startswith("<" + E2 + ">"):
				feature['index2'] = sent.index(w)
				break

		sent = re.split(r'[.\s]+', soup.text)
		# print(sent)

		feature['preffix1'], feature['preffix2'] = e1[:2], e2[:2]
		feature['suffix1'], feature['suffix2'] = e1[-2:], e2[-2:]
		feature['istitle1'], feature['istitle2'] = e1.istitle(), e2.istitle()
		feature['pos_tag1'], feature['pos_tag2'] = nlp.pos_tag(e1)[0][1], nlp.pos_tag(e2)[0][1]

		if feature['index1'] < 2:
			feature['pre_pos_tag1'] = 'None'
			feature['pre_istitle1'], feature['pre_istitle2'] = 'None', 'None'
		else:
			word1, word2 = sent[feature['index1'] - 1], sent[feature['index2'] - 1]
			feature['pre_istitle1'], feature['pre_istitle2'] = word1.istitle(), word2.istitle()
			feature['pre_pos_tag1'], feature['pre_pos_tag2'] = nlp.pos_tag(word1)[0][1], nlp.pos_tag(word2)[0][1]

		if feature['index2'] > len(sent) - 2:
			feature['post_pos_tag2'] = 'None'
			feature['post_istitle1'], feature['post_istitle2'] = 'None', 'None'
		else:
			word1, word2 = sent[feature['index1'] + 1], sent[feature['index2'] + 1]
			feature['post_istitle1'], feature['post_istitle2'] = word1.istitle(), word2.istitle()
			feature['post_pos_tag1'], feature['post_pos_tag2'] = nlp.pos_tag(word1)[0][1], nlp.pos_tag(word2)[0][1]

		# print(feature)
		features.append(feature)
	nlp.close()

	return features


def extract_labels(train_keys):
	'''
	:param train_keys:list
	:return:labels:list
	'''
	labels = []
	for k in train_keys:
		labels.append(k.split('\t')[1])
	return labels


if __name__ == '__main__':
	train_sents = [
		'1	"The system as described above has its greatest application in an arrayed <e1>configuration</e1> of antenna <e2>elements</e2>."',
		'2	"The <e1>child</e1> was carefully wrapped and bound into the <e2>cradle</e2> by means of a cord."',
		'8	"<e1>People</e1> have been moving back into <e2>downtown</e2>."',
		'9	"The <e1>lawsonite</e1> was contained in a <e2>platinum crucible</e2> and the counter-weight was a plastic crucible with metal pieces."'
	]

	features = extract_features(train_sents)

# train_keys = [
# 	'1	Component - Whole(e2, e1)',
# 	'2	Other',
# 	'3	Instrument - Agency(e2, e1)',
# 	'4	Other',
# 	'5	Member - Collection(e1, e2)'
# ]
# labels = extract_labels(train_keys)
# print(labels)

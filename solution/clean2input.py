#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:extract_sents
   Author:jason
   date:2018/4/7
-------------------------------------------------
   Change Activity:2018/4/7:
-------------------------------------------------
"""
import sys
import datetime

sys.path.append("./feature")

from feature import extract
from feature import digitalize
from feature import normalize

delimiter = "\t"


def load(file):
	'''
	:param file: str
	:return:text:list
	'''
	text = []
	with open(file, "r", encoding="utf-8") as f:
		for line in f.readlines():
			line = line.replace('<e', ' <e')  # 确保实体标记之前有空白字符
			text.append(line.strip())
	return text


def save(text, file):
	'''
	:param text:list
	:param file: str
	:return:
	'''
	try:
		with open(file, "w", encoding="utf-8") as f:
			for line in text:
				f.write(line + "\n")
		print("save successfully!", file)
	except Exception as e:
		print(e)


def convert_features(text):
	'''
	:param text:list
	:return:text:list
	'''
	features = extract.extract_features(text)
	# for f in features:
	# 	print(f)
	features_dataframe = digitalize.get_features_dataframe(features)
	props_table = digitalize.get_props_table(features_dataframe)
	nums_of_features = digitalize.features2nums(features_dataframe, props_table)
	normalized_features = normalize.normalize(nums_of_features)
	text = []
	for row in normalized_features.index:
		row_str = [str(x) for x in list(normalized_features.loc[row])]
		text.append(delimiter.join(row_str))
	return text


def convert_labels(text):
	'''
	:param text:list
	:return:nums_of_labels:list
	'''
	labels = extract.extract_labels(text)
	nums_of_labels = [str(x) for x in digitalize.labels2nums(labels)]
	return nums_of_labels


if __name__ == '__main__':
	ftrain = "data/clean/train_clean.txt"
	ftest = "data/clean/test_clean.txt"
	fkey = "data/clean/train_key.txt"

	# begin = datetime.datetime.now()
	# train_text = load(ftrain)
	# train_text = convert_features(train_text)
	# save(train_text, "data/input/train.txt")
	# end = datetime.datetime.now()
	# print('convert_features finished in ' + str((end - begin).seconds) + ' s!')

	# begin = datetime.datetime.now()
# test_text = load(ftest)
# test_text = convert_features(test_text)
# save(test_text, "data/input/test.txt")
# end = datetime.datetime.now()
# print('convert_features finished in ' + str((end - begin).seconds) + ' s!')

# begin = datetime.datetime.now()
# key_text = load(fkey)
# key_text = convert_labels(key_text)
# save(key_text, "data/input/key.txt")
# end = datetime.datetime.now()
# print('convert_labels finished in ' + str((end - begin).seconds) + ' s!')

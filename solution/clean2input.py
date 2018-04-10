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
sys.path.append("./ioutil")
from feature import extract
from feature import digitalize
from feature import normalize
from ioutil import io

delimiter = "\t"


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
	digitalize.save_features_mapping_table(props_table,"data/mapping/features.txt")  # save mapping file
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
	labels_table = digitalize.get_labels_table(labels)
	digitalize.save_labels_mapping_table(labels_table,"data/mapping/labels.txt")  # save mapping file
	nums_of_labels = [str(x) for x in digitalize.labels2nums(labels, labels_table)]
	return nums_of_labels


if __name__ == '__main__':
	ftrain = "data/clean/train_clean.txt"
	ftest = "data/clean/test_clean.txt"
	ftrain_key = "data/clean/train_key.txt"
	ftest_key = "data/clean/test_key.txt"

	begin = datetime.datetime.now()
	# train_text = io.load(ftrain)
	# train_text = convert_features(train_text)
	# io.save(train_text, "data/input/train.txt")
	# end = datetime.datetime.now()
	# print('convert_features finished in ' + str((end - begin).seconds) + ' s!')
	#
	# test_text = io.load(ftest)
	# test_text = convert_features(test_text)
	# io.save(test_text, "data/input/test.txt")
	# end = datetime.datetime.now()
	# print('convert_features finished in ' + str((end - begin).seconds) + ' s!')
	#
	# key_text = io.load(ftrain_key)
	# key_text = convert_labels(key_text)
	# io.save(key_text, "data/input/train_key.txt")
	# end = datetime.datetime.now()
	# print('convert_labels finished in ' + str((end - begin).seconds) + ' s!')

	key_text = io.load(ftest_key)
	key_text = convert_labels(key_text)
	io.save(key_text, "data/input/test_key.txt")
	end = datetime.datetime.now()
	print('convert_labels finished in ' + str((end - begin).seconds) + ' s!')

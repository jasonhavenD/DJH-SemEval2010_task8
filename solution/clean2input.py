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


def convert_features(text, file):
	'''
	:param text:list
	:param file:str
	:return:text:list
	'''
	features = extract.extract_features(text)
	# for f in features:
	# 	print(f)
	features_dataframe = digitalize.get_features_dataframe(features)
	props_table = digitalize.get_props_table(features_dataframe)
	digitalize.save_features_mapping_table(props_table, file)  # save mapping file
	nums_of_features = digitalize.features2nums(features_dataframe, props_table)
	normalized_features = normalize.normalize(nums_of_features)
	text = []
	for row in normalized_features.index:
		row_str = [str(x) for x in list(normalized_features.loc[row])]
		text.append(delimiter.join(row_str))
	return text


def convert_labels(text, file):
	'''
	:param text:list
	:param file:str
	:return:nums_of_labels:list
	'''
	labels = extract.extract_labels(text)
	labels_table = digitalize.get_labels_table(labels)
	digitalize.save_labels_mapping_table(labels_table, file)  # save mapping file
	nums_of_labels = [str(x) for x in digitalize.labels2nums(labels_table, labels)]
	return nums_of_labels


if __name__ == '__main__':
	ftrain_clean = "data/clean/train_clean.txt"
	ftest_clean = "data/clean/test_clean.txt"
	ftrain_clean_key = "data/clean/train_key.txt"
	ftest_clean_key = "data/clean/test_key.txt"

	ftrain_input = "data/input/train_input.txt"
	ftest_input = "data/input/test_input.txt"
	ftrain_input_keys = "data/input/train_key.txt"
	ftest_input_keys = "data/input/test_key.txt"

	ftrain_features_mapping = "data/mapping/train_features.txt"
	ftest_features_mapping = "data/mapping/test_features.txt"
	ftrain_keys_mapping = "data/mapping/train_labels.txt"
	ftest_keys_mapping = "data/mapping/test_labels.txt"

	begin = datetime.datetime.now()
	# train_text = io.load(ftrain_clean)
	# train_text = convert_features(train_text, ftrain_features_mapping)
	# io.save(train_text, ftrain_input)
	# end = datetime.datetime.now()
	# print('convert_features finished in ' + str((end - begin).seconds) + ' s!')
	#
	# test_text = io.load(ftest_clean)
	# test_text = convert_features(test_text, ftest_features_mapping)
	# io.save(test_text, ftest_input)
	# end = datetime.datetime.now()
	# print('convert_features finished in ' + str((end - begin).seconds) + ' s!')

	key_text = io.load(ftrain_clean_key)
	key_text = convert_labels(key_text, ftrain_keys_mapping)
	io.save(key_text, ftrain_input_keys)
	end = datetime.datetime.now()
	print('convert_labels finished in ' + str((end - begin).seconds) + ' s!')

	key_text = io.load(ftest_clean_key)
	key_text = convert_labels(key_text, ftest_keys_mapping)
	io.save(key_text, ftest_input_keys)
	end = datetime.datetime.now()
	print('convert_labels finished in ' + str((end - begin).seconds) + ' s!')

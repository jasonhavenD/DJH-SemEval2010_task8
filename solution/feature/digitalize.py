#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:svm
   Author:admin
   date:2018/4/8
-------------------------------------------------
   Change Activity:2018/4/8:
-------------------------------------------------
"""
from extract import *
import pandas as pd




def get_features_dataframe(features):
	'''
	:param features:list
	:return:features_dataframe:DataFrame
	'''
	features_data = []  # data of dataframe
	features_keys = list(features[0].keys())  # key of features

	for item in features:
		feature = []
		for key in features_keys:
			feature.append(item[key])
		features_data.append(feature)
	# print(features_data)

	features_dataframe = pd.DataFrame(features_data, columns=features_keys)
	return features_dataframe


def get_props_table(features_dataframe):
	'''
	:param features_dataframe:DataFrame
	:return:props_table:dict
	'''
	props_table = {}  # table of props,which aim to trans prop to num
	for prop_key in features_dataframe.columns:
		# print(set(features_dataframe[prop_key]))
		props = sorted(set(features_dataframe[prop_key]))
		props_table[prop_key] = props
	return props_table

def labels2nums(labels):
	'''
	:param labels:list
	:return:nums_of_labels:list
	'''
	labels_table = sorted(set(labels))
	nums_of_labels = []
	for label in labels:
		nums_of_labels.append(labels_table.index(label)+1)
	return nums_of_labels

def features2nums(features_dataframe, props_table):
	'''
	:param features_dataframe:DataFrame
	:param props_table:dict
	:return:nums_of_features:DataFrame
	'''
	nums_of_features = pd.DataFrame(columns=features_dataframe.columns)
	for prop_key in features_dataframe.columns:
		values_of_props = features_dataframe[prop_key]
		nums_of_props = props2nums(props_table, values_of_props, prop_key)
		nums_of_features[prop_key] = nums_of_props
	return nums_of_features


def props2nums(props_table, values_of_props, prop_key):
	'''
	:param props_table:dict
	:param values_of_props:list or Series
	:param prop_key:str
	:return:nums_of_props:list
	'''
	nums_of_props = []
	for value in values_of_props:
		nums_of_props.append(props_table[prop_key].index(value)+1)
	return nums_of_props


if __name__ == '__main__':
	train_sents = [
		'1	"The system as described above has its greatest application in an arrayed <e1>configuration</e1> of antenna <e2>elements</e2>."',
		'2	"The <e1>child</e1> was carefully wrapped and bound into the <e2>cradle</e2> by means of a cord."',
		'3	"The <e1>author</e1> of a keygen uses a <e2>disassembler</e2> to look at the raw assembly code."']

	# features = extract_features(train_sents)
	# features_dataframe = get_features_dataframe(features)
	# props_table = get_props_table(features_dataframe)
	# print(features2nums(features_dataframe, props_table))

	train_keys = [
		'1	Component - Whole(e2, e1)',
		'2	Other',
		'3	Instrument - Agency(e2, e1)'
	]
	labels = extract_labels(train_keys)
	print(labels2nums(labels))

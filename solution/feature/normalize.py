#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:smooth
   Author:admin
   date:2018/4/9
-------------------------------------------------
   Change Activity:2018/4/9:
-------------------------------------------------
"""
from digitalize import *
from extract import *
import pandas as pd


def normalize(nums_of_features):
	normalized_features = pd.DataFrame(columns=nums_of_features.columns)
	for key in nums_of_features.columns:
		a = nums_of_features[key] - nums_of_features[key].mean()
		b = nums_of_features[key].std()
		if b == 0:
			normalized_features[key] = 0
			continue
		normalized_features[key] = a / b
	return normalized_features


if __name__ == '__main__':
	train_sents = [
		'1	"The system as described above has its greatest application in an arrayed <e1>configuration</e1> of antenna <e2>elements</e2>."',
		'2	"The <e1>child</e1> was carefully wrapped and bound into the <e2>cradle</e2> by means of a cord."',
		'3	"The <e1>author</e1> of a keygen uses a <e2>disassembler</e2> to look at the raw assembly code."']
	features = extract_features(train_sents)
	features_dataframe = get_features_dataframe(features)
	props_table = get_props_table(features_dataframe)
	nums_of_features = features2nums(features_dataframe, props_table)
	print(normalize(nums_of_features))

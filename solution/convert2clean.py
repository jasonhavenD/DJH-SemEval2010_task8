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
'''
从训练语料中抽取出指定格式的句子+标签
保存到指定文件中
'''

delimiter = "\t"


def load(file):
	text = []
	with open(file, "r", encoding="utf-8") as f:
		raw = f.read()
		for lines in raw.split("\n\n"):
			try:
				if len(lines.split("\n")) < 3:
					print("lines empty or format error!\n", lines)
					continue
				sent, relation, comment = lines.split("\n")
				item = {}
				item['sent'] = sent.strip()
				item['relation'] = sent.split(delimiter)[0] + delimiter + relation.strip()
				item['comment'] = comment.strip()
				# print(item)
				text.append(item)
			except Exception as e:
				print(e)
	return text


def save(text, file):
	with open(file, "w", encoding="utf-8") as f:
		for line in text:
			f.write(line + "\n")


def convert(text):
	sents = []
	relations = []
	for item in text:
		sents.append(item['sent'])
		relations.append(item['relation'])
	return sents, relations


if __name__ == '__main__':
	filename = "data/TRAIN_FILE_FULL.TXT"
	text = load(filename)
	sents, relations = convert(text)
	save(sents, "data/clean/train_clean.txt")
	save(relations, "data/clean/train_key.txt")

	filename = "data/TEST_FILE_FULL.TXT"
	text = load(filename)
	sents, relations = convert(text)
	save(sents, "data/clean/test_clean.txt")
	save(relations, "data/clean/test_key.txt")

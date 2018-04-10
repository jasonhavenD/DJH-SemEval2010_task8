#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:ioutil
   Author:admin
   date:2018/4/10
-------------------------------------------------
   Change Activity:2018/4/10:
-------------------------------------------------
"""
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
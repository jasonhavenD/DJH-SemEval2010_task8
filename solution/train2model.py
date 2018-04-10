#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:train2model
   Author:admin
   date:2018/4/8
-------------------------------------------------
   Change Activity:2018/4/8:
-------------------------------------------------
"""
from ioutil import io
import datetime

if __name__ == '__main__':
	ftrain = "data/input/train.txt"
	fkey = "data/input/key.txt"
	fmodel = "data/model/model.txt"

	begin = datetime.datetime.now()

	train_text = io.load(ftrain)
	key_text = io.load(fkey)

	print(key_text[:5])



	end = datetime.datetime.now()
	print('train2model finished in ' + str((end - begin).seconds) + ' s!')

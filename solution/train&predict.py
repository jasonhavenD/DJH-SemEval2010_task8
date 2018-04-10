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
import sys

sys.path.append('libsvm-3.22\python')

from ioutil import io
import datetime
from svmutil import *

if __name__ == '__main__':
	begin = datetime.datetime.now()
	train_label, train_value = svm_read_problem("data/input/train-FormatDatalibsvm.txt")  # 训练数据集
	predict_label, predict_value = svm_read_problem("data/input/test-FormatDatalibsvm.txt")  # 预测数
	model = svm_train(train_label, train_value)  # 训练模型
	svm_save_model("data/model/model.txt", model)  # 保存模型
	p_label, p_acc, p_val = svm_predict(predict_label, predict_value, model)
	print(p_acc)
	end = datetime.datetime.now()
	print('train2model finished in ' + str((end - begin).seconds) + ' s!')

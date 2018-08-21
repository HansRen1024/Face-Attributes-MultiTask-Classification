#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:35:42 2017

@author: hans

http://blog.csdn.net/renhanchi
"""

import matplotlib.pyplot as plt
import numpy as np
import commands
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-p','--log_path',
    type = str,
    default = 'mcnn-face-attri.log',
    help = """\
    path to log file\
    """
)

FLAGS = parser.parse_args()
train_log_file = FLAGS.log_path
display = 10 #solver
test_interval = 1000 #solver
time = 5
def reduce_data(data):
  iteration = len(data)/time*time
  _data = data[0:iteration]
  ind=0
  if time > 1:
    data_ = []
    for i in np.arange(len(data)/time):
      sum_data = 0
      for j in np.arange(time):
        ind = i*time + j
        sum_data += float(_data[ind])
      data_.append(sum_data/float(time))
  else:
    data_ = data
  return data_

def process(label,index):
	train_output = commands.getoutput("cat " + train_log_file + " | grep 'Train net output #%d' | awk '{print $11}'" %index)  #train mbox_loss
	accu_output = commands.getoutput("cat " + train_log_file + " | grep 'Test net output #%d' | awk '{print $11}'" %index) #test detection_eval
	train_loss = train_output.split("\n")
	test_accu = accu_output.split("\n")
	_train_loss = reduce_data(train_loss)
	_test_accu = reduce_data(test_accu)
	_,ax1 = plt.subplots()
	ax1.set_title(label)
	ax2 = ax1.twinx()
	ax1.plot(time*display*np.arange(len(_train_loss)), _train_loss)
	ax2.plot(time*test_interval*np.arange(len(_test_accu)), _test_accu, 'r')
	ax1.set_xlabel('Iteration')
	ax1.set_ylabel('%s Train Loss' %label)
	ax2.set_ylabel('%s Test Accuracy' %label)
if __name__ == '__main__':
	process('Bangs',0)
	process('Egeglasses',1)
	process('Gender',2)
	plt.show()
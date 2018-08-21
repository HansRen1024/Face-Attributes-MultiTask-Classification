#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 18:13:22 2018

@author: hans
"""

import sys
sys.path.append('.')
sys.path.append('/home/hans/caffe/python')
import cv2
import caffe
import numpy as np
deploy = './models/deploy_mcnn_Attri.prototxt'
caffemodel = './models/mcnn_iter_5000.caffemodel'
net_mcnn = caffe.Net(deploy,caffemodel,caffe.TEST)
caffe.set_device(0)
caffe.set_mode_gpu()
def faceAttri(img):
    caffe_img = (img.copy()-127.5)*0.007843
    caffe_img = cv2.resize(caffe_img,(227,227))
    caffe_img = np.swapaxes(caffe_img, 0, 2)
    net_mcnn.blobs['data'].reshape(1,3,227,227)
    net_mcnn.blobs['data'].data[...]=caffe_img
    out = net_mcnn.forward()
    accuracy_Eyeglasses = out['accuracy_Eyeglasses'].reshape(2,)
    accuracy_Bangs = out['accuracy_Bangs'].reshape(2,)
    accuracy_Male = out['accuracy_Male'].reshape(2,)
    return accuracy_Eyeglasses,accuracy_Bangs,accuracy_Male
if __name__=='__main__':
    FaceImg=cv2.imread('imgpath')
    accuracy_Eyeglasses,accuracy_Bangs,accuracy_Male = faceAttri(FaceImg)
    order_Eyeglasses = accuracy_Eyeglasses.argsort()[-1]
    order_Bangs = accuracy_Bangs.argsort()[-1]
    order_Male = accuracy_Male.argsort()[-1]
    if order_Eyeglasses==0:
        glasses='no glasses'
    else:
        glasses='with glasses'
    if order_Bangs==0:
        bangs='no bangs'
    else:
        bangs='with bangs'
    if order_Male==0:
        gender='female'
    else:
        gender='male'
    print glasses+','+bangs+','+gender

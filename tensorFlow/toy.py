from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time

import numpy as np
import tensorflow as tf
import collections
import os
import math
from decimal import *

def main(_):   
    dim = 2
    vocab = 10
    batch = 3
    precision = tf.float32

    em = np.zeros((vocab,dim),dtype=np.float32)
    for i in range(vocab):
        em[i,0] = float(1.0) + float(i/10)
        em[i,1] = float(2.0) + float(i/10)
    out = np.zeros((batch,dim),dtype=np.float32)
    
    out[0,0] = float(3.0)
    out[0,1] = float(4.0)
    out[1,0] = float(5.0)
    out[1,1] = float(6.0)
    out[2,0] = float(7.0)
    out[2,1] = float(8.0)
    
    in_num = np.random.rand(2,3,4)
    out_word = np.ones((2,4),dtype = np.float32)
       
    gpu_opt = tf.GPUOptions(per_process_gpu_memory_fraction=0.1)
    
    with tf.Graph().as_default(), tf.Session(config=tf.ConfigProto(gpu_options=gpu_opt)) as sess:
        
        embed = tf.Variable(em,dtype=precision,name="embed")
        output = tf.Variable(out,dtype=precision,name="output")
        print('embed = ',embed)
        print('output = ',output)
        
        temp = tf.slice(output,[0,0],[3,1])

        x = tf.reduce_sum(tf.multiply(embed,embed),1)
        x = tf.reshape(x,[10,1])
        y = tf.matmul(embed,tf.transpose(output))
        z = tf.transpose(tf.reduce_sum(tf.multiply(output,output),1))
        z = tf.reshape(z,[1,3])
        print('x = ',x)
        print('y = ',y)
        print('z = ',z)
        
        tf.initialize_all_variables().run()
     
        T = sess.run([temp])
        print('temp = ',T)
        
        X,Y,Z = sess.run([x,y,z],{})       
        print('X = ',X)
        print('Y = ',Y)
        print('Z = ',Z)
        
            
if __name__ == "__main__":
  tf.app.run()
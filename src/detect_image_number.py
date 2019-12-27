# Detect a number from an image using a convolutional neural network
# Network structure and inspiration from 'Deep MNIST for Experts'
# https://www.tensorflow.org/versions/r1.1/get_started/mnist/pros

import tensorflow as tf
import numpy as np
#import scipy.ndimage
from matplotlib.pyplot import imread
import sys
import json

# Comment one of the imports
# PYTHON 2 IMPORT
#from network import network
# PYTHON 3 IMPORT
from .network.network import network

def detect_image_number(image_path):

	# Create network and retrieve required parameters
	y_conv, x, _y, keep_prob = network()

	# Restore the model
	saver = tf.train.Saver()
	sess = tf.InteractiveSession()
	saver.restore(sess, "model/model.ckpt")

	# Flatten test image
	data = np.ndarray.flatten(imread(image_path))

	# Debug
	raw_predict = sess.run(y_conv, feed_dict={x: [data], keep_prob: 1.0})

	# Test the image
	results = sess.run(tf.argmax(y_conv, 1), feed_dict={x: [data], keep_prob: 1.0})
	sess.close()

	# Return raw data and prediction
	pred = ''.join(map(str, results))
	return {"raw": raw_predict[0].tolist(), "prediction": pred}













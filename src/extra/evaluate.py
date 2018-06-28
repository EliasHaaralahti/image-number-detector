# Evaluate a trained model using the MNIST dataset
# Network structure and inspiration from 'Deep MNIST for Experts'
# https://www.tensorflow.org/versions/r1.1/get_started/mnist/pros

import tensorflow as tf
import sys
import os

# Allow us to import from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from network import network

if len(sys.argv) != 2:
    print("Usage: python evaluate.py <MODEL_PATH>")
    print("Example: python evaluate.py ../../model/model.ckpt")
    sys.exit()

model_path = sys.argv[1]

sess = tf.InteractiveSession()

# MNIST dataset
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# Create network and retrieve required parameters
y_conv, x, y_, keep_prob = network()

# Restore the model
saver = tf.train.Saver()
saver.restore(sess, model_path)

# Test the model
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print("test accuracy %g" % accuracy.eval( feed_dict={
                                    x: mnist.test.images,
                                    y_: mnist.test.labels,
                                    keep_prob: 1.0}))















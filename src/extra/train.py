# Train a model using the MNIST dataset
# Network structure and inspiration from 'Deep MNIST for Experts'
# https://www.tensorflow.org/versions/r1.1/get_started/mnist/pros

import tensorflow as tf
import sys
import os

# Allow us to import from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from network import network

if len(sys.argv) != 2:
    print("Usage: python train.py <MODEL_SAVE_PATH>")
    print("Example: python train.py ../../model/model.ckpt")
    sys.exit()

model_save_path = sys.argv[1]

sess = tf.InteractiveSession()

# MNIST dataset
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# Create network and retrieve required parameters
y_conv, x, y_, keep_prob = network()

saver = tf.train.Saver()

# Training and testing parameters
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess.run(tf.global_variables_initializer())

# Training 20 000 steps, print accuracy every 100 steps
# 50 batches at a time
for i in range(20000):
  batch = mnist.train.next_batch(50)
  if i % 100 == 0:
    train_accuracy = accuracy.eval(feed_dict={
        x:batch[0], y_: batch[1], keep_prob: 1.0})
    print("step %d, training accuracy %g"%(i, train_accuracy))
  train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("test accuracy %g" % accuracy.eval(feed_dict={
                                x: mnist.test.images,
                                y_: mnist.test.labels, 
                                keep_prob: 1.0}))

# Save the model
save_path = saver.save(sess, model_save_path)
print("Model saved to: %s" % save_path)















from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

print(tf.version.VERSION)
print(tf.keras.__version__)

hello = tf.constant("hello world")

a = tf.constant(1)
b = tf.constant(2)
c = tf.constant(3)

with tf.Session() as sess:
    print("a: %i" % sess.run(a), "b: %i" % sess.run(b))
    print("Addition with constants: %i" % sess.run(a+b))
    print("Multiplication with constants: %i" % sess.run(a*b))

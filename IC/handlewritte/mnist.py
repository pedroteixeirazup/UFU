import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import matplolib.pyplot as plt

mnist = input_data.read_data_sets('mnist/', one_hot = False)

X_treinamento = mnist.train.images
Y_treinamento = mnist.train.labels
X_testes = mnist.test.images
Y_testes = mnist.test.labels

plt.imshow(X_treinamento[0].reshape(28,28))
plt.show()
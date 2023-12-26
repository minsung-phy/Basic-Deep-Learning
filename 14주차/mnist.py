import tensorflow as tf
import numpy as np

# download MNIST dataset
mnist = tf.keras.datasets.mnist

# load MNIST dataset and split to trainset and testset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize the image (0 ~ 255 => 0 ~ 1)
x_train, x_test = x_train / 255.0 , x_test / 255.0

# make neural network model
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)), tf.keras.layers.Dense(128, activation = 'relu'), tf.keras.layers.Dense(10, activation = 'softmax')])

# add training setting
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(x_train, y_train, epochs = 5)
model.evaluate(x_test, y_test, verbose = 2)
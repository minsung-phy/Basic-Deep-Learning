import tensorflow as tf
from keras.models import Model
import numpy as np
from keras.layers import *

# XOR data
x = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y = np.array([[0], [1], [1], [0]])

inputs = Input(shape = (2,)) # input tensor
hidden1 = Dense(units = 2, activation = 'sigmoid')(inputs) # hidden layer 1
outputs = Dense(units = 1, activation = 'sigmoid')(hidden1) # hidden layer 2

# define the model's start and end point 
model = Model(inputs, outputs)
model.compile(optimizer = tf.keras.optimizers.SGD(learning_rate = 0.1), loss = 'mse')
history = model.fit(x, y, epochs = 3000, batch_size = 1)
model.summary()
print(model.predict(x))
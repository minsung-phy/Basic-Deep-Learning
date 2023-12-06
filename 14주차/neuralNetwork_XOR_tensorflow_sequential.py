import tensorflow as tf
import numpy as np

# XOR data
x = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y = np.array([[0], [1], [1], [0]])

model = tf.keras.Sequential([tf.keras.layers.Dense(units = 2, activation = 'sigmoid', input_shape = (2,)), tf.keras.layers.Dense(units = 1, activation = 'sigmoid')])

model.compile(optimizer = tf.keras.optimizers.SGD(learning_rate = 0.1), loss = 'mse')
history = model.fit(x, y, epochs = 3000, batch_size = 1)
model.summary()
print(model.predict(x))


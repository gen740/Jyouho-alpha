import platform
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from util import *

x_test, y_test = np.loadtxt("./TBP_sim/build/data_for_learning/initial_value.csv",
                delimiter=" "), \
                np.loadtxt("./TBP_sim/build/data_for_learning/forward_step_data.csv",\
                delimiter=" ");

Dense = tf.keras.layers.Dense
Input = tf.keras.Input
# This is NN model
inputs = Input(shape=(15,))
x = Dense(3000, activation='sigmoid')(inputs)
x = Dense(3000, activation='sigmoid')(x)
x = Dense(3000, activation='sigmoid')(x)
x = Dense(3000, activation='sigmoid')(x)
x = Dense(3000, activation='sigmoid')(x)
x = Dense(3000, activation='sigmoid')(x)
x = Dense(3000, activation='sigmoid')(x)
x = Dense(3000, activation='sigmoid')(x)
output = Dense(120, activation='softmax')(x)
model = tf.keras.Model(inputs, output)
# compile
model.compile(
        loss='mean_squared_error',
        optimizer=tf.keras.optimizers.Adam(),
        metrics=["accuracy"],
        )
tf.keras.utils.plot_model(model,
                   show_shapes=True,
                   show_layer_names=True)

history = model.fit(x_test, y_test, batch_size=100, epochs=NUM_EPOCHS, verbose=1)

test_scores = model.evaluate(x_test, y_test, verbose=2)
print("test_loss", test_scores[0])
print("test_accuracy:", test_scores[1])

loss = history.history['loss']
val_loss = history.history['val_loss']
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

'''
plt.plot(range(epochs), loss, "b", label="train")
plt.plot(range(epochs), val_loss, "r", label="validate")
plt.legend()
plt.title("loss")
plt.show()

plt.plot(range(epochs), acc, "b", label="train")
plt.plot(range(epochs), val_acc, "r", label="validate")
plt.legend()
plt.title("accuracy")
plt.show()
'''

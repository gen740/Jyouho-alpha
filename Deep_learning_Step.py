import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
import tensorflow as tf
import keras
from keras.layers import Input, Dense, Dropout, Activation, Flatten, BatchNormalization, GlobalAveragePooling2D
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np

x_test, y_test = np.loadtxt("./TBP_sim/build/data_for_learning/Re_initial_value.csv",
        delimiter=" "), \
                 np.loadtxt("./TBP_sim/build/data_for_learning/Re_forward_step_data.csv",
                         delimiter=" ")

# データの整形
x_test, y_test = x_test/100, y_test/100

x_test_shape = x_test.shape
y_test_shape = y_test.shape

print(f"x_test_shape = {x_test_shape} : y_test_shape = {y_test_shape}")

inputs = Input(shape=(x_test_shape[1],))
x = Dense(32, activation='tanh')(inputs)
x = Dense(512, activation='tanh')(x)
x = Dense(1024, activation='tanh')(x)
x = Dense(2048, activation='tanh')(x)
x = Dense(4096, activation='tanh')(x)
x = Dense(8192, activation='tanh')(x)
x = Dense(16384, activation='tanh')(x)
x = Dense(32768, activation='tanh')(x)
x = Dense(32768, activation='tanh')(x)
x = Dense(32768, activation='tanh')(x)
x = Dense(16384, activation='tanh')(x)
x = Dense(8192, activation='tanh')(x)
x = Dense(4096, activation='tanh')(x)
x = Dense(4096, activation='tanh')(x)
x = Dense(3200, activation='tanh')(x)
x = Dense(3200, activation='tanh')(x)
output = Dense(y_test_shape[1], activation='tanh')(x)

model = keras.Model(inputs, output)
model.compile(
    loss='mean_absolute_error',
    optimizer=keras.optimizers.Adam(lr=0.00055, epsilon=None, decay=0.08, amsgrad=False),
    #optimizer=keras.optimizers.Nadam(lr=0.0003, beta_1=0.9, beta_2=0.999),#(lr=0.0003, epsilon=None, decay=0., amsgrad=False),
    #optimizer=keras.optimizers.SGD(lr=0.003, momentum=0.3, nesterov=False),
    metrics=["mean_squared_error"],
)

keras.utils.plot_model(model,
                       show_shapes=True,
                       show_layer_names=True)

epochs = 30
history = model.fit(x_test, y_test, batch_size=10, epochs=epochs, verbose=1, validation_split=0.2)

test_scores = model.evaluate(x_test, y_test, verbose=2)
print("テスト損失:", test_scores[0])
print("テスト精度（正答率）:", test_scores[1])

#loss = history.history['loss']
#val_loss = history.history['val_loss']
#acc = history.history['accuracy']
#val_acc = history.history['val_accuracy']

model.save_weights('./TBP_weight')

"""
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
"""

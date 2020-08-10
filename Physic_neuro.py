import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
import keras
from keras.layers import Input, Dense, Dropout, Activation, Flatten, BatchNormalization, GlobalAveragePooling2D
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np

x_test, y_test = np.loadtxt("./TBP_sim/build/data_for_learning/initial_value.csv",
        delimiter=" "), \
                 np.loadtxt("./TBP_sim/build/data_for_learning/forward_dt_data.csv",
                         delimiter=" ")
x_test, y_test = x_test/10, y_test/10

inputs = Input(shape=(15,),dtype='float32')
x = Dense(256, activation='tanh',dtype='float32')(inputs)
x = Dense(512, activation='tanh',dtype='float32')(x)
x = Dense(512, activation='tanh',dtype='float32')(x)
x = Dense(512, activation='tanh',dtype='float32')(x)
x = Dense(1024, activation='tanh',dtype='float32')(x)
x = Dense(1024, activation='tanh',dtype='float32')(x)
x = Dense(512, activation='tanh',dtype='float32')(x)
x = Dense(512, activation='tanh',dtype='float32')(x)
x = Dense(512, activation='tanh',dtype='float32')(x)
x = Dense(256, activation='tanh',dtype='float32')(x)
x = Dense(256, activation='tanh',dtype='float32')(x)
output = Dense(12, activation='tanh',dtype='float32')(x)

model = keras.Model(inputs, output)
model.compile(
    loss='mean_squared_error',
    optimizer=keras.optimizers.Adam(lr=0.0008, epsilon=None, decay=0.5, amsgrad=False),
    metrics=["accuracy"],
)

keras.utils.plot_model(model,
                       show_shapes=True,
                       show_layer_names=True)

epochs = 120
history = model.fit(x_test, y_test, batch_size=100, epochs=epochs, verbose=1)

test_scores = model.evaluate(x_test, y_test, verbose=2)
print("テスト損失:", test_scores[0])
print("テスト精度（正答率）:", test_scores[1])

loss = history.history['loss']
val_loss = history.history['val_loss']
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

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

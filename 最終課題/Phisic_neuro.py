from TB_problem import *
import platform
if platform.system() == "Darwin": #google colabo でやるか自分のPCでやっているかの判定
 import os
 os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
import keras
from keras.layers import Input, Dense, Dropout, Activation, Flatten, BatchNormalization, GlobalAveragePooling2D
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
import matplotlib.pyplot as plt

x_test, y_test = np.load("/Users/fujimotogen/Documents/GitHub/Jyouho-alpha/最終課題/x_test.npy"),\
                 np.load("/Users/fujimotogen/Documents/GitHub/Jyouho-alpha/最終課題/y_test.npy")

inputs = Input((16,))
x = Dense(300, activation='sigmoid')(inputs)
x = Dense(300, activation='sigmoid')(x)
x = Dense(300, activation='sigmoid')(x)
x = Dense(300, activation='sigmoid')(x)
x = Dense(300, activation='sigmoid')(x)
x = Dense(300, activation='sigmoid')(x)
x = Dense(300, activation='sigmoid')(x)
x = Dense(300, activation='sigmoid')(x)
output = Dense(12, activation='softmax')(x)

model = keras.Model(inputs, output)
model.compile(
    loss='mean_squared_error',
    optimizer=keras.optimizers.Adam(),
    metrics=["accuracy"],
)

keras.utils.plot_model(model,
                       show_shapes=True,
                       show_layer_names=True)

epochs = 10
history = model.fit(x_test, y_test, batch_size=1 ,epochs=epochs, verbose=1)

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


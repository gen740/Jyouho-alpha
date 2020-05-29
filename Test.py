import platform
if platform.system() == "Darwin":
  import os
  os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Input, Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

datagen = ImageDataGenerator(
    rotation_range=45,
    width_shift_range=0.15,
    height_shift_range=0.15,
    zca_whitening=True,
    zoom_range=0.4,
    horizontal_flip=True,
    validation_split=0.2)

x_train = x_train/255
x_test = x_test/255



for i in range(10):
    fig, ax = plt.subplots()
    ax.imshow(next(datagen.flow(x_train[0].reshape(1, 32, 32, 3), batch_size=1)).reshape(32, 32, 3))
    print(next(datagen.flow(x_train[0].reshape(1, 32, 32, 3), batch_size=1)).reshape(32, 32, 3))
    fig.savefig(f'/Users/fujimotogen/Desktop/outuput/fig{i}.png')
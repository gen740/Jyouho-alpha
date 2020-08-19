import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Dropout, Activation, Flatten, BatchNormalization, GlobalAveragePooling2D
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
import tensorflow.keras as keras
import matplotlib.pyplot as plt
import numpy as np
import datetime

def save_data():
    from keras.utils import to_categorical
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train = x_train.reshape(60000, 784).astype("float32") / 255
    x_test = x_test.reshape(10000, 784).astype("float32") / 255
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    model_zero = tf.keras.models.load_model('./Zero_Mnist_model')
    model_zero.summary()
    model_trained = tf.keras.models.load_model('./Mnist_model')
    model_trained.summary()

    Model_OV = np.loadtxt('./Model_OV.csv')
    layers = model_trained.layers[:]
    layers_zero = model_zero.layers[:]

    # 層数
    layer_size = len(layers) - 1
    print("層数 = ", layer_size)

    # パラメータ数
    param_size = model_trained.count_params()
    print("パラメータ数 = ", param_size)

    # 汎化誤差
    test_scores = model_trained.evaluate(x_test, y_test, verbose=2)
    test_loss = test_scores[0]
    test_acc = test_scores[1]
    print("テスト損失 = " ,test_loss ,"\nテスト正答率 = " ,test_acc )

    # データ数
    Data_size = Model_OV[0]
    print(Data_size)

    # A
    A = np.sqrt( param_size / Data_size)
    print("A = ", A)

    lay = layers[0]

    # B
    B = 1.
    for i in range(layer_size):
        lay = layers[i + 1]
        param_lay = np.array(lay.get_weights()[0])
        param_bias = np.array(lay.get_weights()[1])
        B *= np.linalg.norm(param_lay) * np.linalg.norm(param_bias)
    B = B / Data_size
    print("B = ", B)

    # C
    C = 0.
    for i in range(layer_size):
        lay = layers[i + 1]
        lay_zero = layers_zero[i + 1]
        param_lay = np.array(lay.get_weights()[0])
        param_bias = np.array(lay.get_weights()[1])
        param_lay_zero = np.array(lay_zero.get_weights()[0])
        param_bias_zero = np.array(lay_zero.get_weights()[1])
        C += np.linalg.norm(param_lay - param_lay_zero) + \
                np.linalg.norm(param_bias - param_lay_zero)
    C = C / Data_size
    print("C = ", C)

    data = [layer_size, param_size, test_loss, test_acc, Data_size, A, B, C]
    del model_zero
    del model_trained
    del layers
    del layers_zero
    del lay
    return data

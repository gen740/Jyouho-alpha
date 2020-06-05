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

a = np.array([random_default() for i in range(10000)])
np.save("/Users/fujimotogen/Documents/GitHub/Jyouho-alpha/最終課題/test", a)
print(np.array([calc_TBP(i) for i in a]))

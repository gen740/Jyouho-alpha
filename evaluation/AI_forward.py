import platform
system = platform.system()
print(system)
if system == "Darwin":
    import os
    os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
    import tensorflow as tf
    import keras
    from keras.layers import Input, Dense, Dropout, Activation, Flatten, BatchNormalization, GlobalAveragePooling2D
    from keras.layers import Conv2D, MaxPooling2D
    from keras.utils import to_categorical
    import matplotlib.pyplot as plt
    import numpy as np
else:
    import tensorflow.keras as keras
    from keras.layers import Input, Dense, Dropout, Activation, Flatten, BatchNormalization, GlobalAveragePooling2D
    from keras.layers import Conv2D, MaxPooling2D
    from keras.utils import to_categorical
    import matplotlib.pyplot as plt
    import numpy as np
    import datetime

new_model = tf.keras.models.load_model('../weight/TBP_08_19_15:18:04_0.046320244669914246_model')
new_model.summary()

initial_val = np.loadtxt("../evaluation/TBP_sim/build/data_for_evaluation/initial_value_for_ai.csv")
initial_shape = initial_val.shape
initial_val = initial_val.reshape(initial_shape[0] * int(initial_shape[1]/3), 3)
result = new_model.predict(initial_val[:].reshape(initial_shape[0] * int(initial_shape[1]/3),3))

result_shape = result.shape
x_1 = result[:,[True,True,False,False]]
x_2 = result[:,[False,False,True,True]]
x_3 = - x_1 - x_2

result = np.concatenate([x_1,x_2,x_3],1)
result_shape = result.shape
print(result)
print(result_shape)

x_1 = x_1.reshape(initial_shape[0],int(initial_shape[1]/3),2)
x_2 = x_2.reshape(initial_shape[0],int(initial_shape[1]/3),2)
x_3 = x_3.reshape(initial_shape[0],int(initial_shape[1]/3),2)


for i in range(100):
    star1_data = x_1[i]
    star2_data = x_2[i]
    star3_data = x_3[i]


    fig, ax = plt.subplots(dpi = 400, figsize=(10,8))

    ax.plot(star1_data[:,0],star1_data[:,1],"g-", markersize = 0.4)
    ax.plot(star2_data[:,0],star2_data[:,1],"r-", markersize = 0.4)
    ax.plot(star3_data[:,0],star3_data[:,1],"b-", markersize = 0.4)

    fig.savefig(f"./Graph/AI-figure{i + 1}.png")
    plt.clf()
    fig.clf()

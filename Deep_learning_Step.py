import platform
system = platform.system()
print(system)
if system == "Darwin":
    import os
    os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
    import tensorflow as tf
    import keras as keras
    from keras.layers import Input, Dense, Dropout, Activation, Flatten, BatchNormalization, GlobalAveragePooling2D
    from keras.layers import Conv2D, MaxPooling2D
    from keras.utils import to_categorical
    import matplotlib.pyplot as plt
    import numpy as np
    import datetime
else:
    from tensorflow.keras.layers import Input, Dense, Dropout, Activation, Flatten, BatchNormalization, GlobalAveragePooling2D
    from tensorflow.keras.layers import Conv2D, MaxPooling2D
    from tensorflow.keras.utils import to_categorical
    import tensorflow.keras as keras
    import matplotlib.pyplot as plt
    import numpy as np
    import datetime

x_test, y_test = np.loadtxt("./TBP_sim/build/data_for_learning/Re_initial_value.csv",
        delimiter=" "), \
                 np.loadtxt("./TBP_sim/build/data_for_learning/Re_forward_step_data.csv",
                         delimiter=" ")

# データの整形
x_test, y_test = x_test, y_test

x_test_shape = x_test.shape
y_test_shape = y_test.shape

print(f"x_test_shape = {x_test_shape} : y_test_shape = {y_test_shape}")

inputs = Input(shape=(x_test_shape[1],))
x = Dense(256, activation='relu')(inputs)
x = Dense(256, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(512, activation='relu')(x)
x = Dense(512, activation='relu')(x)
x = Dense(512, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(256, activation='relu')(x)
output = Dense(y_test_shape[1], activation='linear')(x)

model = keras.Model(inputs, output)
model.compile(
    loss='mean_squared_error',
    optimizer=keras.optimizers.Adam(lr=0.0008, epsilon=None, decay=0.001, amsgrad=False),
    #optimizer=keras.optimizers.Nadam(lr=0.0003, beta_1=0.9, beta_2=0.999),#(lr=0.0003, epsilon=None, decay=0., amsgrad=False),
    #optimizer=keras.optimizers.SGD(lr=0.003, momentum=0.3, nesterov=False),
    metrics=["mean_absolute_error"],
)

keras.utils.plot_model(model,
                       show_shapes=True,
                       show_layer_names=True)

epochs = 1000
history = model.fit(x_test, y_test, batch_size=40, epochs=epochs, verbose=1, validation_split=0.2)

test_scores = model.evaluate(x_test, y_test, verbose=2)
print("テスト損失:", test_scores[0])
print("テスト精度（正答率）:", test_scores[1])

dt_now = datetime.datetime.now()
s_date = dt_now.strftime('_%m_%d_%H:%M:%S')
model.save_weights(f'./weight/TBP{s_date}_weight')
model.save(f'./weight/TBP{s_date}_{test_scores[1]}_model')

fig, ax = plt.subplots(dpi = 100, figsize=(18,9))
fig2, ax2 = plt.subplots(dpi = 100, figsize=(18,9))

loss = history.history['loss']
val_loss = history.history['val_loss']
acc = history.history['mean_absolute_error']
val_acc = history.history['val_mean_absolute_error']

ax.plot(range(epochs),loss,"b-", linewidth=0.5, label="train")
ax.plot(range(epochs),val_loss,"r-", linewidth=0.5, label="validate")
ax.legend()
ax.set_title("loss")
fig.show()
fig.savefig(f"./Graphs/loss_graph{s_date}.png")

ax2.plot(range(epochs),acc,"b-", linewidth=0.5, label="train")
ax2.plot(range(epochs),val_acc,"r-", linewidth=0.5, label="validate")
ax2.legend()
ax2.set_title("mean_absolute_error")
fig2.show()
fig2.savefig(f"./Graphs/error_graph{s_date}.png")
plt.show()

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
    import tensorflow as tf

def AI_learning(dim_of_layer, middle_lay_size, size_of_data = 60000):
    input_dim = 28*28
    middle_dim = dim_of_layer
    output_dim = 10
    DATA_SIZE = size_of_data
    val_split = 0.1

    from tensorflow.keras.utils import to_categorical
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.reshape(60000, 784).astype("float32") / 255
    x_test = x_test.reshape(10000, 784).astype("float32") / 255
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    x_train, y_train = x_train[0:DATA_SIZE,:], y_train[0:DATA_SIZE,:]

    inputs = Input(shape=(input_dim,), name="Input")
    x = inputs
    if middle_lay_size == 1:
        pass
    else:
        for i in range(middle_lay_size - 1):
            x = Dense(middle_dim, activation="relu")(x)
    outputs = Dense(output_dim, activation='softmax')(x)

    model = keras.Model(inputs=inputs, outputs=outputs, name="MNIST") #入力と出力だけ指定すればOK
    model.summary()

    model.compile(
        loss="categorical_crossentropy", #ここでクロスエントロピーを指定
        optimizer=keras.optimizers.Adam(lr=0.0005, decay=0.0005), #学習アルゴリズムにAdamを指定
        metrics=["acc"], #性能評価にaccuracyを指定
    )

    model.save_weights(f'./Zero_Mnist_weight')
    model.save(f'./Zero_Mnist_model')

    epochs = 100 #エポック数（全データを概ねチェックして更新する回数）を指定
    history = model.fit(x_train, y_train, batch_size=64, epochs=epochs, validation_split=val_split)

    test_scores = model.evaluate(x_test, y_test, verbose=2)
    print("テスト損失:", test_scores[0])
    print("テスト精度（正答率）:", test_scores[1])

    # dt_now = datetime.datetime.now()
    # s_date = dt_now.strftime('_%m_%d_%H:%M:%S')
    model.save_weights(f'./Mnist_weight')
    model.save(f'./Mnist_model')

    DATA_OV = np.array([DATA_SIZE*(1-val_split), 0.00])
    
    np.savetxt('Model_OV.csv', DATA_OV)

    del model

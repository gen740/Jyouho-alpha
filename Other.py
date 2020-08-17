import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
import numpy as np

x_test, y_test = np.loadtxt("./TBP_sim/build/data_for_learning/initial_value.csv",
        delimiter=" "), \
                 np.loadtxt("./TBP_sim/build/data_for_learning/forward_step_data.csv",
                         delimiter=" ")

x_test, y_test = x_test/10, y_test/10

print(y_test.shape)
x_2 = x_test[:,5:10] - x_test[:,0:5]
x_3 = x_test[:,10:15] - x_test[:,0:5]

x_test = np.concatenate([x_2[:,1:5],x_3[:,1:5]],1)

y_2 = y_test[:,4:8] - y_test[:,0:4]
y_3 = y_test[:,8:12] - y_test[:,0:4]

y_test = np.concatenate([y_2[:,0:4],y_3[:,0:4]],1)

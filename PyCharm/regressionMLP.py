import tensorflow as tf
from tensorflow.keras.optimizers  import SGD
from keras import layers
from keras import models
from keras.callbacks import CSVLogger
import numpy as np
# import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

housing = fetch_california_housing()

X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data, housing.target, random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_valid = scaler.transform(X_valid)
X_test = scaler.transform(X_test)

np.random.seed(42)
tf.random.set_seed(42)

input_ = layers.Input(shape=X_train.shape[1:])
hidden1 = layers.Dense(30, activation="relu")(input_)
hidden2 = layers.Dense(30, activation="relu")(hidden1)
concat = layers.concatenate([input_, hidden2])
output = layers.Dense(1)(concat)
model = models.Model(inputs=[input_], outputs=[output])

print(model.summary())

model.compile(loss="mean_squared_error", optimizer=SGD(learning_rate=1e-3))

# X_train_A, X_train_B = X_train[:, :5], X_train[:, 2:]
# X_valid_A, X_valid_B = X_valid[:, :5], X_valid[:, 2:]
# X_test_A, X_test_B = X_test[:, :5], X_test[:, 2:]
# X_new_A, X_new_B = X_test_A[:3], X_test_B[:3]

csvLogger = CSVLogger("model_log.csv")
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_valid, y_valid), callbacks=csvLogger)
model.save("regressionMLP_model.h5")
print(model.summary())
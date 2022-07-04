import tensorflow as tf
from PIL import Image
from keras.models import model_from_json
from keras.optimizers import adam_v2 as adam
from tensorflow.python.keras.layers import Activation, Flatten, Dense
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, GlobalMaxPooling2D, BatchNormalization
from tensorflow.python.keras.models import Sequential
from base.base_model import BaseModel


class CNNModel(BaseModel):
    def __init__(self, config):
        super(CNNModel, self).__init__(config)

    def build_model(self):
        self.model = Sequential()
        self.model.add(Conv2D(32, (3, 3), input_shape=self.config.config.model.input_shape, activation='linear'))
        self.model.add(BatchNormalization())
        self.model.add(Activation('relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Conv2D(32, (3, 3), activation='linear'))
        self.model.add(BatchNormalization())
        self.model.add(Activation('relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(BatchNormalization())
        self.model.add(Activation('relu'))
        self.model.add(GlobalMaxPooling2D())

        self.model.add(Flatten())
        self.model.add(Dense(128, activation='linear'))
        self.model.add(BatchNormalization())
        self.model.add(Activation('relu'))
        self.model.add(Dense(1, activation='sigmoid'))

        self.model.optimizer = adam.Adam()
        self.model.compile(loss='binary_crossentropy',
                           optimizer=self.config.config.model.optimizer,
                           metrics=[tf.keras.metrics.BinaryAccuracy(), tf.keras.metrics.AUC()])

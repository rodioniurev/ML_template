from tensorflow import keras
import numpy as np
from keras.utils.image_utils import load_img
import pandas as pd


class DataLoader(keras.utils.Sequence):
    """Helper to iterate over the data (as Numpy arrays)."""

    # DataLoader(config.train_data)

    def __init__(self, config):
        self.batch_size = config.batch_size
        self.img_size = config.image_size
        df = pd.read_csv(config.path_file_csv, encoding='utf8', sep=';', index_col=False)
        self.input_image_class = df.image_class.tolist()
        self.input_image_paths = df.image_paths.tolist()

    def __len__(self):  # сколько батчей в выборке этот метод в керасе есть, тут переопределяем
        return len(self.input_image_paths) // self.batch_size

    def normalize_x(self, x) -> np.array():
        return x  # здесь надо написать алгоритм обработки

    def augmentate_x(self, x) -> np.array():
        return x

    def __getitem__(self, idx):
        """Returns tuple (input, target) correspond to batch #idx."""
        i = idx * self.batch_size
        batch_input_image_class = self.input_image_class[i: i + self.batch_size]
        batch_input_image_paths = self.input_image_paths[i: i + self.batch_size]
        x = np.zeros((self.batch_size,) + self.img_size + (3,), dtype="float32") # это форма для записи тупля
        # тут выделяется память под батч, имжсайз - это размер сайт, 3 - это ргб

        for j, path in enumerate(batch_input_image_paths):
            img = load_img(path, target_size=self.img_size)  # следить за последовательностью: высота-ширина
            x[j] = img
        x = self.augmentate_x(x)
        x = self.normalize_x(x)  # альтернативный вариант - делать в цикле нормализацию каждого изображения
        # препроцесс x важная штука
        y = np.zeros((self.batch_size, 1), dtype="float32")
        # делается такая же матрица для сегментации, здесь -- бинарная, поэтому 1
        # тут сложение туплов
        for j, cls in enumerate(batch_input_image_class):
            y[j] = cls
        return x, y

# Prepare U-Net Xception-style

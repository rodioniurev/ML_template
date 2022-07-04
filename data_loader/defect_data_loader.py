from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.image import load_img

from base.base_data_loader import BaseDataLoader


class ImageDataLoader(BaseDataLoader, keras.utils.Sequence):
    """Helper to iterate over the data (as Numpy arrays).OxfordPets"""

    def __init__(self, config):
        super(ImageDataLoader, self).__init__(config)
        super(BaseDataLoader, self).__init__(config)
        self.batch_size = config.model.batch_size
        self.img_size = config.model.img_size
        self.input_img_paths = config.model.input_img_paths
        self.target_img_paths = config.model.target_img_paths

    def __len__(self): # сколько батчей в выборке
        return len(self.target_img_paths) // self.batch_size

    def __getitem__(self, idx):
        """Returns tuple (input, target) correspond to batch #idx."""
        i = idx * self.batch_size
        batch_input_img_paths = self.input_img_paths[i : i + self.batch_size]
        batch_target_img_paths = self.target_img_paths[i : i + self.batch_size]
        target_img_class = self.config.y_file[i:i+self.batch_size]
        x = np.zeros((self.batch_size,) + self.img_size + (3,), dtype="float32")
        # тут выделяется память под батч, имжсайз - это размер сайт, 3 - это ргб
        for j, path in enumerate(batch_input_img_paths):
            img = load_img(path, target_size=self.img_size)
            x[j] = img
        y = np.zeros((self.batch_size,) + self.img_size + (1,), dtype="uint8")
        # делается такая же матрица для сегментации, здесь -- бинарная, поэтому 1
        # тут сложение туплов
        for j, path in enumerate(batch_target_img_paths):
            img = load_img(path, target_size=self.img_size, color_mode="grayscale")

            y[j] = np.expand_dims(img, 2)
            # Ground truth labels are 1, 2, 3. Subtract one to make them 0, 1, 2:
            y[j] -= 1
        return x, y
# Prepare U-Net Xception-style
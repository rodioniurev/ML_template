from abc import ABC, abstractmethod


class BaseDataLoader(ABC):
    """
    Abstract class for loading of data
    """
    def __init__(self, config):
        pass

    @abstractmethod
    def get_train_data(self):
        pass

    @abstractmethod
    def get_test_data(self):
        pass

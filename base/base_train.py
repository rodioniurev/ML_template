from abc import ABC, abstractmethod


class BaseTrain(ABC):
    """
    Abstract class for trainers
    """
    def __init__(self, model, data, config):
        self.model = model
        self.data = data
        self.config = config

    @abstractmethod
    def train(self):
        pass

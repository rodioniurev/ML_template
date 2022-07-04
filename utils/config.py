import os.path
import time

from dotmap import DotMap
from yaml import load, FullLoader


class Config:
    def __init__(self, yaml_file: str):
        """ Set the configuration in object
            :param yaml_file: string (path to file)
            :return: object of dotmap (with dot notation as: config.callbacks)
        """
        with open(yaml_file, 'r', encoding='utf8') as config_file:
            config = DotMap(load(config_file, Loader=FullLoader))
        config.callbacks.tensorboard.log_dir = os.path.join(
            'experiments',
            time.strftime("%Y-%m-%d/", time.localtime()),
            config.experiment.name,
            "logs/")
        config.callbacks.checkpoint_dir = os.path.join(
            "experiments",
            time.strftime("%Y-%m-%d/", time.localtime()),
            config.experiment.name,
            "checkpoints/")
        self.config = config

import os.path
import time

from dotmap import DotMap
from yaml import load, FullLoader


def get_config_from_yaml(yaml_file: str) -> object:
    """
    Set the configuration in object
    :param yaml_file: string (path to file)
    :return: object of dotmap (with dot notation as: config.callbacks)
    """
    with open(yaml_file, 'r', encoding='utf8') as config_file:
        return DotMap(load(config_file, Loader=FullLoader))


def set_config_dirs(yaml_file: str) -> object:
    """
    set path parameters for training
    :param yaml_file: str
    :return: object of config
    """
    config = get_config_from_yaml(yaml_file)
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
    return config


cfg = set_config_dirs('configs/cnn_model_1.yaml')

print(cfg.callbacks.modelcheckpoint.filepath, cfg.callbacks.write_graf, cfg.callbacks.tensorboard.log_dir)

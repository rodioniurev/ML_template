import time
from pathlib import Path
from dotmap import DotMap
from yaml import load, FullLoader


class Config:
    """
    Creating configuration from YAML file
    """

    def __init__(self, yaml_file: str):
        with open(yaml_file, 'r', encoding='utf8') as f:
            self.config = DotMap(load(f, Loader=FullLoader))
        local_date = time.strftime("%Y-%m-%d/", time.localtime())
        self.config.collbacks.tensorboard.log_dir = Path('experiments') \
                                                    / local_date \
                                                    / self.config.experiment.name \
                                                    / 'logs'
        self.config.collbacks.tensorboard.checkpoint_dir = Path('experiments') \
                                                           / local_date \
                                                           / self.config.experiment.name \
                                                           / 'checkpoints'

    def create_env(self, main_path=None):
        """
        Making the dirs for working and saving the results
        :return: None
        """
        main_path = Path(main_path) if main_path else Path.cwd()
        self.config.collbacks.tensorboard.log_dir = main_path / self.config.collbacks.tensorboard.log_dir
        self.config.collbacks.tensorboard.log_dir.mkdir(parents=True)
        self.config.collbacks.tensorboard.checkpoint_dir = main_path / self.config.collbacks.tensorboard.checkpoint_dir
        self.config.collbacks.tensorboard.checkpoint_dir.mkdir()

from utils import config

cfg = config.set_config_dirs('../configs/cnn_model_1.yaml')

print(f'filepath: {cfg.callbacks.modelcheckpoint.filepath=}\n'
      f'writeGraf: {cfg.callbacks.tensorboard.write_graph=}\n'
      f'LogDir: {cfg.callbacks.tensorboard.log_dir}')

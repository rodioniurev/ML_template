from utils.config import Config


config = Config('../configs/cnn_model_1.yaml').config

print(config.model.name)

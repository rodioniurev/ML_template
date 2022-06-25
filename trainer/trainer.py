from keras.callbacks import ModelCheckpoint, CSVLogger, TensorBoard

from base.base_train import BaseTrain


class DefectTrainer(BaseTrain):
    def __init__(self, model, data, config):
        super().__init__(model, data, config)
        self.callbacks = []
        self.loss = []
        self.acc = []
        self.val_loss = []
        self.val_acc = []
        self.init_callbacks()

    def init_callbacks(self):
        self.callbacks.append(
            [ModelCheckpoint(
                filepath=self.config.callbacks.modelcheckpoint.filepath,
                monitor=self.config.callbacks.modelcheckpoint.check_monitor,
                mode=self.config.callbacks.modelcheckpoint.checkpoint_mode,
                save_best_only=self.config.callbacks.modelcheckpoint.checkpoint_save_best_only,
                save_weights_only=self.config.callbacks.modelcheckpoint.checkpoint_save_weights_only,
                verbose=self.config.callbacks.modelcheckpoint.checkpoint_verbose,
            ),
                CSVLogger(
                    filename=self.config.callbacks.csvlogger.filename,
                    append=self.config.callbacks.csvlogger.append,
                    separator=self.config.callbacks.csvlogger.separator,
                ),
                TensorBoard(
                    log_dir=self.config.callbacks.tensorboard.log_dir,
                    write_graph=self.config.callbacks.tensorboard.write_graph,
                )
            ]
        )

    def train(self):



def train_model(model, train_generator, val_generator):
    # # балансировка классов
    # weight_for_0 = 0.015  # (1 / len(os.listdir(fr'{train_dir}/42'))) * (nb_train_samples / 2.0)
    # weight_for_1 = 0.04  # (1 / len(os.listdir(fr'{train_dir}/53'))) * (nb_train_samples / 2.0)
    # class_weights = {0: weight_for_0, 1: weight_for_1}
    # print('Class weights:', class_weights)


    model.fit(
        x=train_generator,
        steps_per_epoch=nb_train_samples // batch_size,
        epochs=epochs,
        validation_data=val_generator,
        validation_steps=nb_validation_samples // batch_size,
        callbacks=[model_checkpoint_callback, csv_logger],
        class_weight=class_weights
    )
    return model

import pandas as pd
from pathlib import Path
from random import shuffle


def prepare_csv(path_to_files: str, csv_name: str, path_to_csv: str = '') -> None:
    """
    Using
    prepare_csv(r'D:\datasets\03\learnset\21-12-14\test', 'test_1.csv', r'..\tests\\')
    """
    classes = {
        '42': 0,
        '53': 1
    }
    path = Path(path_to_files)
    files = list(path.glob('**/*.tiff'))
    shuffle(files)
    cls_list = []
    for i in files:
        cls = Path(i).parts[-2]
        cls_list.append(classes[cls])
    df = pd.DataFrame.from_dict({'image_class': cls_list,
                                 'image_paths': files})
    df.to_csv(f'{path_to_csv}{csv_name}', encoding='utf8', index=False)

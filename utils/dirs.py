from pathlib import Path


def create_dirs(dirs: list[str]) -> None:
    """
    dirs - a list of directories to create if these directories are not found
    :param dirs: list[str]
    Usage: create_dirs(['test_dir', 'test_2_dir'])
    """
    for dir_ in dirs:
        Path(dir_).mkdir(parents=True, exist_ok=True)

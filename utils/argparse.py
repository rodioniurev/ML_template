from argparse import ArgumentParser


def get_args():
    """
    Create the arguments string for command-line start
    :return: parsed arguments
    """
    argparser = ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-c', '--config',
        dest='config',
        metavar='C',
        default='None',
        help='The configuration file')
    return argparser.parse_args()

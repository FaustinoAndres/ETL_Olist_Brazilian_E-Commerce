from .extract import *

import logging
logging.basicConfig(filename='log.log', filemode='w', level=logging.INFO)

def pipeline():
    print(create_kaggle_config_dir())

if __name__ == '__main__':
    pipeline()
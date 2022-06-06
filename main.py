from extract import using_kaggle_api

import logging
logging.basicConfig(filename='log.log', filemode='w', level=logging.INFO)

def pipeline():
    print(using_kaggle_api())

if __name__ == '__main__':
    pipeline()
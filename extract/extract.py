import os

def using_kaggle_api(dataset='olistbr/brazilian-ecommerce'):

    pwd = os.getcwd()
    os.environ['KAGGLE_CONFIG_DIR'] = f'{pwd}/.kaggle'
    os.system(f'kaggle datasets download -d {dataset}')



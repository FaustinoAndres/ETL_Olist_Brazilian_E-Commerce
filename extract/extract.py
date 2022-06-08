import os
from zipfile36 import ZipFile

def download_data_from_kaggle(dataset: str = 'olistbr/brazilian-ecommerce') -> None:

    pwd = os.getcwd()
    os.environ['KAGGLE_CONFIG_DIR'] = f'{pwd}/.kaggle'
    os.system(f'kaggle datasets download -d {dataset}')

    path = pwd

    return (path, name_file)

def extract_data_from_zip_file(file_path: str, name_file: str) -> None:

    name_file = name_file.strip('.zip')
    
    with ZipFile(file_path, 'r') as zip:
        pass
        zip.printdir()
        zip.extractall()

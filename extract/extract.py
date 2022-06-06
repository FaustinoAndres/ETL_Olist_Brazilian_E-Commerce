import os
from zipfile36 import ZipFile

def download_data_from_kaggle(dataset: str = 'olistbr/brazilian-ecommerce') -> None:

    pwd = os.getcwd()
    os.environ['KAGGLE_CONFIG_DIR'] = f'{pwd}/.kaggle'
    os.system(f'kaggle datasets download -d {dataset}')

def extract_data_from_zip_file(file_path: str) -> None:

    name_file = file_path.split('/')[-1].strip('.zip')
    print(name_file)

    with ZipFile(file_path, 'r') as zip:
        pass
        #zip.printdir()
        #zip.extractall()

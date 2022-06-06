from extract import download_data_from_kaggle, extract_data_from_zip_file

import os
import logging
logging.basicConfig(filename='log.log', filemode='w', level=logging.INFO)

def pipeline():
    download_data_from_kaggle()
    extract_data_from_zip_file(os.getcwd()+'/brazilian-ecommerce.zip')

if __name__ == '__main__':
    pipeline()
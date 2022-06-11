import os
import logging
import subprocess
from typing import List
from zipfile36 import ZipFile

from utils import *

def extract(datasets: List[str]) -> None:

    set_kaggle_config_dir_venv()
    logging.info('Starting extract process')
    download_data_from_kaggle(datasets)
    create_dir_to_save_dataset(datasets)

def set_kaggle_config_dir_venv() -> None:
    """
    > Set the KAGGLE_CONFIG_DIR environment variable to .kaggle directory
    """

    pwd = os.getcwd()
    logging.info('Setting KAGGLE_CONFIG_DIR')
    os.environ['KAGGLE_CONFIG_DIR'] = f'{pwd}/.kaggle'

def download_data_from_kaggle(datasets: List[str]) -> None:
    """
    It takes a list of datasets as an argument and downloads them from Kaggle.

    Args:
        datasets (List[str]): List of datasets will be downloaded
    """

    for dataset in datasets:
        logging.info(f'Started to download {dataset} dataset')
        completed_process: str = subprocess.run(['kaggle', 'datasets', 'download', '-d', f'{dataset}'], capture_output=True)
        capture_output(completed_process)
        logging.info(f'Finished to download {dataset} dataset')

def create_dir_to_save_dataset(datasets: List[str]) -> None:
    """
    It creates a directory to save the dataset

    Args:
        datasets List[str]: The name of the dataset you want to download.
    """

    for dataset in datasets:
        completed_process: str = subprocess.run(['mkdir', f'data/raw/{dataset}'], capture_output=True)
        capture_output(completed_process)
        logging.info(completed_process.stderr)

def move_downloaded_dataset(dataset: str) -> None:

    os.system(f'find . -name "{dataset}.zip"')


def extract_data_from_zip_file(file_path: str, name_file: str) -> None:
    """
    It takes a zip file and extracts it to the current working directory.

    Args:
        file_path (str): The path to the zip file.
        name_file (str): The name of the file you want to extract.
    """

    name_file = name_file.strip('.zip')

    with ZipFile(file_path, 'r') as zip:
        zip.printdir()
        zip.extractall()
